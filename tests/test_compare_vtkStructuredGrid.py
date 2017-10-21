import pytest
import vtk
import numpy as np
from vtk.util import numpy_support as ns
from pytestvtk.assert_vtk import assert_vtk


@pytest.fixture
def vtk_grid():
    result = vtk.vtkStructuredGrid()
    result.Setdimensions(2, 2, 2)
    points = vtk.vtkPoints()
    array_points = ns.numpy_to_vtk(np.arange(8).reshape(8, 3))
    array_points.SetName('test_points')
    points.SetData(array_points)
    result.SetPoints(points)
    # WIP