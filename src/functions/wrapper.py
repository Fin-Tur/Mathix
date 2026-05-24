import ast
import json
import sympy as sp
import functions.ana as ana
import functions.la as la

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
