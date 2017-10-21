import numpy as np
import pytest
import vtk
from vtk.util import numpy_support as ns

from pytestvtk.assert_vtk import assert_vtk


@pytest.fixture
def vtk_points():
    result = vtk.vtkPoints()
    np_array = np.arange(9).reshape(3, 3)
    array = ns.numpy_to_vtk(np_array)
    array.SetName('test_points')
    array._np = np_array
    result.SetData(array)
    return result

@pytest.fixture
def vtk_points_mod():
    result = vtk.vtkPoints()
    np_array = np.arange(12).reshape(4, 3)
    array = ns.numpy_to_vtk(np_array)
    array._np = np_array
    array.SetName('test_points_modified')
    result.SetData(array)
    return result

def test_compare_vtkPoints(vtk_points):
    assert_vtk(vtk_points, vtk_points)

def test_compare_vtkPoints_fail(vtk_points, vtk_points_mod):
    with pytest.raises(pytest.fail.Exception) as excinfo:
        assert_vtk(vtk_points, vtk_points_mod)