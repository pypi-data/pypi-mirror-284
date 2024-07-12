import numpy as np

from math import sqrt
from typing import Callable

def gauss_integration(
    f: Callable[[float], float],
    a: float = -1,
    b: float = 1,
) -> float:
    """
    Compute the integral of a function `f` between `a` and `b` using the
    Gauss-Legendre quadrature method.

    Parameters
    ----------
    f : Callable[[float], float]
        The function to integrate.
    a : float, optional
        The lower bound of the integration interval, by default -1.
    b : float, optional
        The upper bound of the integration interval, by default 1.

    Returns
    -------
    float
        The integral of `f` between `a` and `b`.
    """

    # Check if the integration interval is the unit interval
    if a == -1 and b == 1:
        # Compute the roots of the Legendre polynomial of degree 3
        x = sqrt(3/5)
        # Compute the integral using the Gauss-Legendre quadrature formula
        return (5*f(-x) + 8*f(0) + 5*f(x)) / 9

    # Compute the number of intervals
    n = int((b-a)/2)+1

    # Compute the intervals
    intervals = np.linspace(a, b, n)

    # Compute the width of each interval
    d = (intervals[1] - intervals[0])/2

    # Compute the integral using the Gauss-Legendre quadrature formula
    return sum([
        gauss_integration(lambda t: f((1+t)*d+intervals[k]), -1, 1)
        for k in range(n-1)
    ]) * d
