import sympy as sp

# ── Multivariate Differential Calculus ───────────────────────────────────────

def solve_partial_derivative(f: sp.Expr, variable: sp.Symbol) -> sp.Expr:
    return sp.diff(f, variable)

def solve_gradient(f: sp.Expr, variables: list[sp.Symbol]) -> sp.Matrix:
    return sp.Matrix([sp.diff(f, v) for v in variables])

def solve_hessian(f: sp.Expr, variables: list[sp.Symbol]) -> sp.Matrix:
    return sp.Matrix([[sp.diff(f, vi, vj) for vj in variables] for vi in variables])

def solve_directional_derivative(f: sp.Expr, variables: list[sp.Symbol], direction: list[sp.Expr]) -> sp.Expr:
    d = sp.Matrix(direction)
    norm = d.norm()
    if norm == 0:
        raise ValueError("Direction vector cannot be zero")
    d_unit = d / norm
    grad = [sp.diff(f, v) for v in variables]
    return sp.simplify(sum(g * di for g, di in zip(grad, d_unit)))

def find_critical_points_multivar(f: sp.Expr, variables: list[sp.Symbol]) -> list[dict]:
    grad = [sp.diff(f, v) for v in variables]
    return sp.solve(grad, variables, dict=True)

def classify_critical_points_multivar(f: sp.Expr, variables: list[sp.Symbol]) -> list[dict]:
    critical_points = find_critical_points_multivar(f, variables)
    H = solve_hessian(f, variables)
    results = []
    for cp in critical_points:
        H_cp = H.subs(list(cp.items()))
        try:
            eigenvals = H_cp.eigenvals()
            evs = []
            for ev, mult in eigenvals.items():
                evs.extend([sp.simplify(ev)] * mult)
            all_pos = all(bool(ev.is_positive) for ev in evs)
            all_neg = all(bool(ev.is_negative) for ev in evs)
            has_pos = any(bool(ev.is_positive) for ev in evs)
            has_neg = any(bool(ev.is_negative) for ev in evs)
            if all_pos:
                kind = "local minimum"
            elif all_neg:
                kind = "local maximum"
            elif has_pos and has_neg:
                kind = "saddle point"
            else:
                kind = "inconclusive"
        except Exception as e:
            kind = f"inconclusive: {e}"
            evs = []
        results.append({"point": cp, "classification": kind, "hessian_eigenvalues": evs})
    return results

def solve_lagrange_multiplier(f: sp.Expr, g: sp.Expr, variables: list[sp.Symbol]) -> list[dict]:
    lam = sp.Symbol('lambda')
    grad_f = [sp.diff(f, v) for v in variables]
    grad_g = [sp.diff(g, v) for v in variables]
    eqs = [gf - lam * gg for gf, gg in zip(grad_f, grad_g)] + [g]
    return sp.solve(eqs, list(variables) + [lam], dict=True)

def solve_jacobian(exprs: list[sp.Expr], variables: list[sp.Symbol]) -> sp.Matrix:
    return sp.Matrix([[sp.diff(f, v) for v in variables] for f in exprs])

# ── Multivariate Integral Calculus ────────────────────────────────────────────

def solve_double_integral(f: sp.Expr, x: sp.Symbol, x_a, x_b, y: sp.Symbol, y_a, y_b) -> sp.Expr:
    inner = sp.integrate(f, (y, y_a, y_b))
    return sp.integrate(inner, (x, x_a, x_b))

def solve_triple_integral(f: sp.Expr, x: sp.Symbol, x_a, x_b, y: sp.Symbol, y_a, y_b, z: sp.Symbol, z_a, z_b) -> sp.Expr:
    inner = sp.integrate(f, (z, z_a, z_b))
    mid = sp.integrate(inner, (y, y_a, y_b))
    return sp.integrate(mid, (x, x_a, x_b))

def solve_line_integral_scalar(f: sp.Expr, curve: list[sp.Expr], spatial_vars: list[sp.Symbol], t: sp.Symbol, a, b) -> sp.Expr:
    subs_dict = dict(zip(spatial_vars, curve))
    f_along = f.subs(subs_dict)
    ds = sp.sqrt(sp.Add(*[sp.diff(c, t)**2 for c in curve]))
    return sp.integrate(sp.simplify(f_along * ds), (t, a, b))

def solve_line_integral_vector(field: list[sp.Expr], curve: list[sp.Expr], spatial_vars: list[sp.Symbol], t: sp.Symbol, a, b) -> sp.Expr:
    subs_dict = dict(zip(spatial_vars, curve))
    dr = [sp.diff(c, t) for c in curve]
    integrand = sp.Add(*[F.subs(subs_dict) * dr_i for F, dr_i in zip(field, dr)])
    return sp.integrate(sp.simplify(integrand), (t, a, b))

# ── Vector Analysis ───────────────────────────────────────────────────────────

def solve_divergence(field: list[sp.Expr], variables: list[sp.Symbol]) -> sp.Expr:
    return sp.simplify(sp.Add(*[sp.diff(F, v) for F, v in zip(field, variables)]))

def solve_curl(field: list[sp.Expr], variables: list[sp.Symbol]) -> list[sp.Expr]:
    if len(field) != 3 or len(variables) != 3:
        raise ValueError("curl is only defined for 3D vector fields")
    Fx, Fy, Fz = field
    x, y, z = variables
    return [
        sp.simplify(sp.diff(Fz, y) - sp.diff(Fy, z)),
        sp.simplify(sp.diff(Fx, z) - sp.diff(Fz, x)),
        sp.simplify(sp.diff(Fy, x) - sp.diff(Fx, y)),
    ]

def solve_laplacian(f: sp.Expr, variables: list[sp.Symbol]) -> sp.Expr:
    return sp.simplify(sp.Add(*[sp.diff(f, v, 2) for v in variables]))

def check_conservative(field: list[sp.Expr], variables: list[sp.Symbol]) -> dict:
    if len(field) == 2:
        Fx, Fy = field
        x, y = variables
        curl_z = sp.simplify(sp.diff(Fy, x) - sp.diff(Fx, y))
        return {"conservative": curl_z == 0, "curl_z": curl_z}
    elif len(field) == 3:
        curl = solve_curl(field, variables)
        is_cons = all(sp.simplify(c) == 0 for c in curl)
        return {"conservative": is_cons, "curl": curl}
    raise ValueError("Field must be 2D or 3D")

def solve_potential(field: list[sp.Expr], variables: list[sp.Symbol]) -> sp.Expr:
    phi = sp.Integer(0)
    for F_i, x_i in zip(field, variables):
        remaining = sp.simplify(F_i - sp.diff(phi, x_i))
        phi += sp.integrate(remaining, x_i)
    return sp.simplify(phi) + sp.Symbol('C')

# ── Ordinary Differential Equations ──────────────────────────────────────────

def solve_ode(ode: sp.Expr, func: sp.Function, variable: sp.Symbol):
    return sp.dsolve(ode, func(variable))

def solve_ode_ivp(ode: sp.Expr, func: sp.Function, variable: sp.Symbol, ics: dict):
    return sp.dsolve(ode, func(variable), ics=ics)

def solve_ode_separable(ode: sp.Expr, func: sp.Function, variable: sp.Symbol):
    try:
        return sp.dsolve(ode, func(variable), hint='separable')
    except Exception:
        return sp.dsolve(ode, func(variable))

def solve_ode_linear_first(p: sp.Expr, q: sp.Expr, func: sp.Function, variable: sp.Symbol):
    f = func(variable)
    ode = f.diff(variable) + p * f - q
    return sp.dsolve(ode, f)

def solve_ode_linear_second(ode: sp.Expr, func: sp.Function, variable: sp.Symbol):
    return sp.dsolve(ode, func(variable))
