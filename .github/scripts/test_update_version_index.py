import json
from pathlib import Path

from update_version_index import Version, build_redirect_page, build_switcher, find_versions, main, replace_stable

BASE_URL = "/Open-Source-Template/"


def make_site(site_dir: Path, folders: list[str]) -> None:
    for folder in folders:
        (site_dir / folder).mkdir()
        (site_dir / folder / "index.html").write_text(folder)


def test_find_versions_returns_version_folders_newest_first(tmp_path: Path) -> None:
    make_site(tmp_path, ["1.9.0", "_static", "1.10.0", "stable", "1.2.2", "autoapi"])
    (tmp_path / "2.0.0").write_text("a file, not a folder")

    assert find_versions(tmp_path) == [Version(1, 10, 0), Version(1, 9, 0), Version(1, 2, 2)]


def test_build_switcher_lists_dev_and_all_versions_with_newest_as_stable() -> None:
    switcher = build_switcher([Version(1, 3, 0), Version(1, 2, 2)], BASE_URL)

    assert switcher == [
        {"name": "dev (unstable)", "version": "dev", "url": "/Open-Source-Template/dev/"},
        {"name": "1.3.0 (stable)", "version": "1.3.0", "url": "/Open-Source-Template/1.3.0/"},
        {"version": "1.2.2", "url": "/Open-Source-Template/1.2.2/"},
    ]


def test_build_switcher_without_versions_lists_only_dev() -> None:
    assert build_switcher([], BASE_URL) == [
        {"name": "dev (unstable)", "version": "dev", "url": "/Open-Source-Template/dev/"},
    ]


def test_replace_stable_copies_version_and_drops_old_files(tmp_path: Path) -> None:
    make_site(tmp_path, ["1.3.0", "stable"])
    (tmp_path / "stable" / "removed_page.html").write_text("only in the old stable")

    replace_stable(tmp_path, Version(1, 3, 0))

    assert sorted(path.name for path in (tmp_path / "stable").iterdir()) == ["index.html"]
    assert (tmp_path / "stable" / "index.html").read_text() == "1.3.0"


def test_build_redirect_page_redirects_to_stable_when_a_version_exists() -> None:
    assert 'content="0; url=stable/"' in build_redirect_page([Version(1, 3, 0)])


def test_build_redirect_page_redirects_to_dev_without_versions() -> None:
    assert 'content="0; url=dev/"' in build_redirect_page([])


def test_main_writes_switcher_stable_redirect_and_nojekyll(tmp_path: Path) -> None:
    make_site(tmp_path, ["dev", "1.2.2", "1.3.0"])

    main([str(tmp_path), "--base-url", BASE_URL])

    switcher = json.loads((tmp_path / "_static" / "switcher_config.json").read_text())
    assert [entry["version"] for entry in switcher] == ["dev", "1.3.0", "1.2.2"]
    assert (tmp_path / "stable" / "index.html").read_text() == "1.3.0"
    assert (tmp_path / "index.html").read_text() == build_redirect_page([Version(1, 3, 0)])
    assert (tmp_path / ".nojekyll").exists()
