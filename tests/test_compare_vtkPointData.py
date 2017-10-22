import vtk
import pytest
import numpy as np
from vtk.util import numpy_support as ns

from pytestvtk.assert_vtk import assert_vtk


@pytest.fixture
def vtk_point_data1():
    result = vtk.vtkPointData()
    result._scalars = np.arange(3)
    scalars = ns.numpy_to_vtk(result._scalars)
    result.SetScalars(scalars)

    result._vectors = np.arange(3, 6)
    vectors = ns.numpy_to_vtk(result._vectors )
    result.SetVectors(vectors)

    result._normals = np.arange(6, 9)
    normals = ns.numpy_to_vtk(result._normals )
    result.SetNormals(normals)

    result._tensors = np.arange(9, 12)
    tensors = ns.numpy_to_vtk(result._tensors)
    result.SetTensors(tensors)

    return result

@pytest.fixture
def vtk_point_data2():
    result = vtk.vtkPointData()
    result._scalars = np.arange(3, 6)
    scalars = ns.numpy_to_vtk(result._scalars )
    result.SetScalars(scalars)

    result._vectors = np.arange(6, 9)
    vectors = ns.numpy_to_vtk(result._vectors)
    result.SetVectors(vectors)

    result._normals = np.arange(9, 12)
    normals = ns.numpy_to_vtk(result._normals)
    result.SetNormals(normals)

    result._tensors = np.arange(12, 15)
    tensors = ns.numpy_to_vtk(result._tensors)
    result.SetTensors(tensors)

    return result


def test_compare_vtkPointData(vtk_point_data1, vtk_point_data2):
    assert_vtk(vtk_point_data1, vtk_point_data1)
    with pytest.raises(pytest.fail.Exception) as excinfo:
        assert_vtk(vtk_point_data1, vtk_point_data2)
