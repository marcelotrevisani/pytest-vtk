import numpy as np
import pytest
import vtk
from vtk.util import numpy_support as ns

from pytestvtk.assert_vtk import assert_vtk


@pytest.fixture
def vtk_array():
    result = vtk.vtkCellArray()
    result.SetNumberOfCells(3)
    cells = vtk.vtkIdTypeArray()

    array = [
                2, 1, 2,
                3, 3, 4, 5,
                4, 5, 6, 7, 8
            ]

    for i in array:
        cells.InsertNextValue(i)
    result.SetCells(3, cells)
    return result


@pytest.fixture
def vtk_array_mod():
    result = vtk.vtkCellArray()
    result.SetNumberOfCells(3)
    cells = vtk.vtkIdTypeArray()

    array = [
        2, 1, 2,
        2, 3, 4,
    ]

    for i in array:
        cells.InsertNextValue(i)
    result.SetCells(2, cells)
    return result


def test_compare_vtkCellArray(vtk_array, vtk_array_mod):
    assert_vtk(vtk_array, vtk_array)
    assert_vtk(vtk_array_mod, vtk_array_mod)
    with pytest.raises(pytest.fail.Exception) as excinfo:
        assert_vtk(vtk_array, vtk_array_mod)