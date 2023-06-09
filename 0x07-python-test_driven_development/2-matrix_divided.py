#!/usr/bin/python3
"""devide elements of a matrix"""


def matrix_divided(matrix, div):
    """devides the elements of a matrix and returns a new matrix
        matrix: list of int or float
        div: nymber to devide by"""

    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list), for row in matrix) or
        not all(isinstance(num, int), or isinstance(num, float))
            for num in [elem for row in matrix for elem in row])):
        raise TypeError("matrix must be a matrix (list of lists) of
                        integers/floats")

    if not all(len(row) == len(matrix[0] for row i matrix):
        raise TypeError("each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
