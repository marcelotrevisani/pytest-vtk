import numpy.testing as nt
import pytest
import vtk
from vtk.util import numpy_support as ns


def compare_vtk(vtk_expect, vtk_compare):
    '''
    Test if two VTK objects are equal
    :param vtk_expect: Receives the VTK object expected
    :param vtk_compare: Receives the VTK object which will be compared
    :return: True if the objects have the same values and False otherwise
    '''
    if isinstance(vtk_compare, vtk.vtkStructuredGrid) and isinstance(vtk_expect, vtk.vtkStructuredGrid):
        compare_vtkStructuredGrid(vtk_expect, vtk_compare)
    elif isinstance(vtk_compare, vtk.vtkUnstructuredGrid) and isinstance(vtk_expect, vtk.vtkUnstructuredGrid):
        pass
    elif isinstance(vtk_compare, vtk.vtkPolyData) and isinstance(vtk_expect, vtk.vtkPolyData):
        pass
    elif isinstance(vtk_compare, vtk.vtkDataArray) and isinstance(vtk_expect, vtk.vtkDataArray):
        compare_vtkDataArray(vtk_expect, vtk_compare)


def compare_vtkDataArray(vtk_expect, vtk_compare):
    '''
    Compare if the two vtkDataArray object are equal
    :param vtk_expect: vtkDataArray
    :param vtk_compare: vtkDataArray
    '''
    list_errors = []

    if vtk_expect.GetName() != vtk_compare.GetName():
        list_errors.append('The name of the vtkDaraArray are different. Expected: {}, received: {}'.format(
                                                                vtk_expect.GetName(), vtk_compare.GetName()))
    if vtk_expect.GetDataType() != vtk_compare.GetDataType():
        list_errors.append('The data type of the vtkDataArray are different. Expected: {}, received: {}'.format(
                                _get_vtk_type(vtk_expect.GetDataType()), _get_vtk_type(vtk_compare.GetDataType())))

    if vtk_expect.GetNumberOfComponents() != vtk_compare.GetNumberOfComponents():
        list_errors.append('The number of components are different. Expected: {}, received: {}'.format(
                                            vtk_expect.GetNumberOfComponents(), vtk_compare.GetNumberOfComponents()))

    if vtk_expect.GetNumberOfTuples() != vtk_compare.GetNumberOfTuples():
        list_errors.append('The number of tuples are different. Expected: {}, received: {}'.format(
                                                    vtk_expect.GetNumberOfTuples(), vtk_compare.GetNumberOfTuples()))

    if isinstance(vtk_compare, vtk.vtkSignedCharArray):
        # vtkSignedCharArray does not support the conversion to numpy
        pass
    else:
        np_expect = ns.vtk_to_numpy(vtk_expect)
        np_compare = ns.vtk_to_numpy(vtk_compare)

        try:
            nt.assert_array_equal(np_expect, np_compare)
        except AssertionError as msg:
            list_errors.append('The vtkDataArray received are not equal.\n{}'.format(msg.message))

    if list_errors:
        pytest.fail('\n\n'.join(list_errors))


def _get_vtk_type(value):
    '''
    Receives a integer value and return a string with the vtk type of that value
    :param value:
    :return:
    '''

    types = {
             0 : 'VTK_VOID',
             1 : 'VTK_BIT',
             2 : 'VTK_CHAR',
             3: 'VTK_UNSIGNED_CHAR',
             4: 'VTK_SHORT',
             5: 'VTK_UNSIGNED_SHORT',
             6: 'VTK_INT',
             7: 'VTK_UNSIGNED_INT',
             8: 'VTK_LONG',
             9: 'VTK_UNSIGNED_LONG',
             10: 'VTK_FLOAT',
             11: 'VTK_DOUBLE',
             12: 'VTK_ID_TYPE',
             13: 'VTK_STRING',
             14: 'VTK_OPAQUE',
             15: 'VTK_SIGNED_CHAR',
             16: 'VTK_LONG_LONG',
             17: 'VTK_UNSIGNED_LONG_LONG',
             18: 'VTK__INT64',
             19: 'VTK_UNSIGNED__INT64',
             20: 'VTK_VARIANT',
             21: 'VTK_OBJECT',
             22: 'VTK_UNICODE_STRING',
         }

    if value in types:
        return types[value]
    else:
        raise ValueError('The type data received is not valid. Value: {}'.format())


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

