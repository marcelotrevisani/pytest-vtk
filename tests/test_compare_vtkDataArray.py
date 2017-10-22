import pytest
import vtk

from pytestvtk.assert_vtk import assert_vtk

@pytest.fixture(params=[
                        vtk.vtkDoubleArray(),
                        vtk.vtkFloatArray(),
                        vtk.vtkIntArray(),
                        vtk.vtkIdTypeArray(),
                        vtk.vtkLongArray(),
                        vtk.vtkShortArray(),
                        vtk.vtkUnsignedCharArray(),
                        vtk.vtkUnsignedIntArray(),
                        vtk.vtkUnsignedLongArray(),
                        vtk.vtkUnsignedLongLongArray(),
                        vtk.vtkUnsignedShortArray(),
                        vtk.vtkCharArray(),
                        ])
def vtk_array(request):
    array = request.param
    array.SetName('testing_array')
    array.SetNumberOfTuples(3)
    array.SetNumberOfComponents(3)
    array.InsertTuple3(0, 1, 2, 3)
    array.InsertTuple3(1, 4, 5, 6)
    array.InsertTuple3(2, 7, 8, 9)
    return array


@pytest.fixture(params=[
                        vtk.vtkDoubleArray(),
                        vtk.vtkFloatArray(),
                        vtk.vtkIntArray(),
                        vtk.vtkIdTypeArray(),
                        vtk.vtkLongArray(),
                        vtk.vtkShortArray(),
                        vtk.vtkUnsignedCharArray(),
                        vtk.vtkUnsignedIntArray(),
                        vtk.vtkUnsignedLongArray(),
                        vtk.vtkUnsignedLongLongArray(),
                        vtk.vtkUnsignedShortArray(),
                        vtk.vtkCharArray(),
                        ])
def vtk_array_mod(request):
    array = request.param
    array.SetName('testing_array_modified')
    array.SetNumberOfTuples(4)
    array.SetNumberOfComponents(2)
    array.InsertTuple2(0, 1, 2)
    array.InsertTuple2(1, 3, 4)
    array.InsertTuple2(2, 5, 6)
    array.InsertTuple2(3, 7, 8)
    return array


def test_compare_vtkDataArray(vtk_array, vtk_array_mod):
    assert_vtk(vtk_array, vtk_array)
    assert_vtk(vtk_array_mod, vtk_array_mod)
    with pytest.raises(pytest.fail.Exception) as excinfo:
        assert_vtk(vtk_array, vtk_array_mod)






