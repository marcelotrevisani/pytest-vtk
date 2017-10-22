import pytest
import vtk

from pytestvtk.assert_vtk import assert_vtk


@pytest.fixture
def vtk_string_array1():
    result = vtk.vtkStringArray()
    result.SetNumberOfTuples(1)
    result.SetNumberOfValues(2)
    result.SetName('testing_string')
    result.SetValue(0, 'Value 0')
    result.SetValue(1, 'Value 1')
    return result

@pytest.fixture
def vtk_string_array2():
    result = vtk.vtkStringArray()
    result.SetNumberOfTuples(2)
    result.SetNumberOfValues(3)
    result.SetName('testing_string_modified')
    result.SetValue(0, 'Value Modified 0')
    result.SetValue(1, 'Value Modified 1')
    result.SetValue(1, 'Value Modified 2')
    return result

def test_compare_vtkStringArray(vtk_string_array1, vtk_string_array2):
    assert_vtk(vtk_string_array1, vtk_string_array1)

    with pytest.raises(pytest.fail.Exception) as excinfo:
        assert_vtk(vtk_string_array1, vtk_string_array2)
