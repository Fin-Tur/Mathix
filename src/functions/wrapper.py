import ast
import json
import sympy as sp
import functions.ana as ana
import functions.ana2 as ana2
import functions.la as la
import skills.induction as induction
import skills.algebraic_equality as algebraic_equality

# ── Parsing Helpers ───────────────────────────────────────────────────────────

def _parse_matrix(s: str) -> sp.Matrix:
    try:
        data = json.loads(s)
    except (json.JSONDecodeError, ValueError):
        data = ast.literal_eval(s)
    if not isinstance(data[0], list):
        return sp.Matrix([[sp.sympify(x)] for x in data])
    return sp.Matrix([[sp.sympify(x) for x in row] for row in data])

def _parse_vectors_list(s: str) -> list:
    try:
        data = json.loads(s)
    except (json.JSONDecodeError, ValueError):
        data = ast.literal_eval(s)
    result = []
    for v in data:
        if v and not isinstance(v[0], list):
            result.append(sp.Matrix([[sp.sympify(x)] for x in v]))
        else:
            result.append(sp.Matrix([[sp.sympify(x) for x in row] for row in v]))
    return result

# ── General ───────────────────────────────────────────────────────────────────

def _call_calculate(expression):
    return ana.calculate(sp.sympify(expression))

# ── Limits & Sequences ────────────────────────────────────────────────────────

def _call_solve_limit(expr, variable, point):
    return ana.solve_limit(sp.sympify(expr), sp.Symbol(variable), sp.sympify(point))

def _call_solve_limit_direction(expr, variable, point, direction):
    return ana.solve_limit_direction(sp.sympify(expr), sp.Symbol(variable), sp.sympify(point), direction)

def _call_check_convergence(expr, variable):
    return ana.check_convergence(sp.sympify(expr), sp.Symbol(variable))

def _call_solve_sequence_limit(expr, n):
    return ana.solve_sequence_limit(sp.sympify(expr), sp.Symbol(n))

# ── Continuity ────────────────────────────────────────────────────────────────

def _call_check_continuity(expr, variable, point):
    return ana.check_continuity(sp.sympify(expr), sp.Symbol(variable), sp.sympify(point))

def _call_find_discontinuities(expr, variable):
    return ana.find_discontinuities(sp.sympify(expr), sp.Symbol(variable))

# ── Differential Calculus ─────────────────────────────────────────────────────

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
    return ana.solve_implicit_derivative(sp.sympify(expr), sp.Symbol(x), sp.Symbol(y))

# ── Integral Calculus ─────────────────────────────────────────────────────────

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

# ── Series ────────────────────────────────────────────────────────────────────

def _call_solve_taylor_series(expr, variable, point, n):
    return ana.solve_taylor_series(sp.sympify(expr), sp.Symbol(variable), sp.sympify(point), int(n))

def _call_solve_maclaurin_series(expr, variable, n):
    return ana.solve_maclaurin_series(sp.sympify(expr), sp.Symbol(variable), int(n))

def _call_check_series_convergence(expr, n):
    return ana.check_series_convergence(sp.sympify(expr), sp.Symbol(n))

def _call_solve_radius_of_convergence(expr, variable):
    return ana.solve_radius_of_convergence(sp.sympify(expr), sp.Symbol(variable))

# ── Vectors ───────────────────────────────────────────────────────────────────

def _call_vector_dot_product(v1, v2):
    return la.vector_dot_product(_parse_matrix(v1), _parse_matrix(v2))

def _call_vector_cross_product(v1, v2):
    return la.vector_cross_product(_parse_matrix(v1), _parse_matrix(v2))

def _call_vector_norm(v, p="2"):
    return la.vector_norm(_parse_matrix(v), int(p))

def _call_vector_normalize(v):
    return la.vector_normalize(_parse_matrix(v))

def _call_vector_angle(v1, v2):
    return la.vector_angle(_parse_matrix(v1), _parse_matrix(v2))

def _call_vector_projection(v, onto):
    return la.vector_projection(_parse_matrix(v), _parse_matrix(onto))

def _call_check_orthogonal(v1, v2):
    return la.check_orthogonal(_parse_matrix(v1), _parse_matrix(v2))

# ── Matrices — Basic Operations ───────────────────────────────────────────────

def _call_matrix_add(A, B):
    return la.matrix_add(_parse_matrix(A), _parse_matrix(B))

def _call_matrix_multiply(A, B):
    return la.matrix_multiply(_parse_matrix(A), _parse_matrix(B))

def _call_matrix_transpose(A):
    return la.matrix_transpose(_parse_matrix(A))

def _call_matrix_inverse(A):
    return la.matrix_inverse(_parse_matrix(A))

def _call_matrix_power(A, n):
    return la.matrix_power(_parse_matrix(A), int(n))

def _call_matrix_trace(A):
    return la.matrix_trace(_parse_matrix(A))

# ── Determinant & Rank ────────────────────────────────────────────────────────

def _call_matrix_determinant(A):
    return la.matrix_determinant(_parse_matrix(A))

def _call_matrix_rank(A):
    return la.matrix_rank(_parse_matrix(A))

def _call_check_invertible(A):
    return la.check_invertible(_parse_matrix(A))

def _call_matrix_nullity(A):
    return la.matrix_nullity(_parse_matrix(A))

# ── Linear Systems ────────────────────────────────────────────────────────────

def _call_solve_linear_system(A, b):
    return la.solve_linear_system(_parse_matrix(A), _parse_matrix(b))

def _call_solve_homogeneous_system(A):
    return la.solve_homogeneous_system(_parse_matrix(A))

def _call_gaussian_elimination(A, b):
    return la.gaussian_elimination(_parse_matrix(A), _parse_matrix(b))

def _call_check_system_consistency(A, b):
    return la.check_system_consistency(_parse_matrix(A), _parse_matrix(b))

# ── Eigenvalues & Eigenvectors ────────────────────────────────────────────────

def _call_solve_eigenvalues(A):
    return la.solve_eigenvalues(_parse_matrix(A))

def _call_solve_eigenvectors(A):
    return la.solve_eigenvectors(_parse_matrix(A))

def _call_solve_characteristic_polynomial(A):
    return la.solve_characteristic_polynomial(_parse_matrix(A))

def _call_matrix_diagonalize(A):
    return la.matrix_diagonalize(_parse_matrix(A))

def _call_check_diagonalizable(A):
    return la.check_diagonalizable(_parse_matrix(A))

# ── Vector Spaces ─────────────────────────────────────────────────────────────

def _call_find_null_space(A):
    return la.find_null_space(_parse_matrix(A))

def _call_find_column_space(A):
    return la.find_column_space(_parse_matrix(A))

def _call_find_row_space(A):
    return la.find_row_space(_parse_matrix(A))

def _call_check_linear_independence(vectors):
    return la.check_linear_independence(_parse_vectors_list(vectors))

def _call_find_basis(vectors):
    return la.find_basis(_parse_vectors_list(vectors))

def _call_solve_coordinates(v, basis):
    return la.solve_coordinates(_parse_matrix(v), _parse_vectors_list(basis))

def _call_change_of_basis(A, old_basis, new_basis):
    return la.change_of_basis(_parse_matrix(A), _parse_vectors_list(old_basis), _parse_vectors_list(new_basis))

# ── Orthogonality ─────────────────────────────────────────────────────────────

def _call_gram_schmidt(vectors):
    return la.gram_schmidt(_parse_vectors_list(vectors))

def _call_find_orthogonal_complement(subspace):
    return la.find_orthogonal_complement(_parse_vectors_list(subspace))

def _call_solve_least_squares(A, b):
    return la.solve_least_squares(_parse_matrix(A), _parse_matrix(b))

def _call_solve_orthogonal_projection(v, subspace):
    return la.solve_orthogonal_projection(_parse_matrix(v), _parse_vectors_list(subspace))

# ── Matrix Decompositions ─────────────────────────────────────────────────────

def _call_decompose_lu(A):
    return la.decompose_lu(_parse_matrix(A))

def _call_decompose_qr(A):
    return la.decompose_qr(_parse_matrix(A))

def _call_decompose_svd(A):
    return la.decompose_svd(_parse_matrix(A))

def _call_decompose_cholesky(A):
    return la.decompose_cholesky(_parse_matrix(A))

# ── Special Matrices & Properties ─────────────────────────────────────────────

def _call_check_symmetric(A):
    return la.check_symmetric(_parse_matrix(A))

def _call_check_positive_definite(A):
    return la.check_positive_definite(_parse_matrix(A))

def _call_check_orthogonal_matrix(A):
    return la.check_orthogonal_matrix(_parse_matrix(A))

def _call_matrix_norm(A, norm_type="fro"):
    return la.matrix_norm(_parse_matrix(A), norm_type)

def _call_solve_matrix_equation(A, B):
    return la.solve_matrix_equation(_parse_matrix(A), _parse_matrix(B))

# ── Ana2 Parsing Helpers ──────────────────────────────────────────────────────

def _parse_variables(s: str) -> list[sp.Symbol]:
    try:
        names = json.loads(s)
        if isinstance(names, list):
            return [sp.Symbol(n) for n in names]
    except (json.JSONDecodeError, ValueError):
        pass
    return [sp.Symbol(n.strip()) for n in s.split(',')]

def _parse_exprs_list(s: str) -> list[sp.Expr]:
    try:
        items = json.loads(s)
        return [sp.sympify(str(e)) for e in items]
    except (json.JSONDecodeError, ValueError):
        return [sp.sympify(e.strip()) for e in s.split(',')]

def _parse_ode_context(func: str, variable: str):
    x = sp.Symbol(variable)
    f = sp.Function(func)
    return x, f, {variable: x, func: f}

def _parse_ics(ics_str: str, func: str, variable: str) -> dict:
    data = json.loads(ics_str)
    x = sp.Symbol(variable)
    f = sp.Function(func)
    result = {}
    for key, val in data.items():
        key = key.strip()
        n_deriv = 0
        name_part = key
        while name_part.startswith('D'):
            n_deriv += 1
            name_part = name_part[1:]
        pt_str = name_part.split('(')[1].rstrip(')')
        pt = sp.sympify(pt_str)
        sym_key = f(pt) if n_deriv == 0 else f(x).diff(x, n_deriv).subs(x, pt)
        result[sym_key] = sp.sympify(str(val))
    return result

# ── Multivariate Differential Calculus ───────────────────────────────────────

def _call_solve_partial_derivative(expr, variable):
    return ana2.solve_partial_derivative(sp.sympify(expr), sp.Symbol(variable))

def _call_solve_gradient(expr, variables):
    return ana2.solve_gradient(sp.sympify(expr), _parse_variables(variables))

def _call_solve_hessian(expr, variables):
    return ana2.solve_hessian(sp.sympify(expr), _parse_variables(variables))

def _call_solve_directional_derivative(expr, variables, direction):
    return ana2.solve_directional_derivative(sp.sympify(expr), _parse_variables(variables), _parse_exprs_list(direction))

def _call_find_critical_points_multivar(expr, variables):
    return ana2.find_critical_points_multivar(sp.sympify(expr), _parse_variables(variables))

def _call_classify_critical_points_multivar(expr, variables):
    return ana2.classify_critical_points_multivar(sp.sympify(expr), _parse_variables(variables))

def _call_solve_lagrange_multiplier(objective, constraint, variables):
    return ana2.solve_lagrange_multiplier(sp.sympify(objective), sp.sympify(constraint), _parse_variables(variables))

def _call_solve_jacobian(exprs, variables):
    return ana2.solve_jacobian(_parse_exprs_list(exprs), _parse_variables(variables))

# ── Multivariate Integral Calculus ────────────────────────────────────────────

def _call_solve_double_integral(expr, x, x_a, x_b, y, y_a, y_b):
    return ana2.solve_double_integral(
        sp.sympify(expr),
        sp.Symbol(x), sp.sympify(x_a), sp.sympify(x_b),
        sp.Symbol(y), sp.sympify(y_a), sp.sympify(y_b),
    )

def _call_solve_triple_integral(expr, x, x_a, x_b, y, y_a, y_b, z, z_a, z_b):
    return ana2.solve_triple_integral(
        sp.sympify(expr),
        sp.Symbol(x), sp.sympify(x_a), sp.sympify(x_b),
        sp.Symbol(y), sp.sympify(y_a), sp.sympify(y_b),
        sp.Symbol(z), sp.sympify(z_a), sp.sympify(z_b),
    )

def _call_solve_line_integral_scalar(expr, curve, variable, a, b):
    t = sp.Symbol(variable)
    curve_exprs = _parse_exprs_list(curve)
    spatial = [sp.Symbol('x'), sp.Symbol('y'), sp.Symbol('z')][:len(curve_exprs)]
    return ana2.solve_line_integral_scalar(sp.sympify(expr), curve_exprs, spatial, t, sp.sympify(a), sp.sympify(b))

def _call_solve_line_integral_vector(field, curve, variable, a, b):
    t = sp.Symbol(variable)
    field_exprs = _parse_exprs_list(field)
    curve_exprs = _parse_exprs_list(curve)
    spatial = [sp.Symbol('x'), sp.Symbol('y'), sp.Symbol('z')][:len(field_exprs)]
    return ana2.solve_line_integral_vector(field_exprs, curve_exprs, spatial, t, sp.sympify(a), sp.sympify(b))

# ── Vector Analysis ───────────────────────────────────────────────────────────

def _call_solve_divergence(field, variables):
    return ana2.solve_divergence(_parse_exprs_list(field), _parse_variables(variables))

def _call_solve_curl(field, variables):
    return ana2.solve_curl(_parse_exprs_list(field), _parse_variables(variables))

def _call_solve_laplacian(expr, variables):
    return ana2.solve_laplacian(sp.sympify(expr), _parse_variables(variables))

def _call_check_conservative(field, variables):
    return ana2.check_conservative(_parse_exprs_list(field), _parse_variables(variables))

def _call_solve_potential(field, variables):
    return ana2.solve_potential(_parse_exprs_list(field), _parse_variables(variables))

# ── Ordinary Differential Equations ──────────────────────────────────────────

def _call_solve_ode(ode, func, variable):
    x, f, ctx = _parse_ode_context(func, variable)
    ode_expr = sp.sympify(ode, locals=ctx)
    return ana2.solve_ode(ode_expr, f, x)

def _call_solve_ode_ivp(ode, func, variable, initial_conditions):
    x, f, ctx = _parse_ode_context(func, variable)
    ode_expr = sp.sympify(ode, locals=ctx)
    ics = _parse_ics(initial_conditions, func, variable)
    return ana2.solve_ode_ivp(ode_expr, f, x, ics)

def _call_solve_ode_separable(ode, func, variable):
    x, f, ctx = _parse_ode_context(func, variable)
    ode_expr = sp.sympify(ode, locals=ctx)
    return ana2.solve_ode_separable(ode_expr, f, x)

def _call_solve_ode_linear_first(p, q, func, variable):
    x, f, _ = _parse_ode_context(func, variable)
    return ana2.solve_ode_linear_first(sp.sympify(p), sp.sympify(q), f, x)

def _call_solve_ode_linear_second(ode, func, variable):
    x, f, ctx = _parse_ode_context(func, variable)
    ode_expr = sp.sympify(ode, locals=ctx)
    return ana2.solve_ode_linear_second(ode_expr, f, x)

# ── Proof Skills ──────────────────────────────────────────────────────────────

def _call_prove_by_induction(claim_lhs, claim_rhs, variable, base, step_term=""):
    n = sp.Symbol(variable, integer=True, positive=True)
    ctx = {variable: n}
    lhs = sp.sympify(claim_lhs, locals=ctx)
    rhs = sp.sympify(claim_rhs, locals=ctx)
    b = sp.sympify(base)
    st = sp.sympify(step_term, locals=ctx) if step_term.strip() else None
    return induction.prove_by_induction(lhs, rhs, n, b, st)

def _call_algebraic_equality(lhs, rhs):
    lhs = sp.simplify(lhs)
    rhs = sp.simplify(rhs)
    return algebraic_equality.verify(lhs, rhs)