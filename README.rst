[![pytest]](https://img.shields.io/pypi/v/pytest.svg)](https://img.shields.io/pypi/v/pytest.svg))

[![PyPI pyversions](https://img.shields.io/pypi/pyversions/Open-Source-Template.svg)](https://img.shields.io/pypi/pyversions/Open-Source-Template.svg)

[![PyPI license](https://img.shields.io/pypi/l/Open-Source-Template.svg)](https://img.shields.io/pypi/l/Open-Source-Template.svg)

[![CodeQL](https://github.com/MeteoSwiss/Open-Source-Template/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/MeteoSwiss/Open-Source-Template/actions/workflows/github-code-scanning/codeql)

[![CI_test](https://github.com/MeteoSwiss/Open-Source-Template/actions/workflows/CI_test.yaml/badge.svg)](https://github.com/MeteoSwiss/Open-Source-Template/actions/workflows/CI_test.yaml)

[![CI_publish_dev_documentation](https://github.com/MeteoSwiss/Open-Source-Template/actions/workflows/CI_publish_dev_documentation.yaml/badge.svg)](https://github.com/MeteoSwiss/Open-Source-Template/actions/workflows/CI_publish_dev_documentation.yaml)

====================
Open Source Template
====================

A demo for the OSS template at MeteoSwiss.

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
