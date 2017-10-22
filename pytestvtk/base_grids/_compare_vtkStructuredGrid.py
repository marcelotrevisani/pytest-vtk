from pytestvtk._compare_vtkPointData import _compare_vtkPointData
from pytestvtk._compare_vtkPoints import _compare_vtkPoints
from pytestvtk.base_array._compare_vtkDataArray import _compare_vtkDataArray


def _compare_vtkStructuredGrid(vtk_expect, vtk_compare):
    '''
    Receives two vtkStructuredGrid and compare if they are equal.
    :param vtk_expect: vtkStructuredGrid expected
    :param vtk_compare: vtkStructuredGrid to compare
    '''
    list_errors = []

    if vtk_expect.GetNumberOfPoints() != vtk_compare.GetNumberOfPoints():
        list_errors.append('The number of points are different. Expected: {}, received: '
                           '{}'.format(vtk_expect.GetNumberOfPoints(), vtk_compare.GetNumberOfPoints()))

    if vtk_expect.GetDimensions() != vtk_compare.GetDimensions():
        list_errors.append('The dimensions are different. Expected: {}, received: '
                           '{}'.format(vtk_expect.GetDimensions(), vtk_compare.GetDimensions()))

    if vtk_expect.GetNumberOfCells() != vtk_compare.GetNumberOfCells():
        list_errors.append('The number of cells are different. Expected: {}, received: '
                           '{}'.format(vtk_expect.GetNumberOfCells(), vtk_compare.GetNumberOfCells()))

    exp_points = vtk_expect.GetPoints()
    exp_point_data = vtk_expect.GetPointData()

    cmp_points = vtk_compare.GetPoints()
    cmp_point_data = vtk_compare.GetPointData()

    list_errors = list_errors + _compare_vtkDataArray(vtk_expect.GetPointGhostArray(), vtk_compare.GetPointGhostArray())

    list_errors = list_errors + _compare_vtkPoints(exp_points, cmp_points)

    list_errors = list_errors + _compare_vtkPointData(exp_point_data, cmp_point_data)

    return list_errors