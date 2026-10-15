.. image:: https://img.shields.io/pypi/v/Open-Source-Template.svg
    :target: https://pypi.org/project/Open-Source-Template/

.. image:: https://img.shields.io/pypi/pyversions/Open-Source-Template.svg
    :target: https://pypi.org/project/Open-Source-Template/

.. image:: https://img.shields.io/pypi/l/Open-Source-Template.svg
    :target: https://pypi.org/project/Open-Source-Template/

.. image:: https://github.com/MeteoSwiss/Open-Source-Template/actions/workflows/github-code-scanning/codeql/badge.svg
    :target: https://github.com/MeteoSwiss/Open-Source-Template/actions/workflows/github-code-scanning/codeql

.. image:: https://github.com/MeteoSwiss/Open-Source-Template/actions/workflows/CI_test.yaml/badge.svg
    :target: https://github.com/MeteoSwiss/Open-Source-Template/actions/workflows/CI_test.yaml

.. image:: https://github.com/MeteoSwiss/Open-Source-Template/actions/workflows/CI_publish_dev_documentation.yaml/badge.svg
    :target: https://github.com/MeteoSwiss/Open-Source-Template/actions/workflows/CI_publish_dev_documentation.yaml

===============
Getting Started
===============

A demo for the OSS template at MeteoSwiss.

The template can be use as an example how to configure MeteoSwiss Github projects.

It uses:

* Github actions to execute the CI/CD pipelines
* Github pages to host the documentation
* PyPI to publish the python packages

Development Setup with Poetry
-----------------------------

Building the Project
''''''''''''''''''''
.. code-block:: console

    $ cd open-source-template
    $ poetry install

Run Tests
'''''''''

.. code-block:: console

    $ poetry run pytest

Run Quality Tools
'''''''''''''''''

.. code-block:: console

    $ poetry run pylint open_source_template
    $ poetry run mypy open_source_template

Generate Documentation
''''''''''''''''''''''

.. code-block:: console

    $ poetry run sphinx-build doc doc/_build

Then open the index.html file generated in *open-source-template/doc/_build/*.

Build wheels
''''''''''''

.. code-block:: console

    $ poetry build

Using the Library
-----------------

To install open-source-template in your project, run this command in your terminal:

.. code-block:: console

    $ poetry add open-source-template

You can then use the library in your project through

    import open_source_template

Releasing
---------

Releases use the `GitHub CLI <https://cli.github.com/>`_ (``gh``). Replace ``X.Y.Z`` with the release version.

#. Add a ``Version X.Y.Z`` section with the release changes to ``CHANGELOG.rst`` and merge it into ``main`` through a
   pull request.

#. Create the release and its tag ``X.Y.Z`` (no ``v`` prefix) on ``main``:

   .. code-block:: console

       $ gh release create X.Y.Z --target main --title X.Y.Z --generate-notes

   Leave the version in ``pyproject.toml`` at ``0.0.0``: the pipeline sets it from the tag.

The tag starts the ``CI_publish`` workflow, which:

* publishes the package to PyPI
* publishes the documentation to ``https://meteoswiss.github.io/Open-Source-Template/X.Y.Z/``
* adds the release to the version switcher and points ``https://meteoswiss.github.io/Open-Source-Template/stable/`` to
  the newest release
