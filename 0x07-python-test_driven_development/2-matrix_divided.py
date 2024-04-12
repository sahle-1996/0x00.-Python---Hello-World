def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix
    Raise TypeError and ZeroDivisionError with messages
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    matrix_error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(matrix_error_msg)

    row_length = 0
    size_error_msg = "Each row of the matrix must have the same size"

    for row in matrix:
        if not row or not isinstance(row, list):
            raise TypeError(matrix_error_msg)

        if row_length != 0 and len(row) != row_length:
            raise TypeError(size_error_msg)

        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError(matrix_error_msg)

        row_length = len(row)

    result = [[round(num / div, 2) for num in row] for row in matrix]
    return result
