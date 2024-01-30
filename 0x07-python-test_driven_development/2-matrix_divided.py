#!/usr/bin/python3
"""Definition of matrix fnctn"""


def matrix_divided(matrix, div):
    """quotient of matrix

    Args:
        matrix (list): list of lists; integers/float values
        div (int/float): The divisor.
    Raises:
        TypeError: for matrix of non-numbers.
        TypeError: for matrix of rows of diffrnt sizes.
        TypeError: for quotient not int/float.
        ZeroDivisionError: quotient 0.
    Returns:
        New matrix representing == div represnttn
    """
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all((isinstance(ele, int) or isinstance(ele, float))
                for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
