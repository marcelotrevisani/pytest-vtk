import numpy.testing as nt
import pytest
import vtk
from vtk.util import numpy_support as ns


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


def _compare_vtkPoints(vtk_expect, vtk_compare):
    '''
    Verify if the two vtkPoints are equal
    :param vtk_expect:
    :param vtk_compare:
    :return:
    '''
    list_errors = []
    aux_errors = _compare_vtkDataArray(vtk_expect.GetData(), vtk_compare.GetData())

    if aux_errors:
        list_errors.append('The arrray points of vtkPoints are different.\n')
        list_errors = list_errors + aux_errors

    if vtk_expect.GetNumberOfPoints() != vtk_compare.GetNumberOfPoints():
        list_errors.append('The number of points of the vtkPoints are different. Expected: {}, received: {}'.format(
                                                      vtk_expect.GetNumberOfPoints(), vtk_compare.GetNumberOfPoints()))
    vtk_expect.ComputeBounds()
    vtk_compare.ComputeBounds()
    if vtk_expect.GetBounds() != vtk_compare.GetBounds():
        list_errors.append('The bounds of the vtkPoints are different. Expected: {}, '
                           'received: {}'.format(vtk_expect.GetBounds(), vtk_compare.GetBounds()))
    return list_errors


def _compare_vtkPointData(vtk_expect, vtk_compare):
    '''
    Compare two vtkPointData objects
    :param vtk_expect:
    :param vtk_compare:
    :return:
    '''
    list_errors = []

    def _aux_add_error(array_exp, array_cmp, msg):
        if array_exp is None or array_cmp is None:
            return []
        aux_errors = _compare_vtkDataArray(array_exp, array_cmp)
        if aux_errors:
            aux_errors.insert(0, 'The {} array of vtkPointData are different.'.format(msg))
            return aux_errors
        else:
            return []

    # Scalars
    list_errors = list_errors + _aux_add_error(vtk_expect.GetScalars(), vtk_compare.GetScalars(), 'scalars')

    # Vectors
    list_errors = list_errors + _aux_add_error(vtk_expect.GetVectors(), vtk_compare.GetVectors(), 'vectors')

    # Texture Coordinates
    list_errors = list_errors + _aux_add_error(vtk_expect.GetTCoords(), vtk_compare.GetTCoords(), 'texture coordinate')

    # Tensors
    list_errors = list_errors + _aux_add_error(vtk_expect.GetTensors(), vtk_compare.GetTensors(), 'tensors')

    # Global Ids
    list_errors = list_errors + _aux_add_error(vtk_expect.GetGlobalIds(), vtk_compare.GetGlobalIds(), 'global ids')

    # Normals
    list_errors = list_errors + _aux_add_error(vtk_expect.GetNormals(), vtk_compare.GetNormals(), 'normals')

    if vtk_expect.GetNumberOfArrays() != vtk_compare.GetNumberOfArrays():
        list_errors.append('The number of arrays in each vtkPointData are different. Expected: {}, '
                           'received: {}'.format(vtk_expect.GetNumberOfArrays(), vtk_compare.GetNumberOfArrays()))
    else:
        for i in range(vtk_expect.GetNumberOfArrays()):
            aux_errors = _compare_vtkAbstractArray(vtk_expect.GetAbstractArray(i), vtk_compare.GetAbstractArray(i),
                                                                        'position array {} of vtkPointData'.format(i))
            if aux_errors:
                list_errors = list_errors + aux_errors

    if vtk_expect.GetNumberOfTuples() != vtk_compare.GetNumberOfTuples():
        list_errors.append('The number of tuples of the vtkPointData are different. Expected: {}, '
                           'received: {}'.format(vtk_expect.GetNumberOfTuples(), vtk_compare.GetNumberOfTuples()))

    if vtk_expect.GetNumberOfComponents() != vtk_compare.GetNumberOfComponents():
        list_errors.append('The number of components of the vtkPointData are different. Expected: {}, '
                            'received: {}'.format(vtk_expect.GetNumberOfComponents(), vtk_compare.GetNumberOfComponents()))
    return list_errors


def _compare_vtkStringArray(vtk_expect, vtk_compare):
    '''
    Verify if the two vtkStringArrays are equal
    :param vtk_expect:
    :param vtk_compare:
    :return:
    '''
    list_errors = []

    if vtk_expect.GetNumberOfComponents() != vtk_compare.GetNumberOfComponents():
        list_errors.append('The number of components of the vtkStringArray are different. Expected: {}, '
                            'received: {}'.format(vtk_expect.GetNumberOfComponents(), vtk_compare.GetNumberOfComponents()))


    if vtk_expect.GetDataSize() != vtk_compare.GetDataSize():
        list_errors.append('The data size of the vtkStringArray are different. Expected: {}, '
                            'received: {}'.format(vtk_expect.GetDataSize(), vtk_compare.GetDataSize()))

    aux_errors = _compare_vtkAbstractArray(vtk_expect, vtk_compare, 'vtkStringArray')
    if aux_errors:
        list_errors = list_errors + aux_errors

    return list_errors


def _compare_vtkAbstractArray(vtk_expect, vtk_compare, type):
    '''
    Verify if the basic attributes of the vtkAbstractArray are equal
    :param vtk_expect:
    :param vtk_compare:
    :param type: The vtk type object
    :return:
    '''
    list_errors = []

    if vtk_expect.GetNumberOfTuples() != vtk_compare.GetNumberOfTuples():
        list_errors.append('The number of tuples of the {} are different. Expected: {}, '
                            'received: {}'.format(type, vtk_expect.GetNumberOfTuples(), vtk_compare.GetNumberOfTuples()))

    if vtk.vtkVersion().GetVTKMajorVersion() > 7 or vtk.vtkVersion().GetVTKVersion() == '7.1.1' and \
       vtk_expect.GetNumberOfValues() != vtk_compare.GetNumberOfValues():
        list_errors.append('The number of values of the {} are different. Expected: {}, '
                            'received: {}'.format(type, vtk_expect.GetNumberOfValues(), vtk_compare.GetNumberOfValues()))

    if vtk_expect.GetSize() != vtk_compare.GetSize():
        list_errors.append('The size of the {} are different. Expected: {}, '
                            'received: {}'.format(type, vtk_expect.GetSize(), vtk_compare.GetSize()))

    if vtk_expect.GetMaxId() != vtk_compare.GetMaxId():
        list_errors.append('The maximum id of the {} are different. Expected: {}, '
                            'received: {}'.format(type, vtk_expect.GetMaxId(), vtk_compare.GetMaxId()))

    if vtk_expect.GetArrayType() != vtk_compare.GetArrayType():
        list_errors.append('The array type of the {} are different. Expected: {}, '
                            'received: {}'.format(type, vtk_expect.GetArrayType(), vtk_compare.GetArrayType()))

    if vtk_expect.GetName() != vtk_compare.GetName():
        list_errors.append('The array name of the {} are different. Expected: {}, '
                            'received: {}'.format(type, vtk_expect.GetName(), vtk_compare.GetName()))

    if vtk_expect.GetMaxDiscreteValues() != vtk_compare.GetMaxDiscreteValues():
        list_errors.append('The maximum discrete values of the {} are different. Expected: {}, '
                           'received: {}'.format(type, vtk_expect.GetMaxDiscreteValues(), vtk_compare.GetMaxDiscreteValues()))

    return list_errors

