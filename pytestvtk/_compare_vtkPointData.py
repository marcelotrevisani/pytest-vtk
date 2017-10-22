from pytestvtk.base_array._compare_vtkAbstractArray import _compare_vtkAbstractArray
from pytestvtk.base_array._compare_vtkDataArray import _compare_vtkDataArray


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