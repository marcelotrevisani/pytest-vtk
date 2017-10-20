import pytest
from pytestvtk.compare_vtk import compare_vtkDataArray

def test_compare_vtkDataArray(vtk_double, vtk_float, vtk_int):
    compare_vtkDataArray()


@pytest.fixture
def vtk_double():
    pass

@pytest.fixture
def vtk_float():
    pass

@pytest.fixture
def vtk_int():
    pass