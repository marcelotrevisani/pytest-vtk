from pytestvtk.base_array._compare_vtkDataArray import _compare_vtkDataArray


def _compare_vtkCellArray(vtk_expect, vtk_compare):
    '''
    Compare if these two vtkCellArray objects received as a parameter are equal
    :param vtk_expect:
    :param vtk_compare:
    :return: Error list
    '''
    list_errors = []

    if vtk_expect.GetNumberOfCells() != vtk_compare.GetNumberOfCells():
        list_errors.append(
            'The number of cells are different. Expected: {}, received: {}'.format(vtk_expect.GetNumberOfCells(),
                                                                                   vtk_compare.GetNumberOfCells()))

    if vtk_expect.GetSize() != vtk_compare.GetSize():
        list_errors.append(
            'The size of vtkCellArray are different. Expected: {}, received: {}'.format(vtk_expect.GetSize(),
                                                                                        vtk_compare.GetSize()))
    if vtk_expect.GetNumberOfConnectivityEntries() != vtk_compare.GetNumberOfConnectivityEntries():
        list_errors.append('The number of connectivity entries are different. Expected: {}, received: {}'.format(
            vtk_expect.GetNumberOfConnectivityEntries(), vtk_compare.GetNumberOfConnectivityEntries()))

    if vtk_expect.GetTraversalLocation() != vtk_compare.GetTraversalLocation():
        list_errors.append('The current traversal location are different. Expected: {}, received: {}'.format(
            vtk_expect.GetTraversalLocation(), vtk_compare.GetTraversalLocation()))

    if vtk_expect.GetMaxCellSize() != vtk_compare.GetMaxCellSize():
        list_errors.append(
            'The size of the largest cell are different. Expected: {}, received: {}'.format(vtk_expect.GetMaxCellSize(),
                                                                                            vtk_compare.GetMaxCellSize()))
    aux_error = _compare_vtkDataArray(vtk_expect.GetData(), vtk_compare.GetData())
    if aux_error:
        list_errors.append('The array of vtkCellArray are different.\n')
        list_errors = list_errors + aux_error

    return list_errors
