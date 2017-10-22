import vtk
from numpy import testing as nt
from vtk.util import numpy_support as ns


def _compare_vtkDataArray(vtk_expect, vtk_compare):
    '''
    Compare if the two vtkDataArray object are equal
    :param vtk_expect: vtkDataArray
    :param vtk_compare: vtkDataArray
    :return string list: Return a list regarding the errors found
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
    elif isinstance(vtk_compare, vtk.vtkBitArray):
        # vtkBitArray does not support the conversion to numpy
        pass
    else:
        np_expect = ns.vtk_to_numpy(vtk_expect)
        np_compare = ns.vtk_to_numpy(vtk_compare)

        try:
            nt.assert_array_equal(np_expect, np_compare)
        except AssertionError as msg:
            list_errors.append('The vtkDataArray received are not equal.\n{}'.format(msg.message))
    return list_errors


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
             3 : 'VTK_UNSIGNED_CHAR',
             4 : 'VTK_SHORT',
             5 : 'VTK_UNSIGNED_SHORT',
             6 : 'VTK_INT',
             7 : 'VTK_UNSIGNED_INT',
             8 : 'VTK_LONG',
             9 : 'VTK_UNSIGNED_LONG',
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