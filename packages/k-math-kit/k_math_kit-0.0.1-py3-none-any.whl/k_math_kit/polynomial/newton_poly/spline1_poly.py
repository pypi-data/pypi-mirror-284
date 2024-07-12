from typing import List
import numpy as np
from .newton_interpol_poly import NewtonInterpolPoly

class Spline1Poly:
    """
    Class representing a 1-st order spline polynomial.
    """

    def __init__(self, x: np.ndarray, y: np.ndarray, name: str = 'P') -> None:
        """
        Initializes a 1-st order spline polynomial.

        Args:
            x (numpy.ndarray): The array of x values.
            y (numpy.ndarray): The array of y values.
            name (str, optional): The name of the polynomial. Defaults to 'P'.
        """
        self.x = np.array(x, dtype=float)
        self.y = np.array(y, dtype=float)
        self.name = name
        self.polynomials: List[NewtonInterpolPoly] = [
            NewtonInterpolPoly(self.x[i:i+2], self.y[i:i+2], "")
            for i in range(len(self.x)-1)
        ]

    def horner_eval(self, x0: float) -> float:
        """
        Evaluates the 1-st order spline polynomial at a given point.

        Args:
            x0 (float): The point where the polynomial is evaluated.

        Returns:
            float: The value of the polynomial at x0.

        Raises:
            ValueError: If x0 is before the range of the x values.
        """
        before_x0 = 0
        for i in range(1, len(self.polynomials)):
            if self.x[i] > self.x[before_x0] and x0 >= self.x[i]:
                before_x0 = i
        if before_x0 == 0 and self.x[0] > x0:
            raise ValueError(f"!{x0} est avant la plage des abscisses!")
        return self.polynomials[before_x0].horner_eval(x0)
    
    def plot(self, ax, label: str = "Spline linear Interpolation of f") -> None:
        """
        Plots the 1-st order spline polynomial.

        Args:
            ax (matplotlib.axes.Axes): The axes to plot on.
            label (str, optional): The label for the plot. Defaults to
                "Spline linear Interpolation of f".
        """
        ax.plot(self.x, self.y, label=label)
        ax.legend()
        
    def __str__(self) -> str:
        """
        Returns a string representation of the 1-st order spline polynomial.

        Returns:
            str: The string representation of the polynomial.
        """
        string = (self.name + "(x) =")
        for i, poly in enumerate(self.polynomials):
            string += "\t" + str(poly)[5:] + f"   if x in [{self.x[i]}, {self.x[i+1]}]\n"
            
        return string


