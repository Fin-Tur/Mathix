import sympy as sp

def solve_integral(expr, integrand, a, b):
    return sp.integrate(expr, (integrand, a, b))


def solve_derivative(expr, variable):
    return sp.diff(expr, variable)

x, y, z, w = sp.symbols('x y z w')
