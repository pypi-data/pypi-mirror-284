from .newton_poly import *

class NewtonInterpolPoly(NewtonPolynomial):
    """
    A class representing a Newton Interpolation Polynomial.

    This class inherits from NewtonPolynomial and overrides the __init__ method.
    It also defines the newton_interpol_coefs and plot methods.

    Attributes:
        x (numpy.ndarray): The array of x values.
        y (numpy.ndarray): The array of y values.
        name (str): The name of the polynomial.
    """

    def __init__(self, x: np.ndarray, y: np.ndarray, name: str = 'P') -> None:
        """
        Initializes a Newton Interpolation Polynomial.

        Args:
            x (numpy.ndarray): The array of x values.
            y (numpy.ndarray): The array of y values.
            name (str, optional): The name of the polynomial. Defaults to 'P'.
        """
        self.x = np.array(x, dtype=float)
        self.y = np.array(y, dtype=float)
        super().__init__(self.newton_interpol_coefs(), x[:-1], name)

    def newton_interpol_coefs(self) -> np.ndarray:
        """
        Computes the coefficients of the Newton Interpolation Polynomial.

        Returns:
            numpy.ndarray: The coefficients of the polynomial.
        """
        n = len(self.x)
        coefficients = self.y.copy()
        step = 1
        for j in range(1, n):
            coefficients[j:n] = (coefficients[j:n] - coefficients[j-1:n-1]) / (self.x[j:n] - self.x[j-step:n-step])
            step += 1
        return coefficients

    def plot(self, ax: plt.Axes, x_plot: np.ndarray, label: str = "Lagrange Interpolation of f") -> None:
        """
        Plots the Newton Interpolation Polynomial.

        Args:
            ax (matplotlib.pyplot.Axes): The axes where the plot will be drawn.
            x_plot (numpy.ndarray): The points where the polynomial will be evaluated.
            label (str, optional): The label of the plot. Defaults to "Lagrange Interpolation of f".
        """
        super().plot(ax, x_plot, label)
