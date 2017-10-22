from pytestvtk.base_array._compare_vtkDataArray import _compare_vtkDataArray


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