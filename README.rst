==========
pytest-vtk
==========

.. image:: https://travis-ci.org/marcelotrevisani/pytest-vtk.svg?branch=master
    :target: https://travis-ci.org/marcelotrevisani/pytest-vtk
    :alt: See Build Status on Travis CI

.. image:: https://ci.appveyor.com/api/projects/status/github/marcelotrevisani/pytest-vtk?branch=master
    :target: https://ci.appveyor.com/project/marcelotrevisani/pytest-vtk/branch/master
    :alt: See Build Status on AppVeyor

It's a plugin for pytest to easily test the VTK objects from VTK library

----

This `Pytest`_ plugin was generated with `Cookiecutter`_ along with `@hackebrot`_'s `Cookiecutter-pytest-plugin`_ template.


Features
--------

Support for testing vtk objects such as:

* vtkDoubleArray
* vtkFloatArray
* vtkIntArray
* vtkIdTypeArray
* vtkLongArray
* vtkShortArray
* vtkUnsignedCharArray
* vtkUnsignedIntArray
* vtkUnsignedLongArray
* vtkUnsignedLongLongArray
* vtkUnsignedShortArray
* vtkPoints
* vtkPointData
* vtkCharArray
* vtkStringArray


To Do
----
* Support to test:
    * vtkSignedCharArray
    * vtkStructuredGrid
    * vtkUnstructuredGrid
    * vtkPolyData
    * vtkImageData
    * vtkRectilinearGrid
    * vtkUnicodeStringArray
    * vtkVariantArray
    * vtkBitArray
* Support for image test
* Add pytest-vtk package in conda-forge and also in Pypi



Requirements
------------

* vtk >= 7.0.0
* numpy
* pytest >= 3.1.1


Installation
------------
(Not implemented yet)
You can install "pytest-vtk" via `pip`_ from `PyPI`_::

    $ pip install pytest-vtk


Usage
-----
Just call the ``assert_vtk`` function and pass two VTK objects which will be compared.

Example:

``assert_vtk(vtk_object1, vtk_object2)``

The pytest-vtl plugin will raise an error if these two objects are different and also will show the differences.

Contributing
------------
Contributions are very welcome.

License
-------

Distributed under the terms of the `MIT`_ license, "pytest-vtk" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`MIT`: http://opensource.org/licenses/MIT
.. _`BSD-3`: http://opensource.org/licenses/BSD-3-Clause
.. _`GNU GPL v3.0`: http://www.gnu.org/licenses/gpl-3.0.txt
.. _`Apache Software License 2.0`: http://www.apache.org/licenses/LICENSE-2.0
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/marcelotrevisani/pytest-vtk/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.io/en/latest/
.. _`pip`: https://pypi.python.org/pypi/pip/
.. _`PyPI`: https://pypi.python.org/pypi
