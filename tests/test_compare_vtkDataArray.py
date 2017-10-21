import pytest
import vtk

from pytestvtk.compare_vtk import compare_vtk

list_vtk_array = [
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
                ]

@pytest.fixture(params=list_vtk_array)
def vtk_array(request):
    array = request.param
    array.SetName('testing_array')
    array.SetNumberOfTuples(3)
    array.SetNumberOfComponents(3)
    array.InsertTuple3(0, 1, 2, 3)
    array.InsertTuple3(1, 4, 5, 6)
    array.InsertTuple3(2, 7, 8, 9)
    return array


@pytest.fixture(params=list_vtk_array)
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


def test_compare_vtkDataArray(vtk_array):
    compare_vtk(vtk_array, vtk_array)

# def test_compare_vtkDataArray_fail(vtk_array, vtk_array_mod):
#     compare_vtk(vtk_array, vtk_array_mod)






