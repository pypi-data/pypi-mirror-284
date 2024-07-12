from typing import List
import numpy as np
from .taylor_poly import *


class Spline3Poly(TaylorPolynomial):
    """
    Cubic spline polynomial class.

    This class extends the TaylorPolynomial class to represent a cubic spline
    polynomial. It represents a polynomial that can be used to interpolate a
    function between two points with known values and 2nd derivatives.

    Parameters
    ----------
    a : float
        The lower bound of the interval.
    b : float
        The upper bound of the interval.
    y_a : float
        The value of the function at the lower bound.
    y_b : float
        The value of the function at the upper bound.
    d_a : float
        The 2nd derivative of the function at the lower bound.
    d_b : float
        The 2nd derivative of the function at the upper bound.
    name : str, optional
        The name of the polynomial, by default "P".
    """

    def __init__(self, a: float, b: float, y_a: float, y_b: float,
                 d_a: float, d_b: float, name: str = "P"):
        self.a = a
        self.b = b
        self.y_a = y_a
        self.y_b = y_b
        self.d_a = d_a
        self.d_b = d_b
        self.name = name
        super().__init__(self.coefs(), a, name)
        self.coefficients = self.coefs()

    def coefs(self) -> List[float]:
        """
        Calculates the coefficients of the polynomial.

        Returns
        -------
        List[float]
            The coefficients of the polynomial.
        """
        h = self.b - self.a
        # The coefficients of the polynomial are calculated using the formula:
        # y(x) = y_a + (y_b - y_a)/h - (2*d_a + d_b)*h/6 + d_a/2*(h/3)**2 + (d_b - d_a)*(h/6)*(h/3)
        return [self.y_a, (self.y_b - self.y_a)/h - (2*self.d_a + self.d_b)*h/6,
                self.d_a/2, (self.d_b - self.d_a)/(6*h)]

    def plot(self, ax, x_plot: np.ndarray, label: str = "Spline Cubic Interpolation") -> None:
        """
        Plots the polynomial using the given axes.

        Parameters
        ----------
        ax : plt.Axes
            The axes to plot on.
        x_plot : np.ndarray
            The x coordinates to plot.
        label : str, optional
            The label for the plot, by default "Spline Cubic Interpolation".
        """
        super().plot(ax, x_plot, label)
