import argparse
import importlib.metadata
import importlib.util
import json
import logging
import pkgutil
import sys
from dataclasses import replace
from importlib.metadata import entry_points
from pathlib import Path

from databricks.bundles.internal._diagnostics import (
    Diagnostics,
    Location,
    Severity,
)
from databricks.bundles.internal._loader import _Loader
from databricks.bundles.jobs.internal import dab_generator
from databricks.bundles.jobs.models.job import Job
from databricks.bundles.variables import VariableContext


def _legacy_build(module_names: list[str]) -> Diagnostics:
    generated_dir = Path("resources/__generated__")
    generated_dir.mkdir(parents=True, exist_ok=True)

    loader = _Loader()
    diagnostics = Diagnostics()

    diagnostics = diagnostics.extend(_run_load(loader, module_names, override=False))
    if diagnostics.has_error():
        return diagnostics

    diagnostics = diagnostics.extend(_run_init(loader))
    if diagnostics.has_error():
        return diagnostics

    _legacy_generate_yml(generated_dir=generated_dir, jobs=loader.jobs)

    return diagnostics


def _run_load(
    loader: _Loader,
    module_names: list[str],
    *,
    override: bool,
) -> Diagnostics:
    diagnostics = Diagnostics()

    for module_name in module_names:
        try:
            logging.debug(f"Loading '{module_name}'")

            module = importlib.import_module(module_name)

            diagnostics = diagnostics.extend(
                loader.register_module(module, override=override)
            )
        except Exception as exc:
            return diagnostics.extend(
                Diagnostics.from_exception(
                    exc=exc,
                    # TODO there must be a way to get location of the module without loading it
                    # through importlib.util.find_spec
                    location=None,
                    summary=f"Failed to load module '{module_name}'",
                )
            )

    return diagnostics


def _run_init(loader: _Loader) -> Diagnostics:
    diagnostics = Diagnostics()

    for resource_generator in loader.resource_generators:
        try:
            for resource in resource_generator.function():
                match resource:
                    case Job() as job:
                        diagnostics = diagnostics.extend(
                            loader.register_job(job, override=False)
                        )

        except Exception as exc:
            return diagnostics.extend(
                Diagnostics.from_exception(
                    exc=exc,
                    location=Location.from_callable(resource_generator.function),
                    summary=f"Failed to apply resource generator '{resource_generator.function.__name__}'",
                )
            )

    if diagnostics.has_error():
        return diagnostics

    for resource_name, job in loader.jobs.items():
        for mutator in loader.mutators:
            try:
                if mutator.resource_type == Job:
                    job = mutator.function(job)

            except Exception as exc:
                return diagnostics.extend(
                    Diagnostics.from_exception(
                        exc=exc,
                        location=Location.from_callable(mutator.function),
                        summary=f"Failed to apply job mutator '{mutator.function.__name__}' to job '{job.resource_name}'",
                    )
                )

        diagnostics = diagnostics.extend(loader.register_job(job, override=True))

    return diagnostics


def _legacy_generate_yml(generated_dir: Path, jobs: dict[str, Job]):
    for name, job in jobs.items():
        output_file = generated_dir / (name + ".yml")

        dab_generator.generate(
            output_file=output_file,
            jobs={name: job},
        )


def _detect_legacy_include(bundle: dict) -> Diagnostics:
    for include in bundle.get("include") or []:
        if include.startswith("resources/__generated__"):
            return Diagnostics.create_error(
                "Detected outdated include 'resources/__generated__' directive in databricks.yml, please remove it"
            )

    return Diagnostics()


def _detect_legacy_experimental(bundle: dict) -> Diagnostics:
    preinit = bundle.get("experimental", {}).get("scripts", {}).get("preinit", "")

    if ".databricks/generate-resources.sh" in preinit:
        return Diagnostics.create_warning(
            "Detected outdated 'experimental.scripts.preinit' in databricks.yml",
            detail="""Replace experimental.scripts.preinit with the following:
  scripts:
    preinit: |
      # create .venv if it doesn't exist
      if [ ! -e .venv ]; then
        python=$(command -v python3.10 || command -v python3.11)
    
        if [ -z "$python" ]; then
          echo "ERROR: Python 3.10 or higher is required to create virtual environment"
          exit 1
        fi
    
        $python -m venv .venv
        .venv/bin/pip install -r requirements-dev.txt
      fi""",
        )

    return Diagnostics()


def _load_bundle(
    bundle: dict,
    module_names: list[str],
    only_load: bool,
) -> tuple[dict, Diagnostics]:
    loader = _Loader()

    diagnostics = Diagnostics()
    diagnostics = diagnostics.extend(_detect_legacy_include(bundle))
    diagnostics = diagnostics.extend(_detect_legacy_experimental(bundle))

    diagnostics = diagnostics.extend(loader.register_bundle_config(bundle))

    if diagnostics.has_error():
        return {}, diagnostics

    if only_load:
        # On 'load' phase, we expect a 'clean' state and no overrides are needed
        diagnostics = diagnostics.extend(
            _run_load(loader, module_names, override=False)
        )
    else:
        # On 'init' phase, we 'bundle' contains resources from 'load' phase
        #
        # Instead of reading them as-is, we override them with resources loaded
        # in Python code, that should be equivalent. Additionally, it gives
        # us types that are erased with JSON serialization.
        #
        # For instance, all ComputeTask are serialized as Task, and instanceof checks
        # aren't going to work anymore in job mutators.

        load_diagnostics = _run_load(loader, module_names, override=True)

        # we ignore warnings in _run_load because we have already reported them at 'load' stage
        if load_diagnostics.has_error():
            return {}, load_diagnostics

        variables = {
            k: v.get("default") for k, v in bundle.get("variables", {}).items()
        }

        with VariableContext.push(variables):
            diagnostics = diagnostics.extend(_run_init(loader))

        # we double-report warnings between load and init, remove them
        diagnostics = _remove_known_warnings(
            diagnostics=diagnostics,
            known_diagnostics=load_diagnostics,
        )

    if diagnostics.has_error():
        return {}, diagnostics

    jobs_dict = dab_generator.get_jobs_json(
        # this is only used to relativize paths
        output_file=Path("__generated__.yml"),
        jobs=loader.jobs,
    )

    bundle["resources"] = bundle.get("resources", {})
    bundle["resources"]["jobs"] = jobs_dict

    return bundle, diagnostics


def _remove_known_warnings(
    *, diagnostics: Diagnostics, known_diagnostics: Diagnostics
) -> Diagnostics:
    known_warnings = {
        item for item in known_diagnostics.items if item.severity == Severity.WARNING
    }

    return replace(
        diagnostics,
        items=[item for item in diagnostics.items if item not in known_warnings],
    )


def _parse_args(args: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--where", default=None)
    parser.add_argument("--include", action="append")
    parser.add_argument("--exclude", action="append")
    parser.add_argument("--phase", default="legacy_build")
    parser.add_argument("--input", default=None)
    parser.add_argument("--output", default=None)
    parser.add_argument("--diagnostics", default=None)

    return parser.parse_args(args)


def find_modules(package: str) -> list[str]:
    import importlib.util

    spec = importlib.util.find_spec(package)

    if not spec:
        return []

    modules = [
        package + "." + module.name
        for module in pkgutil.iter_modules(path=spec.submodule_search_locations)
        # this will filter out nested packages, since we already find them using
        # find_packages
        if not module.ispkg
    ]

    return modules


def _load_module_names_from_entry_points() -> tuple[list[str], Diagnostics]:
    plugins = entry_points(group="databricks.bundles")
    diagnostics = Diagnostics()
    module_names = []

    for plugin in plugins:
        if plugin.attr:
            return [], Diagnostics.create_error(
                f"Only namespace packages are supported as entry points, but got '{plugin}'",
            )

        package = plugin.value
        package_spec = importlib.util.find_spec(package)

        if not package_spec:
            return [], Diagnostics.create_error(
                f"Package '{package}' specified as entry point in pyproject.toml is not found",
            )

        package_paths = package_spec.submodule_search_locations
        prefix = package + "."

        for loader, module_name, is_pkg in pkgutil.walk_packages(package_paths, prefix):
            module_names.append(module_name)

    return module_names, diagnostics


def _legacy_load_module_names(
    where: str,
    include: list[str],
    exclude: list[str],
) -> tuple[list[str], Diagnostics]:
    # only needed on legacy path
    import setuptools

    packages = setuptools.find_packages(
        where=where,
        include=include,
        exclude=exclude,
    )

    package_code = "\n".join([f"'{package}' = '{package}'" for package in packages])
    diagnostics = Diagnostics.create_warning(
        "PyDABs 0.5.0 introduces a new method for loading Python code, replacing the mechanism used\n"
        "in version 0.4.x, which is now deprecated. To adopt the new loading mechanism, please append\n"
        "entry-points to 'pyproject.toml' file or re-create the project from the latest template.\n"
        "\n"
        "[project.entry-points.'databricks.bundles']\n"
        f"{package_code}"
    )

    module_names = [module for package in packages for module in find_modules(package)]

    return module_names, diagnostics


def main(args) -> Diagnostics:
    module_names = []
    diagnostics = Diagnostics()

    if not args.where:
        if args.include and args.include != ["src"]:
            diagnostics = diagnostics.extend(
                Diagnostics.create_warning(
                    "--include argument is not supported without --where, "
                    "check 'scripts' section in databricks.yml"
                )
            )

        if args.exclude:
            diagnostics = diagnostics.extend(
                Diagnostics.create_warning(
                    "--exclude argument is not supported without --where, "
                    "check 'scripts' section in databricks.yml"
                )
            )

        module_names, diagnostics = diagnostics.extend_tuple(
            _load_module_names_from_entry_points()
        )

    if not module_names:
        # as fallback, use legacy discover mechanism

        # this used to be ".", but all template are using "src" that is
        # a better default
        where = args.where or "src"

        # this is not needed in PyDABs integration, it was a workaround for
        # the case where we don't have a good "venv" setup
        sys.path.append(where)

        module_names, diagnostics = diagnostics.extend_tuple(
            _legacy_load_module_names(
                where=where,
                include=args.include or ["*"],
                exclude=args.exclude or [],
            )
        )

    # if discovery fails, we have a potential to destroy resources
    # let's be safe and exit if it doesn't look correct
    if not module_names:
        return diagnostics.extend(
            Diagnostics.create_error(
                "No Python modules found, check your configuration"
            )
        )

    if diagnostics.has_error():
        return diagnostics

    try:
        if args.phase == "legacy_build":
            # integration for WAT 0.4.x
            return diagnostics.extend(_legacy_build(module_names))
        elif args.phase == "load":
            bundle = json.load(open(args.input))

            new_bundle, diagnostics = diagnostics.extend_tuple(
                _load_bundle(bundle, module_names, only_load=True)
            )

            with open(args.output, "w") as f:
                json.dump(new_bundle, f)

            return diagnostics

        elif args.phase == "init":
            # clear all warnings, because they are already reported at 'load' stage
            diagnostics = Diagnostics()
            bundle = json.load(open(args.input))

            new_bundle, diagnostics = diagnostics.extend_tuple(
                _load_bundle(bundle, module_names, only_load=False)
            )

            with open(args.output, "w") as f:
                json.dump(new_bundle, f)

            return diagnostics
        else:
            return diagnostics.extend(
                Diagnostics.create_error(f"Unknown phase '{args.phase}'")
            )
    except Exception as exc:
        return diagnostics.extend(
            Diagnostics.from_exception(
                summary="Unhandled exception in Python mutator",
                exc=exc,
            )
        )


def _legacy_print_diagnostics(diagnostics: Diagnostics):
    for diagnostic in diagnostics.items:
        log_fn = (
            logging.error if diagnostic.severity == Severity.ERROR else logging.warning
        )

        log_fn(f"{diagnostic.severity.name.upper()}: {diagnostic.summary}")
        if diagnostic.detail:
            log_fn(f"{diagnostic.detail}")
        if diagnostic.location:
            log_fn(f"at {diagnostic.location.to_text()}")


if __name__ == "__main__":
    args = _parse_args(sys.argv[1:])

    if args.phase == "legacy_build":
        # reduce logging level for legacy build, or it will be too verbose
        # to see any warnings in the output
        logging.basicConfig(level=logging.INFO, stream=sys.stderr)
    else:
        logging.basicConfig(level=logging.DEBUG, stream=sys.stderr)

    diagnostics = main(args)

    if args.diagnostics:
        with open(args.diagnostics, "w") as f:
            diagnostics.write_json(f)
    else:
        _legacy_print_diagnostics(diagnostics)

    if diagnostics.has_error():
        sys.exit(1)
    else:
        sys.exit(0)
