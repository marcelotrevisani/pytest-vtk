import pytest
import vtk

from pytestvtk._compare_vtkPointData import _compare_vtkPointData
from pytestvtk._compare_vtkPoints import _compare_vtkPoints
from pytestvtk.base_array._compare_vtkDataArray import _compare_vtkDataArray
from pytestvtk.base_array._compare_vtkStringArray import _compare_vtkStringArray
from pytestvtk.base_grids._compare_vtkStructuredGrid import _compare_vtkStructuredGrid


def assert_vtk(vtk_expect, vtk_compare):
    '''
    Test if two VTK objects are equal
    :param vtk_expect: Receives the VTK object expected
    :param vtk_compare: Receives the VTK object which will be compared
    :return: True if the objects have the same values and False otherwise
    '''
    list_errors = []
    if isinstance(vtk_compare, vtk.vtkStructuredGrid) and isinstance(vtk_expect, vtk.vtkStructuredGrid):
        list_errors = _compare_vtkStructuredGrid(vtk_expect, vtk_compare)
    elif isinstance(vtk_compare, vtk.vtkUnstructuredGrid) and isinstance(vtk_expect, vtk.vtkUnstructuredGrid):
        pass
    elif isinstance(vtk_compare, vtk.vtkPolyData) and isinstance(vtk_expect, vtk.vtkPolyData):
        pass
    elif isinstance(vtk_compare, vtk.vtkPoints) and isinstance(vtk_expect, vtk.vtkPoints):
        list_errors = _compare_vtkPoints(vtk_expect, vtk_compare)
    elif isinstance(vtk_compare, vtk.vtkPointData) and isinstance(vtk_expect, vtk.vtkPointData):
        list_errors = _compare_vtkPointData(vtk_expect, vtk_compare)
    elif isinstance(vtk_compare, vtk.vtkStringArray) and isinstance(vtk_expect, vtk.vtkStringArray):
        list_errors = _compare_vtkStringArray(vtk_expect, vtk_compare)
    elif isinstance(vtk_compare, vtk.vtkUnicodeStringArray) and isinstance(vtk_expect, vtk.vtkUnicodeStringArray):
        pass
    elif isinstance(vtk_compare, vtk.vtkVariantArray) and isinstance(vtk_expect, vtk.vtkVariantArray):
        pass
    elif isinstance(vtk_compare, vtk.vtkDataArray) and isinstance(vtk_expect, vtk.vtkDataArray):
        list_errors = _compare_vtkDataArray(vtk_expect, vtk_compare)

    if list_errors:
        pytest.fail('\n\n'.join(list_errors))


