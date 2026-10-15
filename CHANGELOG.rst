=========
Changelog
=========

Version 1.3.0
-------------

* Upgrade to poetry 2.x
* Restructure the GitHub Actions workflows into ``ci.yml`` and ``release.yml`` (see ``.github/WORKFLOWS.md``): publish
  only after all checks pass, build the package on every pull request, and publish the dev documentation to ``dev/``
  with the site root redirecting to ``stable/``.
* Fix the documentation version switcher: set ``html_static_path`` so that ``doc/_static/switcher_config.json`` is
  published with the documentation again (it was no longer copied since the sphinx configuration was simplified).

Version 1.2.3
-------------

* Enhance the documentation header and footer by displaying the MCH logo in the header and the package version and build information in the footer.
* Simplify the sphinx configuration to include only the strictly necessary settings.

Version 1.2.2
-------------
* Use global version switcher configuration


Version 1.2.0
-------------
* Integrated multi-versioning feature in documentation pages


Version 1.1.0
-------------
* Added `another_dummy_func` to `main.py` that converts an integer to a float.
* Updated this Changelog


Version 1.0.0
----------------

* Initial release.