from typing import Callable, Tuple, Union
import numpy as np
import matplotlib.pyplot as plt

from math import *

""" Objects """

real = int | float
Real = {int, float}

""" Functions """

def plot_f(ax: plt.Axes, f: Union[Callable[[real], real], str], x_plot: np.ndarray) -> None:
    """
    Plot the graph of a function f on the Axes ax.

    Args:
        ax (plt.Axes): The Axes object to plot the graph on.
        f (Union[Callable[[real], real], str]): The function to plot.
            Can be either a callable that takes a real number and returns a real number,
            or a string representing the function.
        x_plot (np.ndarray): The array of real numbers to plot the function at.

    Raises:
        ValueError: If the function is neither a callable nor a string.

    """
    if callable(f):
        # If the function is a callable, use the string representation of the function.
        f_str = "f"
    elif type(f) == str:
        # If the function is a string, parse it as a lambda function.
        f_exp = f
        f_str = "f(x) = " + f_exp
        f = lambda x: eval(f_exp.replace("x", str(x)))
    else:
        raise ValueError(f"!{f} must be either a function or a string!")
    
    # Evaluate the function at the given points and plot the graph.
    y_f = np.array([f(x) for x in x_plot])
    ax.plot(x_plot, y_f, label=f_str)
    ax.legend()



def set_fig(
    title: str = "Plotting of Interpolations of f",
    xlabel: str = "x",
    ylabel: str = "y"
) -> Tuple[plt.Figure, plt.Axes]:
    """
    Set up a figure and axes with the given title and labels.

    Args:
        title (str, optional): The title of the figure. Defaults to "Plotting of Interpolations of f".
        xlabel (str, optional): The label for the x-axis. Defaults to "x".
        ylabel (str, optional): The label for the y-axis. Defaults to "y".

    Returns:
        Tuple[plt.Figure, plt.Axes]: A tuple containing the figure and axes objects.
    """

    # Create a new figure and axes objects
    fig, ax = plt.subplots()

    # Set the title of the figure
    ax.set_title(title)

    # Set the x-axis label
    ax.set_xlabel(xlabel)

    # Set the y-axis label
    ax.set_ylabel(ylabel)

    # Return the figure and axes objects
    return fig, ax





