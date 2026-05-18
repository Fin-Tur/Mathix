import sympy as sp
import functions.ana as ana

# ── Folgen & Grenzwerte ──────────────────────────────────────────────────────

def _call_solve_limit(expr, variable, point):
    return ana.solve_limit(sp.sympify(expr), sp.Symbol(variable), sp.sympify(point))

def _call_solve_limit_direction(expr, variable, point, direction):
    return ana.solve_limit_direction(sp.sympify(expr), sp.Symbol(variable), sp.sympify(point), direction)

def _call_check_convergence(expr, variable):
    return ana.check_convergence(sp.sympify(expr), sp.Symbol(variable))

def _call_solve_sequence_limit(expr, n):
    return ana.solve_sequence_limit(sp.sympify(expr), sp.Symbol(n))

# ── Stetigkeit ───────────────────────────────────────────────────────────────

def _call_check_continuity(expr, variable, point):
    return ana.check_continuity(sp.sympify(expr), sp.Symbol(variable), sp.sympify(point))

def _call_find_discontinuities(expr, variable):
    return ana.find_discontinuities(sp.sympify(expr), sp.Symbol(variable))

# ── Differentialrechnung ─────────────────────────────────────────────────────

def _call_solve_derivative(expr, variable):
    return ana.solve_derivative(sp.sympify(expr), sp.Symbol(variable))

def _call_solve_nth_derivative(expr, variable, n):
    return ana.solve_nth_derivative(sp.sympify(expr), sp.Symbol(variable), int(n))

def _call_solve_tangent_line(expr, variable, point):
    x = sp.Symbol(variable)
    return ana.solve_tangent_line(sp.sympify(expr), x, sp.sympify(point))

def _call_find_critical_points(expr, variable):
    return ana.find_critical_points(sp.sympify(expr), sp.Symbol(variable))

def _call_classify_critical_points(expr, variable):
    return ana.classify_critical_points(sp.sympify(expr), sp.Symbol(variable))

def _call_solve_implicit_derivative(expr, x, y):
    x_sym = sp.Symbol(x)
    y_sym = sp.Symbol(y)
    return ana.solve_implicit_derivative(sp.sympify(expr), x_sym, y_sym)

# ── Integralrechnung ─────────────────────────────────────────────────────────

def _call_solve_integral(expr, integrand, a, b):
    return ana.solve_integral(sp.sympify(expr), sp.Symbol(integrand), sp.sympify(a), sp.sympify(b))

def _call_solve_indefinite_integral(expr, variable):
    return ana.solve_indefinite_integral(sp.sympify(expr), sp.Symbol(variable))

def _call_solve_improper_integral(expr, variable, a, b):
    return ana.solve_improper_integral(sp.sympify(expr), sp.Symbol(variable), sp.sympify(a), sp.sympify(b))

def _call_solve_arc_length(expr, variable, a, b):
    return ana.solve_arc_length(sp.sympify(expr), sp.Symbol(variable), sp.sympify(a), sp.sympify(b))

def _call_solve_area_between(expr1, expr2, variable, a, b):
    v = sp.Symbol(variable)
    return ana.solve_area_between(sp.sympify(expr1), sp.sympify(expr2), v, sp.sympify(a), sp.sympify(b))

def _call_solve_volume_of_revolution(expr, variable, a, b, axis):
    return ana.solve_volume_of_revolution(sp.sympify(expr), sp.Symbol(variable), sp.sympify(a), sp.sympify(b), axis)

# ── Reihen ───────────────────────────────────────────────────────────────────

def _call_solve_taylor_series(expr, variable, point, n):
    return ana.solve_taylor_series(sp.sympify(expr), sp.Symbol(variable), sp.sympify(point), int(n))

def _call_solve_maclaurin_series(expr, variable, n):
    return ana.solve_maclaurin_series(sp.sympify(expr), sp.Symbol(variable), int(n))

def _call_check_series_convergence(expr, n):
    return ana.check_series_convergence(sp.sympify(expr), sp.Symbol(n))

