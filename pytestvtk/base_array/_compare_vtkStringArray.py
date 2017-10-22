from pytestvtk.base_array._compare_vtkAbstractArray import _compare_vtkAbstractArray


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