import vtk
import numpy as np
import numpy.testing as nt
from vtk.util import numpy_support as ns

def compare_vtk(vtk_expect, vtk_compare):
    '''
    Test if two VTK objects are equal
    :param vtk_expect: Receives the VTK object expected
    :param vtk_compare: Receives the VTK object which will be compared
    :return: True if the objects have the same values and False otherwise
    '''
    if not isinstance(vtk_expect, vtk_compare):
        # erro de objetos diferentes
        pass

    if isinstance(vtk_compare, vtk.vtkStructuredGrid):
        compare_vtkStructuredGrid(vtk_expect, vtk_compare)
    elif isinstance(vtk_compare, vtk.vtkUnstructuredGrid):
        pass
    elif isinstance(vtk_compare, vtk.vtkPolyData):
        pass
    elif isinstance(vtk_compare, vtk.vtkDataArray):
        pass


def compare_vtkStructuredGrid(vtk_expect, vtk_compare):
    '''
    Receives two vtkStructuredGrid and compare if they are equal.
    :param vtk_expect: vtkStructuredGrid expected
    :param vtk_compare: vtkStructuredGrid to compare
    '''
    exp_points = ns.vtk_to_numpy(vtk_expect.GetPoints().GetData())
    exp_scalars = ns.vtk_to_numpy(vtk_expect.GetPointData().GetScalars())
    exp_ghost = None

    if vtk_expect.GetPointGhostArray():
        exp_ghost = ns.vtk_to_numpy(vtk_expect.GetPointGhostArray())

    cmp_points = ns.vtk_to_numpy(vtk_compare.GetPoints().GetData())
    cmp_scalars = ns.vtk_to_numpy(vtk_compare.GetPointData().GetScalars())
    cmp_ghost = None

    if vtk_compare.GetPointGhostArray():
        cmp_ghost = ns.vtk_to_numpy(vtk_compare.GetPointGhostArray())

    list_errors = []

    if vtk_expect.GetNumberOfPoints() != vtk_compare.GetNumberOfPoints():
        list_errors.append('The number of points are different. Expected: {}, received: '
                           '{}'.format(vtk_expect.GetNumberOfPoints(), vtk_compare.GetNumberOfPoints()))

    if vtk_expect.GetDimensions() != vtk_compare.GetDimensions():
        list_errors.append('The dimensions are different. Expected: {}, received: '
                           '{}'.format(vtk_expect.GetDimensions(), vtk_compare.GetDimensions()))

    if vtk_expect.GetPoints().GetData().GetName() != vtk_compare.GetPoints().GetData().GetName():
        list_errors.append('The name of the points data structure  are different. '
                           'Expected: {} , Received: {}'.format(vtk_expect.GetPoints().GetData().GetName(),
                                                                vtk_compare.GetPoints().GetData().GetName()))

    try:
        nt.assert_array_equal(exp_points, cmp_points)
    except AssertionError as msg:
        list_errors.append('The vtkStructuredGrid points compared are not equal. \n'
                           '{}'.format(msg.message))

    if vtk_expect.GetPointData().GetScalars().GetName() != vtk_compare.GetPointData().GetScalars().GetName():
        list_errors.append('The name of the scalars data structure  are different. '
                           'Expected: {} , Received: {}'.format(vtk_expect.GetPointData().GetScalars().GetName(),
                                                                vtk_compare.GetPointData().GetScalars().GetName()))

    try:
        nt.assert_array_equal(exp_scalars, cmp_scalars)
    except AssertionError as msg:
        list_errors.append('The vtkStructuredGrid scalars compared are not equal. \n'
                           '{}'.format(msg.message))

    if not (exp_ghost is None and cmp_ghost is None) and \
            vtk_expect.GetPointGhostArray().GetName() != vtk_compare.GetPointGhostArray().GetName():
        list_errors.append('The name of the ghost data structure  are different. '
                           'Expected: {} , Received: {}'.format(vtk_expect.GetPointGhostArray().GetName(),
                                                                vtk_compare.GetPointGhostArray().GetName()))

    try:
        nt.assert_array_equal(exp_ghost, cmp_ghost)
    except AssertionError as msg:
        list_errors.append('The vtkStructuredGrid ghost compared are not equal. \n'
                           '{}'.format(msg.message))

