"""Update the version index of the documentation site checked out from the gh-pages branch.

Writes the version switcher configuration from the version folders found in the site and replaces the `stable` folder
with a copy of the newest version.
"""
import argparse
import json
import re
import shutil
from dataclasses import dataclass
from pathlib import Path

VERSION_PATTERN = re.compile(r"(\d+)\.(\d+)\.(\d+)")
SWITCHER_PATH = Path("_static") / "switcher_config.json"
STABLE_FOLDER = "stable"


def main(arguments: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site_dir", type=Path, help="Root folder of the gh-pages checkout.")
    parser.add_argument("--base-url", required=True, help="URL path the site is served from, e.g. /Repository/.")
    options = parser.parse_args(arguments)

    versions = find_versions(options.site_dir)
    write_switcher(options.site_dir, build_switcher(versions, options.base_url))
    if versions:
        replace_stable(options.site_dir, versions[0])


@dataclass(frozen=True, order=True)
class Version:
    major: int
    minor: int
    patch: int

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"


def find_versions(site_dir: Path) -> list[Version]:
    """Return the versions with a documentation folder in the site, newest first."""
    matches = (VERSION_PATTERN.fullmatch(path.name) for path in site_dir.iterdir() if path.is_dir())
    return sorted((Version(*map(int, match.groups())) for match in matches if match), reverse=True)


def build_switcher(versions: list[Version], base_url: str) -> list[dict[str, str]]:
    """Return the pydata-sphinx-theme switcher entries: dev, then every version with the newest one named stable."""
    switcher = [{"name": "dev (unstable)", "version": "dev", "url": base_url}]
    switcher.extend({"version": str(version), "url": f"{base_url}{version}/"} for version in versions)
    if versions:
        switcher[1] = {"name": f"{versions[0]} (stable)", **switcher[1]}
    return switcher


def write_switcher(site_dir: Path, switcher: list[dict[str, str]]) -> None:
    path = site_dir / SWITCHER_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(switcher, indent=2) + "\n")


def replace_stable(site_dir: Path, version: Version) -> None:
    """Replace the stable folder with a copy of the given version, so no page of an older release remains."""
    stable_dir = site_dir / STABLE_FOLDER
    shutil.rmtree(stable_dir, ignore_errors=True)
    shutil.copytree(site_dir / str(version), stable_dir)


if __name__ == "__main__":
    main()
