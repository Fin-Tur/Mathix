import sympy as sp

def solve_integral(expr, integrand, a, b):
    return sp.integrate(expr, (integrand, a, b))

def solve_derivative(expr, variable):
    return sp.diff(expr, variable)

def solve_limit(expr, variable, point):
    return sp.limit(expr, variable, point) 
