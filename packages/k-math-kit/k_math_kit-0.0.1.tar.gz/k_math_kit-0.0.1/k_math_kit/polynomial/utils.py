import numpy as np

from math import pi, cos
from typing import List


def tchebychev_points(a: float, b: float, n: int) -> List[float]:
    """
    Calculates the n Chebyshev points within the interval [a, b].

    The Chebyshev points are defined as the roots of the n-th degree Chebyshev polynomial of the first kind.
    These points are particularly well-suited for numerical analysis and interpolation.

    Args:
        a (float): The lower bound of the interval.
        b (float): The upper bound of the interval.
        n (int): The number of Chebyshev points to calculate.

    Returns:
        List[float]: A list of length n containing the Chebyshev points.
    """
    # Calculate the interval length
    interval_length = b - a

    # Calculate the Chebychev points
    chebyshev_points = [(a + b)/2 - (interval_length/2) * np.cos(pi*(2*i+1)/(2*n)) for i in range(n)]

    return chebyshev_points


def number_wrapper(x: float, nb_dec_digits: int = 3) -> str:
    """
    Wraps a number x in parentheses if it is negative, otherwise returns the string representation of x.

    Args:
        x (float): The number to wrap.
        nb_dec_digits (int, optional): The number of decimal digits to round x to. Defaults to 3.

    Returns:
        str: The wrapped or string representation of x.
    """
    # Round the number to the specified number of decimal digits
    x = round(x, nb_dec_digits)

    # Check if the number is zero
    if x == 0:
        return ""

    # Check if the number is positive
    if x > 0:
        return str(x)

    # Return the wrapped number
    return f"({x})"
