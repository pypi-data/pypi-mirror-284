
=====================
swagger-coverage-py
=====================

This project is the adapter that allows using swagger-coverage_ tool in Python projects (PyTest+Requests).
=============================================================================================================================================================

.. _swagger-coverage: https://github.com/viclovsky/swagger-coverage

Original description summary:
-----------------------------

    Swagger-coverage gives a full picture about coverage of API tests
    (regression) based on OAS 2 (Swagger). By saying coverage we mean
    not a broad theme functionality, but presence (or absence) of calls
    defined by API methods, parameters, return codes or other conditions
    which corresponds specification of API.

Some more info about the project you can also find HERE_

.. _HERE: https://viclovsky.github.io/%D0%B0%D0%B2%D1%82%D0%BE%D1%82%D0%B5%D1%81%D1%82%D1%8B%20%D0%BD%D0%B0%20api/2020/01/16/swagger-coverage

How to use:
===========

All required steps are listed below. Additionally, you can find a
working example  here allure-results-sample_:

.. _allure-results-sample: allure-results-sample <https://github.com/JamalZeynalov/allure-results-sample

0. Resolve dependencies:
========================

-  python 3.6+
-  java JDK 11+ (with JAVA\_HOME environment variable set)
-  Enable Long Paths (Windows only). Check the guide_

.. _guide: https://docs.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation#enable-long-paths-in-windows-10-version-1607-and-later

1. Add the session-scoped fixture
=================================

    .. code-block:: python

        import pytest
        from swagger_coverage_py.reporter import CoverageReporter
        from requests.auth import HTTPBasicAuth


        @pytest.fixture(scope="session", autouse=True)
        def setup_swagger_coverage():
            reporter = CoverageReporter(api_name="my-project", host="http://my-project.com")
            reporter.cleanup_input_files()
            reporter.setup("/api/v1/resources/my_project/doc/swagger.json", auth=HTTPBasicAuth("username", "password"))

            yield
            reporter.generate_report()


If you have 2 and more projects, then just add more reporters:
==============================================================

    .. code-block:: python

        import pytest
        from swagger_coverage_py.reporter import CoverageReporter
        from requests.auth import HTTPBasicAuth


        @pytest.fixture(scope="session", autouse=True)
        def setup_swagger_coverage():
            reporter = CoverageReporter(api_name="petstore", host="https://petstore.swagger.io")
            reporter.cleanup_input_files()
            reporter.setup(path_to_swagger_json="/v2/swagger.json")

            reporter2 = CoverageReporter(api_name="my-project", host="http://my-project.com")
            reporter2.cleanup_input_files()
            reporter2.setup(path_to_swagger_json="/api/v1/swagger.json", auth=HTTPBasicAuth("username", "password"))

            yield
            reporter.generate_report()
            reporter2.generate_report()

Steps and Parameters:
=====================

        ``api_name`` - Define the name of the API. This name will be used to
        find a configuration file.      For APIs in this example the files
        must have names ``swagger-coverage-config-petstore.json`` and
        ``swagger-coverage-config-my-project.json``.

        ``host`` - The host of the API. It will be used to download a
        swagger.json file and to identify the CoverageListener output
        directory for each API.

        ``cleanup_input_files()`` - THis step deletes all files in the
        CoverageListener output directory (according to the target host)

        ``path_to_swagger_json`` - A second part of the HTTP link to your
        OpenApi/Swagger documentation in JSON format      Adapted
        ``swagger-<api_name>.json`` file will be created in your project
        root.      The "Swagger 2.0" format is completely compatible with
        this tool.      The "OpenAPI 3.0.2" format is partly compatible.
        "Tags coverage summary" calculation is not supported.

        ``auth`` - An authentication parameter for "requests" lib. Skip it
        if your API doesn't require authentication.

2. Create and place ``swagger-coverage-config-<api_name>.json`` file(s) to your project:
========================================================================================

.. code-block:: python

    {
      "rules": {
        "status": {
          "enable": true,
          "ignore": [
            "500"
          ],
          "filter": []
        },
        "only-declared-status": {
          "enable": false
        },
        "exclude-deprecated": {
          "enable": true
        }
      },
      "writers": {
        "html": {
          "locale": "en",
          "filename": "swagger-coverage-report-petstore.html"
        }
      }
    }

If you have more than 1 API then this config MUST:
==================================================
| 1. Be created for each microservice which you track using ``CoverageListener``.

    Otherwise, the default behavior will be applied, and your report
    will be saved as ``swagger-coverage-report.html`` which may cause
    override in case you have multiple APIs

| 2. Contain *writers* section with filename in the format:
    *swagger-coverage-report-<api_name>.html*

| 3. Be placed in the root of your project

More examples of configuration options you can find in the Configuration options_ section of the documentation.

.. _options: https://github.com/JamalZeynalov/swagger-coverage#configuration-options

3. Trace all your API calls with CoverageListener:
==================================================

.. code-block:: python

    from requests import Response
    from requests.auth import HTTPBasicAuth
    from swagger_coverage_py.listener import CoverageListener

    response: Response = CoverageListener(
        method="get",
        base_url="https://petstore.swagger.io",
        raw_path="/v2/store/order/{orderId}",
        uri_params={"orderId": 1},
        auth=HTTPBasicAuth("username", "password"),
        params={"type": "active"},
    ).response

Note: "auth" and "params" arguments are default for "requests" lib and are not required. You can use any other \*\*kwargs that are applicable for Requests library.

4. Run your tests and open created *swagger-coverage-report-<api_name>.html* report(s) in your browser.
=========================================================================================================


How it works:
=============

1. The fixture ``setup_swagger_coverage`` setups required artifacts
2. During test execution the CoverageListener saves all requests as JSON
   files in swagger format to a subdirectory named as a called host.
   (e.g. ``swagger-coverage-output/petstore.swagger.io/``).
3. After all tests execution a ``CoverageReporter().generate_report()``
   creates and saves new report(s) into your project root.

Created & Maintained By
-----------------------

`Jamal Zeinalov`_

.. _`Jamal Zeinalov`: https://github.com/JamalZeynalov

License
-------

Swagger coverage is released under version 2.0 of the `Apache License`_

.. _`Apache License`: http://www.apache.org/licenses/LICENSE-2.0
