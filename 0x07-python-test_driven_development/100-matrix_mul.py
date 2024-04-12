#!/usr/bin/python3
'''Contains a get_matrix_size and a matrix_mul function for a TDD project.
'''


def get_matrix_sizes(matrix1, matrix2, name1, name2):
    '''Computes the size of a matrix and performs some
    matrix validation.
    Args:
        matrix (list): The matrix.
        name (str): The name of the matrix.
    Returns:
        list. The rows and columns of the given matrix.
    '''
    funcs = (
        lambda txt: '{} must be a list'.format(txt),
        lambda txt: '{} can\'t be empty'.format(txt),
        lambda txt: '{} must be a list of lists'.format(txt),
        lambda txt: '{} should contain only integers or floats'.format(txt),
        lambda txt: 'each row of {} must be of the same size'.format(txt),
        lambda l: all(map(lambda n: isinstance(n, (int, float)), l)),
    )
    size0 = [0, 0]
    size1 = [0, 0]
    if not isinstance(matrix1, list):
        raise TypeError(funcs[0](name1))
    if not isinstance(matrix2, list):
        raise TypeError(funcs[0](name2))
    size0[0] = len(matrix1)
    size1[0] = len(matrix2)
    if size0[0] == 0:
        raise ValueError(funcs[1](name1))
    if size1[0] == 0:
        raise ValueError(funcs[1](name2))
    if not all(map(lambda x: isinstance(x, list), matrix1)):
        raise TypeError(funcs[2](name1))
    if not all(map(lambda x: isinstance(x, list), matrix2)):
        raise TypeError(funcs[2](name2))
    if all(map(lambda x: len(x) == 0, matrix1)):
        raise ValueError(funcs[1](name1))
    if all(map(lambda x: len(x) == 0, matrix2)):
        raise ValueError(funcs[1](name2))
    if not all(map(lambda x: funcs[5](x), matrix1)):
        raise TypeError(funcs[3](name1))
    if not all(map(lambda x: funcs[5](x), matrix2)):
        raise TypeError(funcs[3](name2))
    size0[1] = len(matrix1[0])
    size1[1] = len(matrix2[0])
    if not all(map(lambda x: len(x) == size0[1], matrix1)):
        raise TypeError(funcs[4](name1))
    if not all(map(lambda x: len(x) == size1[1], matrix2)):
        raise TypeError(funcs[4](name2))
    return size0, size1


def matrix_mul(matrix_a, matrix_b):
    '''Multiplies 2 matrices.
    Args:
        matrix_a (list): The first matrix.
        matrix_b (list): The second matrix.
    Returns:
        list: A list of lists of the products of the two given matrices.
    Raises:
        ValueError: If matrix_a's column count isn't equal to matrix_b's row count.
    '''
    size_a, size_b = get_matrix_sizes(matrix_a, matrix_b, 'matrix_a', 'matrix_b')
    # AB only works iff column_count in A == row_count in B
    if size_a[1] != size_b[0]:
        raise ValueError('matrix_a and matrix_b can\'t be multiplied')
    else:
        result = []
        for row_a in matrix_a:
            row_result = []
            for i in range(size_b[1]):
                cell_args = zip(range(size_a[1]), row_a)
                val = map(lambda x: x[1] * matrix_b[x[0]][i], cell_args)
                row_result.append(sum(list(val)))
            result.append(row_result)
        return result
