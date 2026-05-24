import sympy as sp

# ── Vectors ───────────────────────────────────────────────────────────────────

def vector_dot_product(v1: sp.Matrix, v2: sp.Matrix) -> sp.Expr:
    return v1.dot(v2)

def vector_cross_product(v1: sp.Matrix, v2: sp.Matrix) -> sp.Matrix:
    if v1.shape != (3, 1) or v2.shape != (3, 1):
        raise ValueError("Cross product is only defined for 3D column vectors.")
    return v1.cross(v2)

def vector_norm(v: sp.Matrix, p: int = 2) -> sp.Expr:
    return v.norm(p)

def vector_normalize(v: sp.Matrix) -> sp.Matrix:
    n = v.norm()
    if n == 0:
        raise ValueError("Cannot normalize the zero vector.")
    return v / n

def vector_angle(v1: sp.Matrix, v2: sp.Matrix) -> sp.Expr:
    cos_angle = sp.simplify(v1.dot(v2) / (v1.norm() * v2.norm()))
    return sp.acos(cos_angle)

def vector_projection(v: sp.Matrix, onto: sp.Matrix) -> sp.Matrix:
    return (v.dot(onto) / onto.dot(onto)) * onto

def check_orthogonal(v1: sp.Matrix, v2: sp.Matrix) -> bool:
    return sp.simplify(v1.dot(v2)) == 0

# ── Matrices — Basic Operations ───────────────────────────────────────────────

def matrix_add(A: sp.Matrix, B: sp.Matrix) -> sp.Matrix:
    return A + B

def matrix_multiply(A: sp.Matrix, B: sp.Matrix) -> sp.Matrix:
    return A @ B

def matrix_transpose(A: sp.Matrix) -> sp.Matrix:
    return A.T

def matrix_inverse(A: sp.Matrix) -> sp.Matrix:
    if A.det() == 0:
        raise ValueError("Matrix is singular and cannot be inverted.")
    return A.inv()

def matrix_power(A: sp.Matrix, n: int) -> sp.Matrix:
    return A ** n

def matrix_trace(A: sp.Matrix) -> sp.Expr:
    return A.trace()

# ── Determinant & Rank ────────────────────────────────────────────────────────

def matrix_determinant(A: sp.Matrix) -> sp.Expr:
    return A.det()

def matrix_rank(A: sp.Matrix) -> int:
    return A.rank()

def check_invertible(A: sp.Matrix) -> bool:
    return A.det() != 0

def matrix_nullity(A: sp.Matrix) -> int:
    return A.shape[1] - A.rank()

# ── Linear Systems ────────────────────────────────────────────────────────────

def solve_linear_system(A: sp.Matrix, b: sp.Matrix):
    sol = sp.linsolve((A, b))
    if sol == sp.EmptySet:
        raise ValueError("The system Ax = b has no solution (inconsistent).")
    return sol

def solve_homogeneous_system(A: sp.Matrix) -> list:
    return A.nullspace()

def gaussian_elimination(A: sp.Matrix, b: sp.Matrix) -> dict:
    augmented = A.row_join(b)
    rref, pivots = augmented.rref()
    return {"augmented_rref": rref, "pivot_columns": pivots, "rank": len(pivots)}

def check_system_consistency(A: sp.Matrix, b: sp.Matrix) -> bool:
    return A.rank() == A.row_join(b).rank()

# ── Eigenvalues & Eigenvectors ────────────────────────────────────────────────

def solve_eigenvalues(A: sp.Matrix) -> dict:
    return A.eigenvals()

def solve_eigenvectors(A: sp.Matrix) -> list:
    return A.eigenvects()

def solve_characteristic_polynomial(A: sp.Matrix) -> sp.Expr:
    lam = sp.Symbol('lambda')
    return sp.expand((A - lam * sp.eye(A.shape[0])).det())

def matrix_diagonalize(A: sp.Matrix) -> tuple:
    try:
        return A.diagonalize()
    except Exception:
        raise ValueError("Matrix is not diagonalizable.")

def check_diagonalizable(A: sp.Matrix) -> bool:
    try:
        A.diagonalize()
        return True
    except Exception:
        return False

# ── Vector Spaces ─────────────────────────────────────────────────────────────

def find_null_space(A: sp.Matrix) -> list:
    return A.nullspace()

def find_column_space(A: sp.Matrix) -> list:
    return A.columnspace()

def find_row_space(A: sp.Matrix) -> list:
    return A.rowspace()

def check_linear_independence(vectors: list) -> bool:
    M = sp.Matrix(vectors)
    return M.rank() == len(vectors)

def find_basis(vectors: list) -> list:
    return sp.Matrix(vectors).rowspace()

def solve_coordinates(v: sp.Matrix, basis: list) -> sp.Matrix:
    B = sp.Matrix(basis).T
    return B.solve(v)

def change_of_basis(A: sp.Matrix, old_basis: list, new_basis: list) -> sp.Matrix:
    # Transforms A (expressed in old_basis) into new_basis coordinates
    P_old = sp.Matrix(old_basis).T
    P_new = sp.Matrix(new_basis).T
    return P_new.inv() * P_old * A * P_old.inv() * P_new

# ── Orthogonality ─────────────────────────────────────────────────────────────

def gram_schmidt(vectors: list) -> list:
    return sp.GramSchmidt(vectors, orthonormal=True)

def find_orthogonal_complement(subspace: list) -> list:
    return sp.Matrix(subspace).T.nullspace()

def solve_least_squares(A: sp.Matrix, b: sp.Matrix) -> sp.Matrix:
    ATA = A.T * A
    if ATA.det() == 0:
        raise ValueError("A^T A is singular; least squares solution is not unique.")
    return ATA.inv() * A.T * b

def solve_orthogonal_projection(v: sp.Matrix, subspace: list) -> sp.Matrix:
    basis = sp.GramSchmidt(subspace, orthonormal=True)
    result = sp.zeros(v.shape[0], 1)
    for u in basis:
        result += u * u.dot(v)
    return result

# ── Matrix Decompositions ─────────────────────────────────────────────────────

def decompose_lu(A: sp.Matrix) -> tuple:
    return A.LUdecomposition()  # returns (L, U, perm)

def decompose_qr(A: sp.Matrix) -> tuple:
    return A.QRdecomposition()  # returns (Q, R)

def decompose_svd(A: sp.Matrix) -> tuple:
    return A.singular_value_decomposition()  # returns (U, S, V) with A = U*S*V.T

def decompose_cholesky(A: sp.Matrix) -> sp.Matrix:
    if A != A.T:
        raise ValueError("Cholesky decomposition requires a symmetric matrix.")
    try:
        return A.cholesky()
    except Exception:
        raise ValueError("Matrix is not positive definite.")

# ── Special Matrices & Properties ─────────────────────────────────────────────

def check_symmetric(A: sp.Matrix) -> bool:
    return A == A.T

def check_positive_definite(A: sp.Matrix) -> bool:
    if A != A.T:
        return False
    return all(bool(ev.is_positive) for ev in A.eigenvals().keys())

def check_orthogonal_matrix(A: sp.Matrix) -> bool:
    n = A.shape[0]
    return sp.simplify(A.T * A) == sp.eye(n)

def matrix_norm(A: sp.Matrix, norm_type: str = 'fro') -> sp.Expr:
    if norm_type in ('fro', 'frobenius'):
        return sp.sqrt((A.T * A).trace())
    elif norm_type in ('spectral', '2'):
        return max(A.singular_values())
    else:
        raise ValueError(f"Unknown norm_type '{norm_type}'. Use 'fro' or 'spectral'.")

def solve_matrix_equation(A: sp.Matrix, B: sp.Matrix) -> sp.Matrix:
    if A.det() == 0:
        raise ValueError("Matrix A is singular; AX = B has no unique solution.")
    return A.solve(B)
