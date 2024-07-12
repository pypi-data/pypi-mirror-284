from .spline3_poly import *

class Spline3Polys:
    """
    A class for representing a set of cubic spline polynomials.

    Attributes:
        x (np.ndarray): The x coordinates of the control points.
        y (np.ndarray): The y coordinates of the control points.
        name (str): The name of the polynomial.
        polynomials (List[Spline3Poly]): The cubic spline polynomials.
    """
    def __init__(self, x: np.ndarray, y: np.ndarray, name: str = "P") -> None:
        """
        Initializes a Spline3Polys object.

        Parameters:
            x (np.ndarray): The x coordinates of the control points.
            y (np.ndarray): The y coordinates of the control points.
            name (str): The name of the polynomial.
        """
        n = len(x)
        assert n >= 2 and n == len(y), "x and y must have the same length"

        self.x = np.array(x, dtype=float)
        self.y = np.array(y, dtype=float)
        if n == 2:
            self.y2 = np.array([0, 0], dtype=float)
        else:
            self.y2 = np.concatenate([[0], self.y2_values(), [0]])
        self.name = name
        self.polynomials = [Spline3Poly(self.x[i], self.x[i+1], self.y[i], self.y[i+1], self.y2[i], self.y2[i+1], "") for i in range(n-1)]
    
    def y2_values(self) -> np.ndarray:
        """
        Calculates the second derivative values of the cubic spline.

        Returns:
            np.ndarray: The second derivative values.
        """
        n = len(self.x)-1
        assert n >= 2, "number of control points must be >= 2"
        h = [self.x[i+1] - self.x[i] for i in range(n)]
        lamda = [self.x[i+2] - self.x[i] for i in range(n-1)]
        beta = [(self.y[i+1]-self.y[i])/h[i] for i in range(n)]
        if n == 2:
            A = np.array([[2*lamda[0]]])
        else:
            A = np.array([[2*lamda[0], h[1]] + [0] * (n-3)] + [[0] * (i-1) + [h[i], 2*lamda[i], h[i+1]] + [0] * (n-i-3) for i in range(1, n-2)] + ([[0] * (n-3) + [h[n-2], 2*lamda[n-2]]] if n >= 3 else []))
        B = 6 * np.array([beta[i+1]-beta[i] for i in range(n-1)])
        return np.linalg.solve(A, B)
        
    def horner_eval(self, x0: float) -> float:
        """
        Evaluates the cubic spline polynomial at x0.

        Parameters:
            x0 (float): The value to evaluate the polynomial at.

        Returns:
            float: The value of the polynomial at x0.
        """
        before_x0 = 0
        for i in range(1, len(self.x)):
            if self.x[i] > self.x[before_x0] and x0 >= self.x[i]:
                before_x0 = i
                
        if before_x0 == len(self.x)-1:
            return self.y[-1]
            
        if before_x0 == 0 and self.x[0] > x0:
            raise ValueError(f"!{x0} est avant la plage des abscisses!")
        
        return self.polynomials[before_x0].horner_eval(x0)
    
    def plot(self, ax: plt.Axes, n_plot: int = 100, label: str = "P") -> None:
        """
        Plots the cubic spline polynomials using the given axes.

        Parameters:
            ax (plt.Axes): The axes to plot on.
            n_plot (int): The number of points to plot.
            label (str): The label for the plot.
        """
        x_plot = np.linspace(min(self.x), max(self.x), n_plot)
        y_plot = [self.horner_eval(x) for x in x_plot]
        ax.plot(x_plot, y_plot, label=label)
        ax.legend()
    
    def __str__(self) -> str:
        """
        Returns a string representation of the cubic spline polynomials.

        Returns:
            str: The string representation of the cubic spline polynomials.
        """
        string = (self.name + "(x) =")
        for i, poly in enumerate(self.polynomials):
            string += "\t" + str(poly)[5:] + f"   if x in [{self.x[i]}, {self.x[i+1]}]\n"
            
        return string
