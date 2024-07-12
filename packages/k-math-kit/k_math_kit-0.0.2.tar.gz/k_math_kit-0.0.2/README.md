# 📐 k_math_kit 📚

Welcome to **k_math_kit**! This toolkit is designed to make advanced mathematical computations and polynomial manipulations easier for you. Whether you are a student, educator, or professional, this library will save you time and effort in performing complex mathematical operations. Created by KpihX.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Examples](#examples)
5. [Contributing](#contributing)
6. [License](#license)

## Features 🎉

- **Polynomial Operations**: Perform operations like addition, subtraction, and multiplication of polynomials.
- **Interpolation**: Implement Newton and Lagrange interpolation methods.
- **Integration**: Perform numerical integration using different techniques.
- **Spline Interpolation**: Generate and work with spline interpolations.
- **Taylor Series**: Compute and manipulate Taylor polynomials.

## Installation 🛠️

To get started with `k_math_kit`, you need to have Python installed on your system. You can then install the package via pip:

```sh
pip install k_math_kit
```

### Examples 🌟

#### I. Lagrange Interpolations of a given analytic function

##### 0. Definitions of Plotting parameters

```python
import numpy as np

a, b, n_plot = -2, 2, 1000
x_plot = np.linspace(a, b, n_plot)
# print("x_plot =", x_plot)
```

##### 1. Definition of f

```python
from utils import *
from math import exp

# f_exp = "cos(x)" # "1/(1+x**2)"
# def f(x):
    # return eval(f_exp, {"x": x})

f = lambda x: 1/(1+x**2)
# f = lambda x: 1/(1+exp(-x**2))

fig, ax = set_fig()
plot_f(ax, f, x_plot)
```

![png](./readme_images/output_4_0.png)

##### 2. Definition of Interpolation parameters

```python
from k_math_kit.polynomial.utils import *

n = 10

# Defintion of Uniforms points
x_uniform = np.linspace(a, b, n)
y_uniform = [f(x) for x in x_uniform]
print("Uniforms points")
print("x_uniform =", x_uniform)
print("\ny_uniform =", y_uniform)

#Definition of Tchebychev points
x_tchebychev = tchebychev_points(a, b, n)
y_tchebychev = [f(x) for x in x_tchebychev]
print("\nTchebychev points")
print("x_tchebychev =", x_tchebychev)
print("\ny_tchebychev =", y_tchebychev)
```

    Uniforms points
    x_uniform = [-2.         -1.55555556 -1.11111111 -0.66666667 -0.22222222  0.22222222
      0.66666667  1.11111111  1.55555556  2.        ]

    y_uniform = [0.2, 0.2924187725631769, 0.4475138121546961, 0.6923076923076922, 0.9529411764705883, 0.9529411764705883, 0.6923076923076924, 0.44751381215469627, 0.29241877256317694, 0.2]

    Tchebychev points
    x_tchebychev = [-1.9753766811902755, -1.7820130483767358, -1.4142135623730951, -0.9079809994790936, -0.31286893008046185, 0.3128689300804612, 0.9079809994790934, 1.414213562373095, 1.7820130483767356, 1.9753766811902753]

    y_tchebychev = [0.20399366423250215, 0.2394882325425853, 0.33333333333333326, 0.5481165495915764, 0.91084057802358, 0.9108405780235803, 0.5481165495915765, 0.33333333333333337, 0.23948823254258536, 0.20399366423250218]

##### 3. Test of Newton Lagrange Polynomial Representation

```python
from k_math_kit.polynomial.newton_poly import *

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print("x =", x)
print("y =", y)
polynomial = NewtonInterpolPoly(x, y)
print(polynomial)

x = 11
value = polynomial.horner_eval(x)
print(f"P{x}) = {value}")
```

    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    P(x) = 1.0 + 3.0 * (x - 1.0) + 1.0 * (x - 1.0)(x - 2.0)
    P11) = 121.0

##### 4. Uniform Lagrange Interpolation of f

```python
uni_lagrange_poly = NewtonInterpolPoly(x_uniform, y_uniform, "Uni_lagrange_poly")

print(uni_lagrange_poly)

x0 = 1
print(f"\nUni_lagrange_poly({x0}) =", uni_lagrange_poly.horner_eval(x0))

# print("\nx_uniform =", x_uniform)
# print("\ny_uniform =", y_uniform)

fig, ax = set_fig()
plot_f(ax, f, x_plot)
uni_lagrange_poly.plot(ax, x_plot, "Uniform Lagrange Interpolation of f")
```

    Uni_lagrange_poly(x) = 0.2 + 0.20794223827 * (x + 2.0) + 0.15864930092 * (x + 2.0)(x + 1.55555555556) + 0.05130066694 * (x + 2.0)(x + 1.55555555556)(x + 1.11111111111) + (-0.10772876887) * (x + 2.0)(x + 1.55555555556)(x + 1.11111111111)(x + 0.66666666667) + (-0.04888651791) * (x + 2.0)(x + 1.55555555556)(x + 1.11111111111)(x + 0.66666666667)(x + 0.22222222222) + 0.1046654664 * (x + 2.0)(x + 1.55555555556)(x + 1.11111111111)(x + 0.66666666667)(x + 0.22222222222)(x - 0.22222222222) + (-0.06139237133) * (x + 2.0)(x + 1.55555555556)(x + 1.11111111111)(x + 0.66666666667)(x + 0.22222222222)(x - 0.22222222222)(x - 0.66666666667) + 0.01726660444 * (x + 2.0)(x + 1.55555555556)(x + 1.11111111111)(x + 0.66666666667)(x + 0.22222222222)(x - 0.22222222222)(x - 0.66666666667)(x - 1.11111111111)

    Uni_lagrange_poly(1) = 0.49544474384530285

![png](./readme_images/output_10_1.png)

##### 5. Tchebychev Lagrange Interpolation of f

```python
tchebychev_lagrange_poly = NewtonInterpolPoly(x_tchebychev, y_tchebychev, "Tchebychev_lagrange_poly")

print(tchebychev_lagrange_poly)

x0 = 1
print(f"\nTchebychev_lagrange_poly({x0}) =", tchebychev_lagrange_poly.horner_eval(x0))

# print("\nx_tchebychev =", x_tchebychev)
# print("\ny_tchebychev =", y_tchebychev)

fig, ax = set_fig()
plot_f(ax, f, x_plot)

uni_lagrange_poly.plot(ax, x_plot, "Uniform Lagrange Interpolation of f")
tchebychev_lagrange_poly.plot(ax, x_plot, "Tchebychev Lagrange Interpolation of f")
```

    Tchebychev_lagrange_poly(x) = 0.20399366423 + 0.18356382632 * (x + 1.97537668119) + 0.12757264074 * (x + 1.97537668119)(x + 1.78201304838) + 0.06176433046 * (x + 1.97537668119)(x + 1.78201304838)(x + 1.41421356237) + (-0.04751642364) * (x + 1.97537668119)(x + 1.78201304838)(x + 1.41421356237)(x + 0.90798099948) + (-0.05625745845) * (x + 1.97537668119)(x + 1.78201304838)(x + 1.41421356237)(x + 0.90798099948)(x + 0.31286893008) + 0.063690232 * (x + 1.97537668119)(x + 1.78201304838)(x + 1.41421356237)(x + 0.90798099948)(x + 0.31286893008)(x - 0.31286893008) + (-0.03054788398) * (x + 1.97537668119)(x + 1.78201304838)(x + 1.41421356237)(x + 0.90798099948)(x + 0.31286893008)(x - 0.31286893008)(x - 0.90798099948) + 0.0081300813 * (x + 1.97537668119)(x + 1.78201304838)(x + 1.41421356237)(x + 0.90798099948)(x + 0.31286893008)(x - 0.31286893008)(x - 0.90798099948)(x - 1.41421356237)

    Tchebychev_lagrange_poly(1) = 0.4959349593495941

![png](./readme_images/output_12_1.png)

##### 6. Test of Gauss Integration

```python
from k_math_kit.integration import *

f_ = lambda x: x**2
start, end = -2, 5
gaus_int_f_ = gauss_integration(f_, -2, 5)
print(f"Gauss Integration of f_ from {start} to {end} =", gaus_int_f_)
```

    Gauss Integration of f_ from -2 to 5 = 44.33333333333334

##### 7. Errors of Lagrange Interpolations of f

```python
func_err_uniform = lambda x: (f(x) - uni_lagrange_poly.horner_eval(x))**2
func_err_tchebychev = lambda x: (f(x) - tchebychev_lagrange_poly.horner_eval(x))**2
err_uniform = sqrt(gauss_integration(func_err_uniform, a, b))
err_tchebychev = sqrt(gauss_integration(func_err_tchebychev, a, b))
print("err_uniform =", err_uniform)
print("err_tchebychev =", err_tchebychev)

fig, ax = set_fig()

plot_f(ax, f, x_plot)
uni_lagrange_poly.plot(ax, x_plot, "Uniform Lagrange Interpolation of f")
tchebychev_lagrange_poly.plot(ax, x_plot, "Tchebychev Lagrange Interpolation of f")

y_uni_plot = [func_err_uniform(x) for x  in x_plot]
ax.plot(x_plot, y_uni_plot, label="Error of Uniform Lagrange Interpolation of f")

y_tche_plot = [func_err_tchebychev(x) for x  in x_plot]
ax.plot(x_plot, y_tche_plot, label="Error of Tchebychev Lagrange Interpolation of f")

ax.legend()

```

    err_uniform = 0.044120898850020976
    err_tchebychev = 0.008834019736683135

    <matplotlib.legend.Legend at 0x780c4001dad0>

![png](./readme_images/output_14_2.png)


### Spline Interpolations of a given analytic function

#### 0. Definitions of Plotting parameters

```python
import numpy as np

a, b, n_plot = -1, 1, 1000
x_plot = np.linspace(a, b, n_plot)
# print("x_plot =", x_plot)
```

#### 1. Definition of f

```python
from utils import *

# f_exp = "cos(x)" # "1/(1+x**2)"
# def f(x):
    # return eval(f_exp, {"x": x})

f = lambda x: 1/(2+x**3)

fig, ax = set_fig()
plot_f(ax, f, x_plot)
```

![png](./readme_images/output_4_0_2.png)

#### 2. Definition of Interpolation parameters

```python
n = 10

# Defintion of Uniforms points
x_uniform = np.linspace(a, b, n)
y_uniform = [f(x) for x in x_uniform]
print("Uniforms points")
print("x_uniform =", x_uniform)
print("\ny_uniform =", y_uniform)
```

    Uniforms points
    x_uniform = [-1.         -0.77777778 -0.55555556 -0.33333333 -0.11111111  0.11111111
      0.33333333  0.55555556  0.77777778  1.        ]

    y_uniform = [1.0, 0.6538116591928251, 0.5468867216804201, 0.5094339622641509, 0.5003431708991077, 0.49965729952021937, 0.49090909090909085, 0.46051800379027164, 0.40477512493059414, 0.3333333333333333]

#### 3. Test of Linear Spline Interpolation

```python
from k_math_kit.polynomial.newton_poly import  Spline1Poly

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print("x =", x)
print("y =", y)
polynomial = Spline1Poly(x, y)
print(polynomial)

x = 1.5
value = polynomial.horner_eval(x)
print(f"P({x}) = {value}")
```

    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    P(x) =	 1.0 + 3.0 * (x - 1.0)   if x in [1.0, 2.0]
    	 4.0 + 5.0 * (x - 2.0)   if x in [2.0, 3.0]
    	 9.0 + 7.0 * (x - 3.0)   if x in [3.0, 4.0]
    	 16.0 + 9.0 * (x - 4.0)   if x in [4.0, 5.0]
    	 25.0 + 11.0 * (x - 5.0)   if x in [5.0, 6.0]
    	 36.0 + 13.0 * (x - 6.0)   if x in [6.0, 7.0]
    	 49.0 + 15.0 * (x - 7.0)   if x in [7.0, 8.0]
    	 64.0 + 17.0 * (x - 8.0)   if x in [8.0, 9.0]
    	 81.0 + 19.0 * (x - 9.0)   if x in [9.0, 10.0]

    P(1.5) = 2.5

#### 4. Uniform Linear Spline Interpolation of f

```python
uni_linear_spline_poly = Spline1Poly(x_uniform, y_uniform, "Uni_linear_spline_poly")

print(uni_linear_spline_poly)

x0 = 1
print(f"\nUni_linear_spline_poly({x0}) =", uni_linear_spline_poly.horner_eval(x0))

# print("\nx_uniform =", x_uniform)
# print("\ny_uniform =", y_uniform)

fig, ax = set_fig()
plot_f(ax, f, x_plot)

uni_linear_spline_poly.plot(ax, "Uniform Linear Spline Interpolation of f")
```

    Uni_linear_spline_poly(x) =	 1.0 + (-1.55784753363) * (x + 1.0)   if x in [-1.0, -0.7777777777777778]
    	 0.65381165919 + (-0.48116221881) * (x + 0.77777777778)   if x in [-0.7777777777777778, -0.5555555555555556]
    	 0.54688672168 + (-0.16853741737) * (x + 0.55555555556)   if x in [-0.5555555555555556, -0.33333333333333337]
    	 0.50943396226 + (-0.04090856114) * (x + 0.33333333333)   if x in [-0.33333333333333337, -0.11111111111111116]
    	 0.5003431709 + (-0.0030864212) * (x + 0.11111111111)   if x in [-0.11111111111111116, 0.11111111111111116]
    	 0.49965729952 + (-0.03936693875) * (x - 0.11111111111)   if x in [0.11111111111111116, 0.33333333333333326]
    	 0.49090909091 + (-0.13675989203) * (x - 0.33333333333)   if x in [0.33333333333333326, 0.5555555555555554]
    	 0.46051800379 + (-0.25084295487) * (x - 0.55555555556)   if x in [0.5555555555555554, 0.7777777777777777]
    	 0.40477512493 + (-0.32148806219) * (x - 0.77777777778)   if x in [0.7777777777777777, 1.0]

    Uni_linear_spline_poly(1) = 0.3333333333333333

![png](./readme_images/output_10_1_2.png)

#### 5. Uniform Cubic Spline Interpolation of f

```python
from k_math_kit.polynomial.taylor_poly import Spline3Polys
    
uni_spline3_poly = Spline3Polys(x_uniform, y_uniform, "Uni_spline3_poly")

print(uni_spline3_poly)

x0 = 1
print(f"\nUni_spline3_poly({x0}) =", uni_spline3_poly.horner_eval(x0))

fig, ax = set_fig()
plot_f(ax, f, x_plot)

# print("\nx_uniform =", x_uniform)
# print("\ny_uniform =", y_uniform)

uni_linear_spline_poly.plot(ax, "Uniform Linear Spline Interpolation of f")
uni_spline3_poly.plot(ax, n_plot, "Uniform Cubic Spline Interpolation of f")
```

    Uni_spline3_poly(x) =	 1.0 + (-1.826136) * (x + 1.0) + 5.432837 * (x + 1.0)^3   if x in [-1.0, -0.7777777777777778]
    	 0.653812 + (-1.021271) * (x + 0.777778) + 3.621892 * (x + 0.777778)^2 + (-5.361309) * (x + 0.777778)^3   if x in [-0.7777777777777778, -0.5555555555555556]
    	 0.546887 + (-0.205809) * (x + 0.555556) + 0.047686 * (x + 0.555556)^2 + 0.540173 * (x + 0.555556)^3   if x in [-0.5555555555555556, -0.33333333333333337]
    	 0.509434 + (-0.10459) * (x + 0.333333) + 0.407801 * (x + 0.333333)^2 + (-0.545553) * (x + 0.333333)^3   if x in [-0.33333333333333337, -0.11111111111111116]
    	 0.500343 + (-0.004168) * (x + 0.111111) + 0.044099 * (x + 0.111111)^2 + (-0.176549) * (x + 0.111111)^3   if x in [-0.11111111111111116, 0.11111111111111116]
    	 0.499657 + (-0.010723) * (x - 0.111111) + (-0.0736) * (x - 0.111111)^2 + (-0.248832) * (x - 0.111111)^3   if x in [0.11111111111111116, 0.33333333333333326]
    	 0.490909 + (-0.080298) * (x - 0.333333) + (-0.239488) * (x - 0.333333)^2 + (-0.065651) * (x - 0.333333)^3   if x in [0.33333333333333326, 0.5555555555555554]
    	 0.460518 + (-0.196463) * (x - 0.555556) + (-0.283255) * (x - 0.555556)^2 + 0.173462 * (x - 0.555556)^3   if x in [0.5555555555555554, 0.7777777777777777]
    	 0.404775 + (-0.296656) * (x - 0.777778) + (-0.167613) * (x - 0.777778)^2 + 0.25142 * (x - 0.777778)^3   if x in [0.7777777777777777, 1.0]

    Uni_spline3_poly(1) = 0.3333333333333333

![png](./readme_images/output_12_1_2.png)

#### 6. Errors of SPline Interpolations of f

```python
from k_math_kit.integration import gauss_integration

func_err_spline1 = lambda x: (f(x) - uni_linear_spline_poly.horner_eval(x))**2
func_err_spline3 = lambda x: (f(x) - uni_spline3_poly.horner_eval(x))**2
err_spline1 = sqrt(gauss_integration(func_err_spline1, a, b))
err_spline3 = sqrt(gauss_integration(func_err_spline3, a, b))
print("err_spline1 =", err_spline1)
print("err_spline3 =", err_spline3)

fig, ax = set_fig()

plot_f(ax, f, x_plot)
uni_linear_spline_poly.plot(ax, "Uniform Linear Spline Interpolation of f")
uni_spline3_poly.plot(ax, n_plot, "Uniform Cubic Spline Interpolation of f")

y_uni_plot = [func_err_spline1(x) for x  in x_plot]
ax.plot(x_plot, y_uni_plot, label="Error of Uniform Linear Spline Interpolation of f")

y_tche_plot = [func_err_spline3(x) for x  in x_plot]
ax.plot(x_plot, y_tche_plot, label="Error of Uniform Cubic Spline Interpolation of f")

ax.legend()

```

    err_spline1 = 0.0006928093124588687
    err_spline3 = 0.0005946540406200942

    <matplotlib.legend.Legend at 0x70aea7f31190>

![png](./readme_images/output_14_2_2.png)



For more dynamic tests, check out the `tests` directory, which contains Jupyter notebooks demonstrating various functionalities:

- `lagrange_interpolations.ipynb`
- `spline_interpolations.ipynb`

## Contributing 🤝

We welcome contributions to enhance the functionality of `k_math_kit`. If you have any ideas or improvements, please feel free to fork the repository and submit a pull request. For major changes, please open an issue to discuss what you would like to change.

### Steps to Contribute

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a pull request.

## License 📜

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---

Feel free to reach out if you have any questions or feedback. Happy computing! 😊

---

## Author

**KpihX**

---

**Enjoy using k_math_kit and happy computing!** 🧮✨
