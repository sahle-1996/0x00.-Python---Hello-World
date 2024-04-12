#!/usr/bin/python3
"""Divide a matrix."""

def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given divisor.
    
    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The divisor.
    
    Returns:
        list of lists: The resulting matrix after division.
    
    Raises:
        TypeError: If div is not a number or matrix is not a list of lists.
        ZeroDivisionError: If div is zero.
        TypeError: If elements of matrix are not integers or floats.
        TypeError: If rows of the matrix are not of the same size.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if any(not all(isinstance(num, (int, float)) for num in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    return [[round(num / div, 2) for num in row] for row in matrix]
