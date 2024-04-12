#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def numpy_matrix_multiply(matrix_a, matrix_b):
    """Return the result of multiplying two matrices using NumPy.
    Args:
        matrix_a (list of lists of ints/floats): The first matrix.
        matrix_b (list of lists of ints/floats): The second matrix.
    Returns:
        numpy.ndarray: The result of the matrix multiplication.
    """
    return np.matmul(matrix_a, matrix_b)
