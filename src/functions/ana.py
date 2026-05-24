import sympy as sp
from sympy.calculus.util import singularities
from sympy.calculus.accumulationbounds import AccumulationBounds

# ── Series and Limits ──────────────────────────────────────────────────────

def solve_limit(f: sp.Expr, variable: sp.Symbol, point) -> sp.Expr:
    return sp.limit(f, variable, point)

def solve_limit_direction(f: sp.Expr, variable: sp.Symbol, point, direction: str) -> sp.Expr:
    return sp.limit(f, variable, point, dir=direction)

def check_convergence(f: sp.Expr, variable: sp.Symbol) -> dict:
    try:
        lim = sp.limit(f, variable, sp.oo)
    except (NotImplementedError, ValueError):
        return {"converges": False, "limit": "undetermined (sympy cannot resolve)"}
    if isinstance(lim, AccumulationBounds):
        return {"converges": False, "limit": str(lim)}
    converges = bool(lim.is_finite) and lim is not sp.nan
    return {"converges": converges, "limit": lim}

def solve_sequence_limit(f: sp.Expr, n: sp.Symbol) -> sp.Expr:
    try:
        return sp.limit(f, n, sp.oo)
    except (NotImplementedError, ValueError) as e:
        return f"undetermined: {e}"

# ── Continuity ───────────────────────────────────────────────────────────────

def check_continuity(f: sp.Expr, variable: sp.Symbol, point) -> bool:
    try:
        lim_left  = sp.limit(f, variable, point, dir='-')
        lim_right = sp.limit(f, variable, point, dir='+')
        val = f.subs(variable, point)
        return bool(lim_left == lim_right == val)
    except Exception:
        return False

STEP_FUNCTIONS = (sp.floor, sp.ceiling, sp.Heaviside, sp.sign, sp.DiracDelta)

def find_discontinuities(f: sp.Expr, variable: sp.Symbol) -> set:
    result = set()
    try:
        result.update(singularities(f, variable))
    except Exception:
        denom_f = sp.fraction(sp.cancel(f))[1]
        result.update(sp.solve(denom_f, variable))

    if f.has(*STEP_FUNCTIONS):
        raise NotImplementedError(
            "Discontinuity of step function (floor, Heaviside, …) "
            "can't be determined automatically."
        )
    return result

# ── Differential Calculus ─────────────────────────────────────────────────────

def solve_derivative(f: sp.Expr, variable: sp.Symbol) -> sp.Expr:
    return sp.diff(f, variable)

def solve_nth_derivative(f: sp.Expr, variable: sp.Symbol, n: int) -> sp.Expr:
    return sp.diff(f, variable, n)

def solve_tangent_line(f: sp.Expr, variable: sp.Symbol, point) -> sp.Expr:
    slope = sp.diff(f, variable).subs(variable, point)
    if not slope.is_finite:
        raise ValueError(
            f"The function at x={point} is not differentiable (m: {slope})."
        )
    y0 = f.subs(variable, point)
    return slope * (variable - point) + y0

def find_critical_points(f: sp.Expr, variable: sp.Symbol) -> sp.Set:
    deriv = sp.diff(f, variable)
    return sp.solveset(deriv, variable, domain=sp.S.Reals)

def _classify_single_cp(f: sp.Expr, variable: sp.Symbol, cp: sp.Expr) -> str:
    for i in range(2, 8):
        fp_of_cp = sp.diff(f, variable, i).subs(variable, cp)
        if fp_of_cp == 0:
            continue
        determined = fp_of_cp.is_positive
        if determined is None:
            return f"inconclusive (f^({i}) not determinable symbolically)"
        if i % 2 == 1:
            return "saddle point"
        return "minimum" if determined else "maximum"
    return "inconclusive (all derivatives zero up to order 7)"


def classify_critical_points(f: sp.Expr, variable: sp.Symbol) -> dict:
    cps = sp.solveset(sp.diff(f, variable), variable, domain=sp.S.Reals)
    if not isinstance(cps, sp.FiniteSet):
        return {"all": f"infinite critical points: {cps}"}
    return {cp: _classify_single_cp(f, variable, cp) for cp in cps}

def solve_implicit_derivative(f: sp.Expr, x: sp.Symbol, y: sp.Symbol) -> sp.Expr:
    return sp.idiff(f, y, x)

# ── Integral Calculus ─────────────────────────────────────────────────────────

def solve_integral(f: sp.Expr, integrand: sp.Symbol, a, b) -> sp.Expr:
    return sp.integrate(f, (integrand, a, b))

def solve_indefinite_integral(f: sp.Expr, variable: sp.Symbol) -> sp.Expr:
    C = sp.Symbol('C')
    return sp.integrate(f, variable) + C

def solve_improper_integral(f: sp.Expr, variable: sp.Symbol, a, b) -> sp.Expr:
    result = sp.integrate(f, (variable, a, b))
    if result is sp.nan or result.has(sp.nan):
        raise ValueError("The improper integral diverges (or could not be evaluated).")
    if not result.is_finite:
        raise ValueError(f"The improper integral diverges: {result}")
    return result

def solve_arc_length(f: sp.Expr, variable: sp.Symbol, a, b) -> sp.Expr:
    integrand = sp.sqrt(1 + sp.diff(f, variable)**2)
    return sp.integrate(integrand, (variable, a, b))

def solve_area_between(f1: sp.Expr, f2: sp.Expr, variable: sp.Symbol, a, b) -> sp.Expr:
    diff = f1 - f2
    zeros = sp.solveset(diff, variable, domain=sp.Interval(a, b))
    if isinstance(zeros, sp.FiniteSet):
        breakpoints = sorted([a] + list(zeros) + [b], key=lambda z: sp.re(z))
    else:
        breakpoints = [a, b]

    total = sp.Integer(0)
    for i in range(len(breakpoints) - 1):
        piece = sp.integrate(diff, (variable, breakpoints[i], breakpoints[i + 1]))
        total += sp.Abs(piece)
    return sp.simplify(total)

def solve_volume_of_revolution(f: sp.Expr, variable: sp.Symbol, a, b, axis: str) -> sp.Expr:
    if axis == 'x':
        return sp.pi * sp.integrate(f**2, (variable, a, b))
    elif axis == 'y':
        return 2 * sp.pi * sp.integrate(variable * f, (variable, a, b))
    else:
        raise ValueError(f"axis must be 'x' or 'y', got '{axis}'")

# ── Series ───────────────────────────────────────────────────────────────────

def solve_taylor_series(f: sp.Expr, variable: sp.Symbol, point, n: int) -> sp.Expr:
    series = sp.series(f, variable, point, n)
    result = series.removeO()
    if result.has(sp.Integral) or result == f:
        raise ValueError(
            f"Taylor series of '{f}' around {variable}={point} could not be computed. "
            f"The function may not be analytic at that point."
        )
    return result

def solve_maclaurin_series(f: sp.Expr, variable: sp.Symbol, n: int) -> sp.Expr:
    series = sp.series(f, variable, 0, n)
    result = series.removeO()
    if result.has(sp.Integral) or result == f:
        raise ValueError(
            f"Maclaurin series of '{f}' could not be computed. "
            f"The function may not be analytic at 0."
        )
    return result

def check_series_convergence(f: sp.Expr, n: sp.Symbol) -> dict:
    s = sp.Sum(f, (n, 1, sp.oo))
    result = s.doit()
    converges = bool(result.is_finite and not result.has(sp.oo, sp.zoo, sp.nan))
    return {"converges": converges, "sum": result}
