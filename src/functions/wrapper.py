import sympy as sp
import functions.ana as ana

# ANA WRAPPER
def _call_solve_integral(expr, integrand, a, b):
    return ana.solve_integral(sp.sympify(expr), sp.Symbol(integrand), sp.sympify(a), sp.sympify(b))

def _call_solve_derivative(expr, variable):
    return ana.solve_derivative(sp.sympify(expr), sp.Symbol(variable))

def _call_solve_limit(expr, variable, point):
    return ana.solve_limit(sp.sympify(expr), sp.Symbol(variable), sp.sympify(point))
