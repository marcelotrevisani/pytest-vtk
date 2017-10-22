import pytest
import vtk
import numpy as np
from vtk.util import numpy_support as ns
from pytestvtk.assert_vtk import assert_vtk


@pytest.fixture
def vtk_grid1():
    result = vtk.vtkStructuredGrid()
    result.SetDimensions(2, 2, 2)
    points = vtk.vtkPoints()
    np_points = np.arange(9).reshape(3, 3)

    array_points = ns.numpy_to_vtk(np_points)
    array_points.SetName('test_points')
    array_points._np = np_points

    points.SetData(array_points)
    result.SetPoints(points)
    np_scalars = np.arange(3)
    scalars = ns.numpy_to_vtk(np_scalars)
    scalars._np = scalars

    result.GetPointData().SetScalars(scalars)
    result.BlankPoint(0)
    result.UnBlankPoint(1)
    result.UnBlankPoint(2)

    return result


@pytest.fixture
def vtk_grid2():
    result = vtk.vtkStructuredGrid()
    result.SetDimensions(2, 2, 1)
    points = vtk.vtkPoints()
    np_points = np.arange(12).reshape(4, 3)

    array_points = ns.numpy_to_vtk(np_points)
    array_points.SetName('test_points_mod')
    array_points._np = np_points

    points.SetData(array_points)
    result.SetPoints(points)
    np_scalars = np.arange(4)
    scalars = ns.numpy_to_vtk(np_scalars)
    scalars._np = scalars

    result.GetPointData().SetScalars(scalars)
    result.BlankPoint(0)
    result.UnBlankPoint(1)
    result.UnBlankPoint(2)
    result.UnBlankPoint(3)

    return result

def test_compare_vtkStructuredGrid(vtk_grid1, vtk_grid2):
    assert_vtk(vtk_grid1, vtk_grid1)
    assert_vtk(vtk_grid2, vtk_grid2)
    with pytest.raises(pytest.fail.Exception) as excinfo:
        assert_vtk(vtk_grid1, vtk_grid2)

