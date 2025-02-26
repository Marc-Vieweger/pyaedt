Installation
============

PyAEDT consolidates and extends all existing capital around scripting for Ansys Electronics Desktop (AEDT), allowing re-use of existing code, sharing of best practices, and collaboration.

This PyAnsys library has been tested on HFSS, Icepak, and Maxwell 3D. It also provides basic support for EDB and Circuit (Nexxim).

Requirements
~~~~~~~~~~~~
In addition to the runtime dependencies listed in the installation information, PyAEDT requires ANSYS EM Suite 2021 R1 or later.

.. todo::
   Add how to install from the AEDT installer like as in https://mapdldocs.pyansys.com/getting_started/running_mapdl.html


Installing on CPython v3.7-v3.9 from pypi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Install the prerequisite packages ``pythonnet`` and ``pywin32`` with:

.. code:: python

    pip install pyaedt


Offline PyAEDT installation from a wheelhouse
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PyAEDT can be installed from one of the wheelhouse available in the release assets.
Wheelhouses have been added starting from release v0.4.70.
They are available for CPython 3.7, 3.8 and 3.9.

This can be helpful for users part of companies restricting access to external network.
They can install PyAEDT and all its dependencies from one single entry point that can be shared internally.
It will ease the review of the PyAEDT package content for security reasons.

For instance, here is the command to execute to install PyAEDT package and all its dependencies.

.. code::

    pip install --no-cache-dir --no-index --find-links=file:///<path_to_wheelhouse>/PyAEDT-v<release_version>-wheelhouse-Windows-3.7 pyaedt


Installing PyAEDT from a Batch File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
AEDT already includes CPython 3.7, which can be used to run PyAEDT.
If you are running on Windows, you can download
:download:`PyAEDT Environment with IDE bat file <pyaedt_with_IDE.bat>`
and run this batch file on your local machine. Using this approach
provides you with a complete IDE for writing PyAEDT scripts in Windows
with a simple batch file.

This batch file executes these steps:

1. Creates a Python virtual environment in your ``%APPDATA%`` folder. To accomplish
   this, it uses CPython in the latest installed version of AEDT on your machine.
2. Installs PyAEDT.
3. Installs `Spyder <https://www.spyder-ide.org/>`_.
4. Installs `Jupyter Lab <https://jupyter.org/>`_.
5. Creates a symbolic link from your PyAEDT installation to AEDT ``PersonalLib`` so
   that scripts can also be run within AEDT.
6. Updates PyAEDT.
7. Runs the tool you choose (Spyder, Jupyter Lab, or a simple console).

Steps 1 through 5 are executed only the first time that you run the batch file or when -f is used.

.. code::

    pyaedt_with_IDE.bat --force-install

    pyaedt_with_IDE.bat -f

Step 6 is executed only when running the command with the ``-update`` option:

.. code::

    pyaedt_with_IDE.bat --update

    pyaedt_with_IDE.bat -u

Optionally the user can decide to pass a python path. It will be used to create the new virtual environment.

.. code::

    pyaedt_with_IDE.bat -f -p <path-to-python-root-folder>


In addition, it is possible to install PyAEDT package and all its dependencies provided in the wheelhouse by
executing the bat file mentioned above. Wheelhous 3.7 package has to be used in case no python path is provided.
Otherwise the correct wheelhouse has to be downloaed and used.

.. code::

    pyaedt_with_IDE.bat-w <path_to_wheelhouse>PyAEDT-v<release_version>-wheelhouse-Windows-3.7

    pyaedt_with_IDE.bat -p <path-to-python3.8-root-folder> -w <path_to_wheelhouse>PyAEDT-v<release_version>-wheelhouse-Windows-3.8
    pyaedt_with_IDE.bat -p <path-to-python3.7-root-folder> -w <path_to_wheelhouse>PyAEDT-v<release_version>-wheelhouse-Windows-3.7
    pyaedt_with_IDE.bat -p <path-to-python3.9-root-folder> -w <path_to_wheelhouse>PyAEDT-v<release_version>-wheelhouse-Windows-3.9


Using IronPython in AEDT
~~~~~~~~~~~~~~~~~~~~~~~~
To use IronPython in AEDT:

1. Download the PyAEDT package from ``https://pypi.org/project/pyaedt/#files``
2. Extract the files.
3. Install PyAEDT into Electronics Desktop, specifying the full paths to ``ipy64`` and ``setup-distutils.py`` as needed:

.. code::

    ipy64 setup-distutils.py install --user