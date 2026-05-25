import sympy as sp

def verify(lhs: sp.Expr, rhs: sp.Expr) -> bool:
    diff = sp.simplify(lhs - rhs)
    if diff == 0:
        return True
    eq = diff.equals(0)
    if eq is not None:
        return bool(eq)
    # Numerical fallback (inconclusive symbolic case)
    try:
        subs = {s: sp.Integer(7) for s in diff.free_symbols}
        return abs(float(diff.evalf(subs=subs))) < 1e-9
    except Exception:
        return False