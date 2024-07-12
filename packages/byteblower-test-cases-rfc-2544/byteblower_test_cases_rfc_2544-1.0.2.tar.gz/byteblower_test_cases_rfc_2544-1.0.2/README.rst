*****************************************
ByteBlower Test Case: RFC 2544 Throughput
*****************************************

.. footer::
   Copyright |copy| |year| - Excentis N.V.

.. |copy| unicode:: U+00A9 .. copyright sign
.. |year| date:: %Y

Introduction
============

This package contains an implementation of the `RFC 2544`_ Throughput
Test using the `ByteBlower Test Framework`_.

.. _RFC 2544: https://www.ietf.org/rfc/rfc2544.txt
.. _ByteBlower Test Framework: https://pypi.org/project/byteblower-test-framework/.

A throughput test aims to measure, under given circumstances,
the highest throughput the DUT can handle correctly without exceeding a given
threshold of frame loss (theoretically, this threshold is 0).

This ByteBlower RFC 2544 throughput test case allows you to:

#. Run throughput tests based on RFC 2544
#. Collect & Analyse statistics
#. Generate HTML & JSON reports

For more detailed documentation, please have a look
at `Test Case: RFC 2544 Throughput`_ in the ByteBlower API documentation.

.. _Test Case\: RFC 2544 Throughput: https://api.byteblower.com/test-framework/latest/test-cases/rfc-2544/overview.html

Installation
============

Requirements
------------

* `ByteBlower Test Framework`_: ByteBlower |registered| is a traffic
  generator/analyser system for TCP/IP networks.
* Highcharts-excentis_: Used for generating graphs
* jinja2_: To create HTML reports

.. _Highcharts-excentis: https://pypi.org/project/highcharts-excentis/
.. |registered| unicode:: U+00AE .. registered sign
.. _jinja2: https://pypi.org/project/Jinja2/

Prepare runtime environment
---------------------------

We recommend managing the runtime environment in a Python virtual
environment. This guarantees proper separation of the system-wide
installed Python and pip packages.

Python
------

The ByteBlower Test Framework currently supports Python versions
3.7 up to 3.11.

Important: Working directory
----------------------------

All the following sections expect that you first moved to your working
directory where you want to run this project. You may also want to create
your configuration files under a sub-directory of your choice.

#. On Unix-based systems (Linux, WSL, macOS):

   .. code-block:: shell

      cd '/path/to/working/directory'

#. On Windows systems using PowerShell:

   .. code-block:: shell

      cd 'c:\path\to\working\directory'

Python virtual environment
--------------------------

Make sure to use the right Python version (>= 3.7, <= 3.11),
list all Python versions installed in your machine by running:

#. On Windows systems using PowerShell:

   .. code-block:: shell

      py --list

If no Python version is in the required range, you can download and install
Python 3.7 or above using your system package manager
or from https://www.python.org/ftp/python.

Prepare Python virtual environment: Create the virtual environment
and install/update ``pip`` and ``build``.

#. On Unix-based systems (Linux, WSL, macOS):

   **Note**: *Mind the leading* ``.`` *which means* **sourcing**
   ``./.venv/bin/activate``.

   .. code-block:: shell

      python3 -m venv --clear .venv
      . ./.venv/bin/activate
      pip install -U pip build

#. On Windows systems using PowerShell:

   **Note**: On Microsoft Windows, it may be required to enable the
   Activate.ps1 script by setting the execution policy for the user.
   You can do this by issuing the following PowerShell command:

   .. code-block:: shell

      PS C:> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

   See `About Execution Policies`_ for more information.

   Make sure to specify the python version you're using.
   For example, for Python 3.8:

   .. code-block:: shell

      py -3.8 -m venv --clear .venv
      & ".\.venv\Scripts\activate.ps1"
      python -m pip install -U pip build

   .. _About Execution Policies: https://go.microsoft.com/fwlink/?LinkID=135170

To install the ByteBlower RFC 2544 throughput test case and its dependencies,
first make sure that you have activated your virtual environment:

#. On Unix-based systems (Linux, WSL, macOS):

   .. code-block:: shell

      . ./.venv/bin/activate

#. On Windows systems using PowerShell:

   .. code-block:: shell

      ./.venv/Scripts/activate.ps1

Then, run:

.. code-block:: shell

   pip install -U byteblower-test-cases-rfc-2544

Quick start
===========

Command-line interface
----------------------

After providing the appropriate test setup and frame configurations,
the test script can be run either as python module or as a command-line script.

For example (*to get help for the command-line arguments*):

#. As a python module:

   .. code-block:: shell

      # To get help for the command-line arguments:
      python -m byteblower.test_cases.rfc_2544 --help

#. As a command-line script:

   .. code-block:: shell

      # To get help for the command-line arguments:
      byteblower-test-cases-rfc-2544-throughput --help

For a quick start, you can run a simple test using the JSON configuration of
one of the example files below:

* Using `ByteBlower Ports scenario <https://api.byteblower.com/test-framework/json/test-cases/rfc-2544/port/rfc_2544.json>`_
* Using `ByteBlower Endpoint scenario <https://api.byteblower.com/test-framework/json/test-cases/rfc-2544/endpoint/rfc_2544.json>`_

Save you configuration in your working directory as ``rfc_2544.json``.
Make sure you change the ``"server"`` and ``"ports"`` configuration
according to the setup you want to run your test on.

More detailed documentation is available in the `Configuration file`_ section
of the documentation.

.. _Configuration file: https://api.byteblower.com/test-framework/latest/test-cases/rfc-2544/config.html

The ``rfc_2544.json`` can be used then to run the test in the
command line interface using the following commands:

**Note**: *The reports will be stored under a subdirectory* ``reports/``.

#. On Unix-based systems (Linux, WSL, macOS):

   .. code-block:: shell

      # Optional: create rfc_2544.json, then copy the configuration to it
      touch rfc_2544.json
      # Create reports folder to store HTML/JSON files
      mkdir reports
      # Run test
      byteblower-test-cases-rfc-2544-throughput --report-path reports

#. On Windows systems using PowerShell:

   .. code-block:: shell

      # Optional: create rfc_2544.json, then copy the configuration to it
      New-Item rfc_2544.json
      # Create reports folder to store HTML/JSON files
      md reports
      # Run test
      byteblower-test-cases-rfc-2544-throughput --report-path reports

Integrated
----------

.. code-block:: python

   from byteblower.test_cases.rfc_2544 import run

   # Defining test configuration, report path and report file name prefix:
   test_config = {} # Here you should provide your test setup + frame(s') configuration(s)
   report_path = 'my-output-folder' # Optional: provide the path to the output folder, defaults to the current working directory
   report_prefix = 'my-dut-feature-test' # Optional: provide prefix of the output files, defaults to 'report'

   # Run the RFC 2544 throughput test:
   run(test_config, report_path=report_path, report_prefix=report_prefix)
