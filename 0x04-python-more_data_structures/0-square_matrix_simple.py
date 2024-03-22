def square_matrix_simple(matrix=[]):
    new_matrix = [[c ** 2 for c in row] for row in matrix]
    return new_matrix
