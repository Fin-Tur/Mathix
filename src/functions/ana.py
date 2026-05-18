import sympy as sp
from sympy.calculus.util import singularities

# ── Series and Limits ──────────────────────────────────────────────────────

def solve_limit(expr: sp.Expr, variable: sp.Symbol, point) -> sp.Expr:
    return sp.limit(expr, variable, point)

def solve_limit_direction(expr: sp.Expr, variable: sp.Symbol, point, direction: str) -> sp.Expr:
    return sp.limit(expr, variable, point, dir=direction)

def check_convergence(expr: sp.Expr, variable: sp.Symbol) -> dict:
    from sympy.calculus.accumulationbounds import AccumulationBounds
    try:
        lim = sp.limit(expr, variable, sp.oo)
    except (NotImplementedError, ValueError):
        return {"converges": False, "limit": "undetermined (oscillating or sympy cannot resolve)"}
    if isinstance(lim, AccumulationBounds):
        return {"converges": False, "limit": str(lim)}
    converges = bool(lim.is_finite) and lim is not sp.nan
    return {"converges": converges, "limit": lim}

def solve_sequence_limit(expr: sp.Expr, n: sp.Symbol) -> sp.Expr:
    try:
        return sp.limit(expr, n, sp.oo)
    except (NotImplementedError, ValueError) as e:
        return f"undetermined: {e}"

# ── Continuity ───────────────────────────────────────────────────────────────

def check_continuity(expr: sp.Expr, variable: sp.Symbol, point) -> bool:
    try:
        lim_left  = sp.limit(expr, variable, point, dir='-')
        lim_right = sp.limit(expr, variable, point, dir='+')
        val = expr.subs(variable, point)
        return bool(lim_left == lim_right == val)
    except Exception:
        return False

def find_discontinuities(expr: sp.Expr, variable: sp.Symbol) -> list:
    try:
        return singularities(expr, variable)
    except Exception:
        denom_expr = sp.fraction(sp.cancel(expr))[1]
        return sp.solve(denom_expr, variable)

# ── Differential Calculus ─────────────────────────────────────────────────────

def solve_derivative(expr: sp.Expr, variable: sp.Symbol) -> sp.Expr:
    return sp.diff(expr, variable)

def solve_nth_derivative(expr: sp.Expr, variable: sp.Symbol, n: int) -> sp.Expr:
    return sp.diff(expr, variable, n)

def solve_tangent_line(expr: sp.Expr, variable: sp.Symbol, point) -> sp.Expr:
    slope = sp.diff(expr, variable).subs(variable, point)
    y0    = expr.subs(variable, point)
    return slope * (variable - point) + y0

def find_critical_points(expr: sp.Expr, variable: sp.Symbol) -> list:
    return sp.solve(sp.diff(expr, variable), variable)

def classify_critical_points(expr: sp.Expr, variable: sp.Symbol) -> dict:
    deriv2 = sp.diff(expr, variable, 2)
    result = {}
    for cp in sp.solve(sp.diff(expr, variable), variable):
        val = deriv2.subs(variable, cp)
        if val.is_positive:
            result[cp] = "minimum"
        elif val.is_negative:
            result[cp] = "maximum"
        else:
            result[cp] = "inconclusive (saddle/inflection)"
    return result

def solve_implicit_derivative(expr: sp.Expr, x: sp.Symbol, y: sp.Symbol) -> sp.Expr:
    return sp.idiff(expr, y, x)

# ── Integral Calculus ─────────────────────────────────────────────────────────

def solve_integral(expr: sp.Expr, integrand: sp.Symbol, a, b) -> sp.Expr:
    return sp.integrate(expr, (integrand, a, b))

def solve_indefinite_integral(expr: sp.Expr, variable: sp.Symbol) -> sp.Expr:
    return sp.integrate(expr, variable)

def solve_improper_integral(expr: sp.Expr, variable: sp.Symbol, a, b) -> sp.Expr:
    return sp.integrate(expr, (variable, a, b))

def solve_arc_length(expr: sp.Expr, variable: sp.Symbol, a, b) -> sp.Expr:
    integrand = sp.sqrt(1 + sp.diff(expr, variable)**2)
    return sp.integrate(integrand, (variable, a, b))

def solve_area_between(expr1: sp.Expr, expr2: sp.Expr, variable: sp.Symbol, a, b) -> sp.Expr:
    return sp.integrate(sp.Abs(expr1 - expr2), (variable, a, b))

def solve_volume_of_revolution(expr: sp.Expr, variable: sp.Symbol, a, b, axis: str) -> sp.Expr:
    if axis == 'x':
        return sp.pi * sp.integrate(expr**2, (variable, a, b))
    elif axis == 'y':
        return 2 * sp.pi * sp.integrate(variable * expr, (variable, a, b))
    else:
        raise ValueError(f"axis must be 'x' or 'y', got '{axis}'")

# ── Series ───────────────────────────────────────────────────────────────────

def solve_taylor_series(expr: sp.Expr, variable: sp.Symbol, point, n: int) -> sp.Expr:
    return sp.series(expr, variable, point, n).removeO()

def solve_maclaurin_series(expr: sp.Expr, variable: sp.Symbol, n: int) -> sp.Expr:
    return sp.series(expr, variable, 0, n).removeO()

def check_series_convergence(expr: sp.Expr, n: sp.Symbol) -> dict:
    s = sp.Sum(expr, (n, 1, sp.oo))
    result = s.doit()
    converges = bool(result.is_finite and not result.has(sp.oo, sp.zoo, sp.nan))
    return {"converges": converges, "sum": result}
