from matplotlib import pyplot as plt
import numpy as np

from ..utils import number_wrapper

class NewtonPolynomial:
    """
    Class representing a Newton polynomial.
    
    Attributes:
        coefficients (numpy.ndarray): The coefficients of the polynomial.
        x (numpy.ndarray): The points where the polynomial is defined.
        name (str): The name of the polynomial.
    """
    def __init__(self, coefficients: np.ndarray, x: np.ndarray, name: str = "P") -> None:
        """
        Initializes a Newton polynomial.

        Args:
            coefficients (numpy.ndarray): The coefficients of the polynomial.
            x (numpy.ndarray): The points where the polynomial is defined.
            name (str, optional): The name of the polynomial. Defaults to "P".
        """
        assert len(coefficients) == len(x) + 1, "The number of coefficients should be equal to the number of points + 1"
        self.coefficients = np.array(coefficients, dtype=float)
        self.x = np.array(x, dtype=float)
        self.name = name
        
    def horner_eval(self, x0: float) -> float:
        """
        Evaluates the Newton polynomial at a given point.

        Args:
            x0 (float): The point where the polynomial is evaluated.

        Returns:
            float: The value of the polynomial at x0.
        """
        n = len(self.coefficients)
        result = self.coefficients[-1]
        for i in range(n - 2, -1, -1):
            result = result * (x0 - self.x[i]) + self.coefficients[i]
        return result
    
    def plot(self, ax: plt.Axes, x_plot: np.ndarray, label: str = "P") -> None:
        """
        Plots the Newton polynomial.

        Args:
            ax (matplotlib.pyplot.Axes): The axes where the plot will be drawn.
            x_plot (numpy.ndarray): The points where the polynomial will be evaluated.
            label (str, optional): The label of the plot. Defaults to "P".
        """
        y_plot = self.horner_eval(x_plot)
        ax.plot(x_plot, y_plot, label=label)
        ax.legend()
    
    def __str__(self, nb_dec_digits: int = 11) -> str:
        """
        Returns a string representation of the Newton polynomial.

        Args:
            nb_dec_digits (int, optional): The number of decimal digits to round the coefficients. Defaults to 6.

        Returns:
            str: The string representation of the polynomial.
        """
        # Get the first term
        first_term = round(self.coefficients[0], nb_dec_digits)
        terms = [f"{first_term}"] if first_term != 0 else []
        
        # Get the other terms
        term = ""
        for i in range(0, len(self.coefficients)-1):
            coef_str = number_wrapper(self.coefficients[i+1], nb_dec_digits)
            if coef_str == "":
                continue
            val = round(self.x[i], nb_dec_digits)
            term += f"(x - {val})" if val > 0 else f"(x + {-val})" if val < 0 else "x"
            terms.append(f"{coef_str} * " + term)
        
        # Return the polynomial
        return self.name + "(x) = " + " + ".join(terms)
