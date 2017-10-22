import vtk


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