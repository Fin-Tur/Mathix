import functions.wrapper as wrapper

_TOOLS_LIMITS = [
    {
        "name": "solve_limit",
        "description": "Calculates the limit of a function as the variable approaches a point.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr":     {"type": "string"},
                "variable": {"type": "string"},
                "point":    {"type": "string"},
            },
            "required": ["expr", "variable", "point"],
        },
    },
    {
        "name": "solve_limit_direction",
        "description": "Calculates a one-sided limit (from the left '-' or right '+').",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr":      {"type": "string"},
                "variable":  {"type": "string"},
                "point":     {"type": "string"},
                "direction": {"type": "string", "enum": ["+", "-"]},
            },
            "required": ["expr", "variable", "point", "direction"],
        },
    },
    {
        "name": "check_convergence",
        "description": "Checks whether a sequence converges as the variable tends to infinity and returns its limit.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr":     {"type": "string"},
                "variable": {"type": "string"},
            },
            "required": ["expr", "variable"],
        },
    },
    {
        "name": "solve_sequence_limit",
        "description": "Computes the limit of a sequence as n → ∞.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr": {"type": "string"},
                "n":    {"type": "string"},
            },
            "required": ["expr", "n"],
        },
    },
    {
        "name": "check_continuity",
        "description": "Checks whether a function is continuous at a given point.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr":     {"type": "string"},
                "variable": {"type": "string"},
                "point":    {"type": "string"},
            },
            "required": ["expr", "variable", "point"],
        },
    },
    {
        "name": "find_discontinuities",
        "description": "Finds all points where a function is discontinuous.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr":     {"type": "string"},
                "variable": {"type": "string"},
            },
            "required": ["expr", "variable"],
        },
    },
]

_TOOLS_CALCULUS = [
    {
        "name": "solve_derivative",
        "description": "Calculates the first derivative of a function with respect to a variable.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr":     {"type": "string"},
                "variable": {"type": "string"},
            },
            "required": ["expr", "variable"],
        },
    },
    {
        "name": "solve_nth_derivative",
        "description": "Calculates the n-th derivative of a function.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr":     {"type": "string"},
                "variable": {"type": "string"},
                "n":        {"type": "string"},
            },
            "required": ["expr", "variable", "n"],
        },
    },
    {
        "name": "solve_tangent_line",
        "description": "Computes the equation of the tangent line to a curve at a given point.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr":     {"type": "string"},
                "variable": {"type": "string"},
                "point":    {"type": "string"},
            },
            "required": ["expr", "variable", "point"],
        },
    },
    {
        "name": "find_critical_points",
        "description": "Finds all critical points of a function where f'(x) = 0 over the reals.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr":     {"type": "string"},
                "variable": {"type": "string"},
            },
            "required": ["expr", "variable"],
        },
    },
    {
        "name": "classify_critical_points",
        "description": "Classifies critical points as local minima, maxima, or saddle points using higher-order derivative tests.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr":     {"type": "string"},
                "variable": {"type": "string"},
            },
            "required": ["expr", "variable"],
        },
    },
    {
        "name": "solve_implicit_derivative",
        "description": "Computes dy/dx via implicit differentiation from an implicit equation F(x,y) = 0.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr": {"type": "string"},
                "x":    {"type": "string"},
                "y":    {"type": "string"},
            },
            "required": ["expr", "x", "y"],
        },
    },
    {
        "name": "solve_integral",
        "description": "Calculates a definite integral.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr":      {"type": "string"},
                "integrand": {"type": "string"},
                "a":         {"type": "string"},
                "b":         {"type": "string"},
            },
            "required": ["expr", "integrand", "a", "b"],
        },
    },
    {
        "name": "solve_indefinite_integral",
        "description": "Calculates the indefinite integral (antiderivative) of a function, including the constant C.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr":     {"type": "string"},
                "variable": {"type": "string"},
            },
            "required": ["expr", "variable"],
        },
    },
    {
        "name": "solve_improper_integral",
        "description": "Calculates an improper integral; raises an error if it diverges. Use 'oo' for ∞ and '-oo' for -∞.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr":     {"type": "string"},
                "variable": {"type": "string"},
                "a":        {"type": "string"},
                "b":        {"type": "string"},
            },
            "required": ["expr", "variable", "a", "b"],
        },
    },
    {
        "name": "solve_arc_length",
        "description": "Computes the arc length of a curve y = f(x) from x = a to x = b.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr":     {"type": "string"},
                "variable": {"type": "string"},
                "a":        {"type": "string"},
                "b":        {"type": "string"},
            },
            "required": ["expr", "variable", "a", "b"],
        },
    },
    {
        "name": "solve_area_between",
        "description": "Computes the area between two curves from a to b, correctly handling sign changes.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr1":    {"type": "string"},
                "expr2":    {"type": "string"},
                "variable": {"type": "string"},
                "a":        {"type": "string"},
                "b":        {"type": "string"},
            },
            "required": ["expr1", "expr2", "variable", "a", "b"],
        },
    },
    {
        "name": "solve_volume_of_revolution",
        "description": "Computes the volume of the solid of revolution using the disc method (axis='x') or shell method (axis='y').",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr":     {"type": "string"},
                "variable": {"type": "string"},
                "a":        {"type": "string"},
                "b":        {"type": "string"},
                "axis":     {"type": "string", "enum": ["x", "y"]},
            },
            "required": ["expr", "variable", "a", "b", "axis"],
        },
    },
]

_TOOLS_SERIES = [
    {
        "name": "solve_taylor_series",
        "description": "Computes the Taylor series of a function around a point up to order n. Raises an error if the function is not analytic there.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr":     {"type": "string"},
                "variable": {"type": "string"},
                "point":    {"type": "string"},
                "n":        {"type": "string"},
            },
            "required": ["expr", "variable", "point", "n"],
        },
    },
    {
        "name": "solve_maclaurin_series",
        "description": "Computes the Maclaurin series (Taylor expansion around 0) up to order n.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr":     {"type": "string"},
                "variable": {"type": "string"},
                "n":        {"type": "string"},
            },
            "required": ["expr", "variable", "n"],
        },
    },
    {
        "name": "check_series_convergence",
        "description": "Checks whether the infinite series Σ expr converges and returns its sum if it does.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr": {"type": "string"},
                "n":    {"type": "string"},
            },
            "required": ["expr", "n"],
        },
    },
    {
        "name": "solve_radius_of_convergence",
        "description": "Computes the radius of convergence of the power series with general term a_n (given as expr in variable). Uses ratio test, falls back to root test.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr":     {"type": "string"},
                "variable": {"type": "string"},
            },
            "required": ["expr", "variable"],
        },
    },
]

_TOOLS_LA_VECTORS = [
    # ── Vectors ──────────────────────────────────────────────────────────────
    {
        "name": "vector_dot_product",
        "description": "Computes the dot product of two vectors.",
        "input_schema": {
            "type": "object",
            "properties": {
                "v1": {"type": "string"},
                "v2": {"type": "string"},
            },
            "required": ["v1", "v2"],
        },
    },
    {
        "name": "vector_cross_product",
        "description": "Computes the cross product of two 3D vectors.",
        "input_schema": {
            "type": "object",
            "properties": {
                "v1": {"type": "string"},
                "v2": {"type": "string"},
            },
            "required": ["v1", "v2"],
        },
    },
    {
        "name": "vector_norm",
        "description": "Computes the p-norm of a vector (default p=2, i.e. Euclidean norm).",
        "input_schema": {
            "type": "object",
            "properties": {
                "v": {"type": "string"},
                "p": {"type": "string"},
            },
            "required": ["v"],
        },
    },
    {
        "name": "vector_normalize",
        "description": "Returns the unit vector in the same direction as the given vector.",
        "input_schema": {
            "type": "object",
            "properties": {
                "v": {"type": "string"},
            },
            "required": ["v"],
        },
    },
    {
        "name": "vector_angle",
        "description": "Computes the angle (in radians) between two vectors.",
        "input_schema": {
            "type": "object",
            "properties": {
                "v1": {"type": "string"},
                "v2": {"type": "string"},
            },
            "required": ["v1", "v2"],
        },
    },
    {
        "name": "vector_projection",
        "description": "Projects vector v onto vector 'onto' and returns the projection vector.",
        "input_schema": {
            "type": "object",
            "properties": {
                "v":    {"type": "string"},
                "onto": {"type": "string"},
            },
            "required": ["v", "onto"],
        },
    },
    {
        "name": "check_orthogonal",
        "description": "Checks whether two vectors are orthogonal (dot product = 0).",
        "input_schema": {
            "type": "object",
            "properties": {
                "v1": {"type": "string"},
                "v2": {"type": "string"},
            },
            "required": ["v1", "v2"],
        },
    },
    # ── Vector Spaces ────────────────────────────────────────────────────────
    {
        "name": "find_null_space",
        "description": "Returns a basis for the null space (kernel) of a matrix.",
        "input_schema": {
            "type": "object",
            "properties": {
                "A": {"type": "string"},
            },
            "required": ["A"],
        },
    },
    {
        "name": "find_column_space",
        "description": "Returns a basis for the column space (image) of a matrix.",
        "input_schema": {
            "type": "object",
            "properties": {
                "A": {"type": "string"},
            },
            "required": ["A"],
        },
    },
    {
        "name": "find_row_space",
        "description": "Returns a basis for the row space of a matrix.",
        "input_schema": {
            "type": "object",
            "properties": {
                "A": {"type": "string"},
            },
            "required": ["A"],
        },
    },
    {
        "name": "check_linear_independence",
        "description": "Checks whether a list of vectors is linearly independent.",
        "input_schema": {
            "type": "object",
            "properties": {
                "vectors": {"type": "string"},
            },
            "required": ["vectors"],
        },
    },
    {
        "name": "find_basis",
        "description": "Extracts a basis from a list of vectors by removing linearly dependent ones.",
        "input_schema": {
            "type": "object",
            "properties": {
                "vectors": {"type": "string"},
            },
            "required": ["vectors"],
        },
    },
    {
        "name": "solve_coordinates",
        "description": "Expresses a vector v in terms of a given basis and returns its coordinate vector.",
        "input_schema": {
            "type": "object",
            "properties": {
                "v":     {"type": "string"},
                "basis": {"type": "string"},
            },
            "required": ["v", "basis"],
        },
    },
    {
        "name": "change_of_basis",
        "description": "Transforms a linear map A (expressed in old_basis coordinates) into new_basis coordinates.",
        "input_schema": {
            "type": "object",
            "properties": {
                "A":         {"type": "string"},
                "old_basis": {"type": "string"},
                "new_basis": {"type": "string"},
            },
            "required": ["A", "old_basis", "new_basis"],
        },
    },
    # ── Orthogonality ────────────────────────────────────────────────────────
    {
        "name": "gram_schmidt",
        "description": "Applies the Gram-Schmidt process to a list of vectors and returns an orthonormal basis.",
        "input_schema": {
            "type": "object",
            "properties": {
                "vectors": {"type": "string"},
            },
            "required": ["vectors"],
        },
    },
    {
        "name": "find_orthogonal_complement",
        "description": "Returns a basis for the orthogonal complement of the given subspace.",
        "input_schema": {
            "type": "object",
            "properties": {
                "subspace": {"type": "string"},
            },
            "required": ["subspace"],
        },
    },
    {
        "name": "solve_orthogonal_projection",
        "description": "Projects a vector v onto the subspace spanned by the given vectors.",
        "input_schema": {
            "type": "object",
            "properties": {
                "v":        {"type": "string"},
                "subspace": {"type": "string"},
            },
            "required": ["v", "subspace"],
        },
    },
]

_TOOLS_LA_MATRICES = [
    # ── Matrices — Basic Operations ──────────────────────────────────────────
    {
        "name": "matrix_add",
        "description": "Adds two matrices A + B.",
        "input_schema": {
            "type": "object",
            "properties": {
                "A": {"type": "string"},
                "B": {"type": "string"},
            },
            "required": ["A", "B"],
        },
    },
    {
        "name": "matrix_multiply",
        "description": "Multiplies two matrices A @ B.",
        "input_schema": {
            "type": "object",
            "properties": {
                "A": {"type": "string"},
                "B": {"type": "string"},
            },
            "required": ["A", "B"],
        },
    },
    {
        "name": "matrix_transpose",
        "description": "Returns the transpose of a matrix.",
        "input_schema": {
            "type": "object",
            "properties": {
                "A": {"type": "string"},
            },
            "required": ["A"],
        },
    },
    {
        "name": "matrix_inverse",
        "description": "Returns the inverse of a square matrix. Raises an error if the matrix is singular.",
        "input_schema": {
            "type": "object",
            "properties": {
                "A": {"type": "string"},
            },
            "required": ["A"],
        },
    },
    {
        "name": "matrix_power",
        "description": "Raises a square matrix to the integer power n (A^n).",
        "input_schema": {
            "type": "object",
            "properties": {
                "A": {"type": "string"},
                "n": {"type": "string"},
            },
            "required": ["A", "n"],
        },
    },
    {
        "name": "matrix_trace",
        "description": "Returns the trace of a matrix (sum of diagonal elements).",
        "input_schema": {
            "type": "object",
            "properties": {
                "A": {"type": "string"},
            },
            "required": ["A"],
        },
    },
    # ── Determinant & Rank ───────────────────────────────────────────────────
    {
        "name": "matrix_determinant",
        "description": "Computes the determinant of a square matrix.",
        "input_schema": {
            "type": "object",
            "properties": {
                "A": {"type": "string"},
            },
            "required": ["A"],
        },
    },
    {
        "name": "matrix_rank",
        "description": "Returns the rank of a matrix.",
        "input_schema": {
            "type": "object",
            "properties": {
                "A": {"type": "string"},
            },
            "required": ["A"],
        },
    },
    {
        "name": "check_invertible",
        "description": "Checks whether a matrix is invertible (det ≠ 0).",
        "input_schema": {
            "type": "object",
            "properties": {
                "A": {"type": "string"},
            },
            "required": ["A"],
        },
    },
    {
        "name": "matrix_nullity",
        "description": "Returns the nullity of a matrix (number of columns minus rank).",
        "input_schema": {
            "type": "object",
            "properties": {
                "A": {"type": "string"},
            },
            "required": ["A"],
        },
    },
    # ── Linear Systems ───────────────────────────────────────────────────────
    {
        "name": "solve_linear_system",
        "description": "Solves the linear system Ax = b. Returns the solution set (unique, parametric, or raises an error if inconsistent).",
        "input_schema": {
            "type": "object",
            "properties": {
                "A": {"type": "string"},
                "b": {"type": "string"},
            },
            "required": ["A", "b"],
        },
    },
    {
        "name": "solve_homogeneous_system",
        "description": "Solves Ax = 0 and returns a basis for the solution space (null space).",
        "input_schema": {
            "type": "object",
            "properties": {
                "A": {"type": "string"},
            },
            "required": ["A"],
        },
    },
    {
        "name": "gaussian_elimination",
        "description": "Performs Gaussian elimination on the augmented matrix [A|b] and returns the RREF, pivot columns, and rank.",
        "input_schema": {
            "type": "object",
            "properties": {
                "A": {"type": "string"},
                "b": {"type": "string"},
            },
            "required": ["A", "b"],
        },
    },
    {
        "name": "check_system_consistency",
        "description": "Checks whether the system Ax = b is consistent (has at least one solution) by comparing ranks.",
        "input_schema": {
            "type": "object",
            "properties": {
                "A": {"type": "string"},
                "b": {"type": "string"},
            },
            "required": ["A", "b"],
        },
    },
    # ── Eigenvalues & Eigenvectors ───────────────────────────────────────────
    {
        "name": "solve_eigenvalues",
        "description": "Returns the eigenvalues of a square matrix as a dict {eigenvalue: algebraic multiplicity}.",
        "input_schema": {
            "type": "object",
            "properties": {
                "A": {"type": "string"},
            },
            "required": ["A"],
        },
    },
    {
        "name": "solve_eigenvectors",
        "description": "Returns the eigenvectors of a matrix as a list of (eigenvalue, multiplicity, [eigenvectors]) tuples.",
        "input_schema": {
            "type": "object",
            "properties": {
                "A": {"type": "string"},
            },
            "required": ["A"],
        },
    },
    {
        "name": "solve_characteristic_polynomial",
        "description": "Returns the characteristic polynomial det(A - λI) as an expression in lambda.",
        "input_schema": {
            "type": "object",
            "properties": {
                "A": {"type": "string"},
            },
            "required": ["A"],
        },
    },
    {
        "name": "matrix_diagonalize",
        "description": "Diagonalizes a matrix, returning (P, D) such that A = P * D * P⁻¹. Raises an error if not diagonalizable.",
        "input_schema": {
            "type": "object",
            "properties": {
                "A": {"type": "string"},
            },
            "required": ["A"],
        },
    },
    {
        "name": "check_diagonalizable",
        "description": "Checks whether a matrix is diagonalizable over the complex numbers.",
        "input_schema": {
            "type": "object",
            "properties": {
                "A": {"type": "string"},
            },
            "required": ["A"],
        },
    },
    # ── Least Squares ────────────────────────────────────────────────────────
    {
        "name": "solve_least_squares",
        "description": "Computes the least-squares solution to the overdetermined system Ax ≈ b.",
        "input_schema": {
            "type": "object",
            "properties": {
                "A": {"type": "string"},
                "b": {"type": "string"},
            },
            "required": ["A", "b"],
        },
    },
    # ── Matrix Decompositions ────────────────────────────────────────────────
    {
        "name": "decompose_lu",
        "description": "Computes the LU decomposition of a matrix, returning (L, U, perm) where perm is a row permutation list.",
        "input_schema": {
            "type": "object",
            "properties": {
                "A": {"type": "string"},
            },
            "required": ["A"],
        },
    },
    {
        "name": "decompose_qr",
        "description": "Computes the QR decomposition of a matrix, returning (Q, R).",
        "input_schema": {
            "type": "object",
            "properties": {
                "A": {"type": "string"},
            },
            "required": ["A"],
        },
    },
    {
        "name": "decompose_svd",
        "description": "Computes the singular value decomposition, returning (U, S, V) such that A = U * S * V^T.",
        "input_schema": {
            "type": "object",
            "properties": {
                "A": {"type": "string"},
            },
            "required": ["A"],
        },
    },
    {
        "name": "decompose_cholesky",
        "description": "Computes the Cholesky decomposition L of a symmetric positive-definite matrix such that A = L * L^T.",
        "input_schema": {
            "type": "object",
            "properties": {
                "A": {"type": "string"},
            },
            "required": ["A"],
        },
    },
    # ── Special Matrices & Properties ────────────────────────────────────────
    {
        "name": "check_symmetric",
        "description": "Checks whether a matrix is symmetric (A = A^T).",
        "input_schema": {
            "type": "object",
            "properties": {
                "A": {"type": "string"},
            },
            "required": ["A"],
        },
    },
    {
        "name": "check_positive_definite",
        "description": "Checks whether a symmetric matrix is positive definite (all eigenvalues > 0).",
        "input_schema": {
            "type": "object",
            "properties": {
                "A": {"type": "string"},
            },
            "required": ["A"],
        },
    },
    {
        "name": "check_orthogonal_matrix",
        "description": "Checks whether a matrix is orthogonal (A^T * A = I).",
        "input_schema": {
            "type": "object",
            "properties": {
                "A": {"type": "string"},
            },
            "required": ["A"],
        },
    },
    {
        "name": "matrix_norm",
        "description": "Computes a matrix norm. Supported types: 'fro' (Frobenius) and 'spectral' (largest singular value).",
        "input_schema": {
            "type": "object",
            "properties": {
                "A":         {"type": "string"},
                "norm_type": {"type": "string", "enum": ["fro", "frobenius", "spectral", "2"]},
            },
            "required": ["A"],
        },
    },
    {
        "name": "solve_matrix_equation",
        "description": "Solves the matrix equation AX = B for X.",
        "input_schema": {
            "type": "object",
            "properties": {
                "A": {"type": "string"},
                "B": {"type": "string"},
            },
            "required": ["A", "B"],
        },
    },
]

_TOOLS_MULTIVAR = [
    # ── Multivariate Differential Calculus ───────────────────────────────────
    {
        "name": "solve_partial_derivative",
        "description": "Computes the partial derivative of a multivariate function with respect to one variable.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr":     {"type": "string"},
                "variable": {"type": "string"},
            },
            "required": ["expr", "variable"],
        },
    },
    {
        "name": "solve_gradient",
        "description": "Computes the gradient ∇f of a scalar function. variables is a JSON array e.g. '[\"x\",\"y\"]'.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr":      {"type": "string"},
                "variables": {"type": "string"},
            },
            "required": ["expr", "variables"],
        },
    },
    {
        "name": "solve_hessian",
        "description": "Computes the Hessian matrix H[i,j] = ∂²f/∂x_i∂x_j.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr":      {"type": "string"},
                "variables": {"type": "string"},
            },
            "required": ["expr", "variables"],
        },
    },
    {
        "name": "solve_directional_derivative",
        "description": "Computes the directional derivative of f in the given direction (automatically normalized). direction is a JSON array e.g. '[1,0]'.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr":      {"type": "string"},
                "variables": {"type": "string"},
                "direction": {"type": "string"},
            },
            "required": ["expr", "variables", "direction"],
        },
    },
    {
        "name": "find_critical_points_multivar",
        "description": "Finds critical points of a multivariate function by solving ∇f = 0.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr":      {"type": "string"},
                "variables": {"type": "string"},
            },
            "required": ["expr", "variables"],
        },
    },
    {
        "name": "classify_critical_points_multivar",
        "description": "Classifies critical points of a multivariate function using the Hessian matrix (local min/max/saddle).",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr":      {"type": "string"},
                "variables": {"type": "string"},
            },
            "required": ["expr", "variables"],
        },
    },
    {
        "name": "solve_lagrange_multiplier",
        "description": "Finds constrained extrema using Lagrange multipliers. Solves ∇f = λ∇g with constraint g = 0.",
        "input_schema": {
            "type": "object",
            "properties": {
                "objective":  {"type": "string"},
                "constraint": {"type": "string"},
                "variables":  {"type": "string"},
            },
            "required": ["objective", "constraint", "variables"],
        },
    },
    {
        "name": "solve_jacobian",
        "description": "Computes the Jacobian matrix J[i,j] = ∂f_i/∂x_j. exprs and variables are JSON arrays.",
        "input_schema": {
            "type": "object",
            "properties": {
                "exprs":     {"type": "string"},
                "variables": {"type": "string"},
            },
            "required": ["exprs", "variables"],
        },
    },
]

_TOOLS_MULTIVAR_INTEGRALS = [
    # ── Multivariate Integral Calculus ────────────────────────────────────────
    {
        "name": "solve_double_integral",
        "description": "Computes ∫∫ f dx dy over a rectangular region. Integration order: inner y, outer x.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr": {"type": "string"},
                "x":    {"type": "string"},
                "x_a":  {"type": "string"},
                "x_b":  {"type": "string"},
                "y":    {"type": "string"},
                "y_a":  {"type": "string"},
                "y_b":  {"type": "string"},
            },
            "required": ["expr", "x", "x_a", "x_b", "y", "y_a", "y_b"],
        },
    },
    {
        "name": "solve_triple_integral",
        "description": "Computes ∫∫∫ f dx dy dz over a rectangular region. Integration order: inner z, then y, outer x.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr": {"type": "string"},
                "x":    {"type": "string"},
                "x_a":  {"type": "string"},
                "x_b":  {"type": "string"},
                "y":    {"type": "string"},
                "y_a":  {"type": "string"},
                "y_b":  {"type": "string"},
                "z":    {"type": "string"},
                "z_a":  {"type": "string"},
                "z_b":  {"type": "string"},
            },
            "required": ["expr", "x", "x_a", "x_b", "y", "y_a", "y_b", "z", "z_a", "z_b"],
        },
    },
    {
        "name": "solve_line_integral_scalar",
        "description": "Computes the scalar line integral ∫_C f ds along a parametric curve. expr uses spatial variables x,y (or x,y,z for 3D). curve is a JSON array of parametric expressions in the given variable e.g. '[\"cos(t)\",\"sin(t)\"]'.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr":     {"type": "string"},
                "curve":    {"type": "string"},
                "variable": {"type": "string"},
                "a":        {"type": "string"},
                "b":        {"type": "string"},
            },
            "required": ["expr", "curve", "variable", "a", "b"],
        },
    },
    {
        "name": "solve_line_integral_vector",
        "description": "Computes the vector line integral ∫_C F·dr along a parametric curve. field and curve are JSON arrays of expressions. Spatial variables are inferred as x,y (or x,y,z).",
        "input_schema": {
            "type": "object",
            "properties": {
                "field":    {"type": "string"},
                "curve":    {"type": "string"},
                "variable": {"type": "string"},
                "a":        {"type": "string"},
                "b":        {"type": "string"},
            },
            "required": ["field", "curve", "variable", "a", "b"],
        },
    },
]

_TOOLS_VECTOR_ANALYSIS = [
    # ── Vector Analysis ───────────────────────────────────────────────────────
    {
        "name": "solve_divergence",
        "description": "Computes the divergence div F = Σ ∂F_i/∂x_i of a vector field. field and variables are JSON arrays.",
        "input_schema": {
            "type": "object",
            "properties": {
                "field":     {"type": "string"},
                "variables": {"type": "string"},
            },
            "required": ["field", "variables"],
        },
    },
    {
        "name": "solve_curl",
        "description": "Computes the curl (rotation) of a 3D vector field. field and variables are JSON arrays of length 3.",
        "input_schema": {
            "type": "object",
            "properties": {
                "field":     {"type": "string"},
                "variables": {"type": "string"},
            },
            "required": ["field", "variables"],
        },
    },
    {
        "name": "solve_laplacian",
        "description": "Computes the Laplacian Δf = Σ ∂²f/∂x_i² of a scalar function.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr":      {"type": "string"},
                "variables": {"type": "string"},
            },
            "required": ["expr", "variables"],
        },
    },
    {
        "name": "check_conservative",
        "description": "Checks whether a vector field is conservative (curl F = 0). Works for 2D and 3D fields.",
        "input_schema": {
            "type": "object",
            "properties": {
                "field":     {"type": "string"},
                "variables": {"type": "string"},
            },
            "required": ["field", "variables"],
        },
    },
    {
        "name": "solve_potential",
        "description": "Finds the scalar potential φ of a conservative field such that ∇φ = F.",
        "input_schema": {
            "type": "object",
            "properties": {
                "field":     {"type": "string"},
                "variables": {"type": "string"},
            },
            "required": ["field", "variables"],
        },
    },
]

_TOOLS_ODE = [
    # ── Ordinary Differential Equations ──────────────────────────────────────
    {
        "name": "solve_ode",
        "description": "Finds the general solution of an ODE. ode is a sympy expression equal to zero, using Derivative(y(x),x) notation. func='y', variable='x'.",
        "input_schema": {
            "type": "object",
            "properties": {
                "ode":      {"type": "string"},
                "func":     {"type": "string"},
                "variable": {"type": "string"},
            },
            "required": ["ode", "func", "variable"],
        },
    },
    {
        "name": "solve_ode_ivp",
        "description": "Solves an ODE with initial conditions. initial_conditions is a JSON dict e.g. '{\"y(0)\": 1, \"Dy(0)\": 0}' where D-prefix means derivative.",
        "input_schema": {
            "type": "object",
            "properties": {
                "ode":                {"type": "string"},
                "func":               {"type": "string"},
                "variable":           {"type": "string"},
                "initial_conditions": {"type": "string"},
            },
            "required": ["ode", "func", "variable", "initial_conditions"],
        },
    },
    {
        "name": "solve_ode_separable",
        "description": "Solves a separable ODE of the form g(y)y' = f(x).",
        "input_schema": {
            "type": "object",
            "properties": {
                "ode":      {"type": "string"},
                "func":     {"type": "string"},
                "variable": {"type": "string"},
            },
            "required": ["ode", "func", "variable"],
        },
    },
    {
        "name": "solve_ode_linear_first",
        "description": "Solves a first-order linear ODE y' + p(x)y = q(x). p and q are expressions in variable.",
        "input_schema": {
            "type": "object",
            "properties": {
                "p":        {"type": "string"},
                "q":        {"type": "string"},
                "func":     {"type": "string"},
                "variable": {"type": "string"},
            },
            "required": ["p", "q", "func", "variable"],
        },
    },
    {
        "name": "solve_ode_linear_second",
        "description": "Solves a second-order linear ODE. ode uses Derivative(y(x), x, 2) notation.",
        "input_schema": {
            "type": "object",
            "properties": {
                "ode":      {"type": "string"},
                "func":     {"type": "string"},
                "variable": {"type": "string"},
            },
            "required": ["ode", "func", "variable"],
        },
    },
]

_TOOLS_UNIVERSAL = [
    {
        "name": "calculate",
        "description": "Evaluates and simplifies any mathematical expression. Use this for arithmetic, algebraic simplification, or substituting values instead of computing manually.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expression": {"type": "string"},
            },
            "required": ["expression"],
        },
    },
]

_TOOLS_PROOF = [
    {
        "name": "prove_by_induction",
        "description": (
            "Proves a formula P(n): claim_lhs(n) = claim_rhs(n) by mathematical induction. "
            "Verifies each step with sympy.simplify(lhs - rhs).equals(0). "
            "For sum/product proofs, pass step_term as the general summand a(n) — "
            "it is substituted with n+1 automatically to form the inductive step: "
            "claim_rhs(n) + step_term(n+1) = claim_rhs(n+1). "
            "Without step_term, attempts direct algebraic verification of claim_lhs(n+1) = claim_rhs(n+1)."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "claim_lhs": {"type": "string"},
                "claim_rhs": {"type": "string"},
                "variable":  {"type": "string"},
                "base":      {"type": "string"},
                "step_term": {"type": "string"},
            },
            "required": ["claim_lhs", "claim_rhs", "variable", "base"],
        },
    },
    {
        "name": "algebraic_equality",
        "description": (
            "Proves a formula P: lhs = rhs by equality."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "lhs": {"type": "string"},
                "rhs": {"type": "string"},
            },
            "required": ["lhs", "rhs"],
        },
    },
]

TOOLS_BY_CATEGORY: dict[str, list[dict]] = {
    "limits":             _TOOLS_LIMITS,
    "calculus":           _TOOLS_CALCULUS,
    "series":             _TOOLS_SERIES,
    "la_vectors":         _TOOLS_LA_VECTORS,
    "la_matrices":        _TOOLS_LA_MATRICES,
    "multivar":           _TOOLS_MULTIVAR,
    "multivar_integrals": _TOOLS_MULTIVAR_INTEGRALS,
    "vector_analysis":    _TOOLS_VECTOR_ANALYSIS,
    "ode":                _TOOLS_ODE,
    "proof":              _TOOLS_PROOF,
}

def get_tools(categories: list[str]) -> list[dict]:
    tools = []
    for cat in categories:
        tools.extend(TOOLS_BY_CATEGORY.get(cat, []))
    tools.extend(_TOOLS_UNIVERSAL)
    tools[-1] = {**tools[-1], "cache_control": {"type": "ephemeral"}}
    return tools

TOOL_MAP = {
    # ── General ──────────────────────────────────────────────────────────────
    "calculate":                    wrapper._call_calculate,
    # ── Limits & Sequences ───────────────────────────────────────────────────
    "solve_limit":                  wrapper._call_solve_limit,
    "solve_limit_direction":        wrapper._call_solve_limit_direction,
    "check_convergence":            wrapper._call_check_convergence,
    "solve_sequence_limit":         wrapper._call_solve_sequence_limit,
    # ── Continuity ───────────────────────────────────────────────────────────
    "check_continuity":             wrapper._call_check_continuity,
    "find_discontinuities":         wrapper._call_find_discontinuities,
    # ── Differential Calculus ────────────────────────────────────────────────
    "solve_derivative":             wrapper._call_solve_derivative,
    "solve_nth_derivative":         wrapper._call_solve_nth_derivative,
    "solve_tangent_line":           wrapper._call_solve_tangent_line,
    "find_critical_points":         wrapper._call_find_critical_points,
    "classify_critical_points":     wrapper._call_classify_critical_points,
    "solve_implicit_derivative":    wrapper._call_solve_implicit_derivative,
    # ── Integral Calculus ────────────────────────────────────────────────────
    "solve_integral":               wrapper._call_solve_integral,
    "solve_indefinite_integral":    wrapper._call_solve_indefinite_integral,
    "solve_improper_integral":      wrapper._call_solve_improper_integral,
    "solve_arc_length":             wrapper._call_solve_arc_length,
    "solve_area_between":           wrapper._call_solve_area_between,
    "solve_volume_of_revolution":   wrapper._call_solve_volume_of_revolution,
    # ── Series ───────────────────────────────────────────────────────────────
    "solve_taylor_series":          wrapper._call_solve_taylor_series,
    "solve_maclaurin_series":       wrapper._call_solve_maclaurin_series,
    "check_series_convergence":     wrapper._call_check_series_convergence,
    "solve_radius_of_convergence":  wrapper._call_solve_radius_of_convergence,
    # ── Vectors ──────────────────────────────────────────────────────────────
    "vector_dot_product":           wrapper._call_vector_dot_product,
    "vector_cross_product":         wrapper._call_vector_cross_product,
    "vector_norm":                  wrapper._call_vector_norm,
    "vector_normalize":             wrapper._call_vector_normalize,
    "vector_angle":                 wrapper._call_vector_angle,
    "vector_projection":            wrapper._call_vector_projection,
    "check_orthogonal":             wrapper._call_check_orthogonal,
    # ── Matrices — Basic Operations ──────────────────────────────────────────
    "matrix_add":                   wrapper._call_matrix_add,
    "matrix_multiply":              wrapper._call_matrix_multiply,
    "matrix_transpose":             wrapper._call_matrix_transpose,
    "matrix_inverse":               wrapper._call_matrix_inverse,
    "matrix_power":                 wrapper._call_matrix_power,
    "matrix_trace":                 wrapper._call_matrix_trace,
    # ── Determinant & Rank ───────────────────────────────────────────────────
    "matrix_determinant":           wrapper._call_matrix_determinant,
    "matrix_rank":                  wrapper._call_matrix_rank,
    "check_invertible":             wrapper._call_check_invertible,
    "matrix_nullity":               wrapper._call_matrix_nullity,
    # ── Linear Systems ───────────────────────────────────────────────────────
    "solve_linear_system":          wrapper._call_solve_linear_system,
    "solve_homogeneous_system":     wrapper._call_solve_homogeneous_system,
    "gaussian_elimination":         wrapper._call_gaussian_elimination,
    "check_system_consistency":     wrapper._call_check_system_consistency,
    # ── Eigenvalues & Eigenvectors ───────────────────────────────────────────
    "solve_eigenvalues":            wrapper._call_solve_eigenvalues,
    "solve_eigenvectors":           wrapper._call_solve_eigenvectors,
    "solve_characteristic_polynomial": wrapper._call_solve_characteristic_polynomial,
    "matrix_diagonalize":           wrapper._call_matrix_diagonalize,
    "check_diagonalizable":         wrapper._call_check_diagonalizable,
    # ── Vector Spaces ────────────────────────────────────────────────────────
    "find_null_space":              wrapper._call_find_null_space,
    "find_column_space":            wrapper._call_find_column_space,
    "find_row_space":               wrapper._call_find_row_space,
    "check_linear_independence":    wrapper._call_check_linear_independence,
    "find_basis":                   wrapper._call_find_basis,
    "solve_coordinates":            wrapper._call_solve_coordinates,
    "change_of_basis":              wrapper._call_change_of_basis,
    # ── Orthogonality ────────────────────────────────────────────────────────
    "gram_schmidt":                 wrapper._call_gram_schmidt,
    "find_orthogonal_complement":   wrapper._call_find_orthogonal_complement,
    "solve_least_squares":          wrapper._call_solve_least_squares,
    "solve_orthogonal_projection":  wrapper._call_solve_orthogonal_projection,
    # ── Matrix Decompositions ────────────────────────────────────────────────
    "decompose_lu":                 wrapper._call_decompose_lu,
    "decompose_qr":                 wrapper._call_decompose_qr,
    "decompose_svd":                wrapper._call_decompose_svd,
    "decompose_cholesky":           wrapper._call_decompose_cholesky,
    # ── Special Matrices & Properties ────────────────────────────────────────
    "check_symmetric":              wrapper._call_check_symmetric,
    "check_positive_definite":      wrapper._call_check_positive_definite,
    "check_orthogonal_matrix":      wrapper._call_check_orthogonal_matrix,
    "matrix_norm":                  wrapper._call_matrix_norm,
    "solve_matrix_equation":        wrapper._call_solve_matrix_equation,
    # ── Multivariate Differential Calculus ───────────────────────────────────
    "solve_partial_derivative":          wrapper._call_solve_partial_derivative,
    "solve_gradient":                    wrapper._call_solve_gradient,
    "solve_hessian":                     wrapper._call_solve_hessian,
    "solve_directional_derivative":      wrapper._call_solve_directional_derivative,
    "find_critical_points_multivar":     wrapper._call_find_critical_points_multivar,
    "classify_critical_points_multivar": wrapper._call_classify_critical_points_multivar,
    "solve_lagrange_multiplier":         wrapper._call_solve_lagrange_multiplier,
    "solve_jacobian":                    wrapper._call_solve_jacobian,
    # ── Multivariate Integral Calculus ────────────────────────────────────────
    "solve_double_integral":             wrapper._call_solve_double_integral,
    "solve_triple_integral":             wrapper._call_solve_triple_integral,
    "solve_line_integral_scalar":        wrapper._call_solve_line_integral_scalar,
    "solve_line_integral_vector":        wrapper._call_solve_line_integral_vector,
    # ── Vector Analysis ───────────────────────────────────────────────────────
    "solve_divergence":                  wrapper._call_solve_divergence,
    "solve_curl":                        wrapper._call_solve_curl,
    "solve_laplacian":                   wrapper._call_solve_laplacian,
    "check_conservative":                wrapper._call_check_conservative,
    "solve_potential":                   wrapper._call_solve_potential,
    # ── Ordinary Differential Equations ──────────────────────────────────────
    "solve_ode":                         wrapper._call_solve_ode,
    "solve_ode_ivp":                     wrapper._call_solve_ode_ivp,
    "solve_ode_separable":               wrapper._call_solve_ode_separable,
    "solve_ode_linear_first":            wrapper._call_solve_ode_linear_first,
    "solve_ode_linear_second":           wrapper._call_solve_ode_linear_second,
    # ── Proof Skills ─────────────────────────────────────────────────────────
    "prove_by_induction":                wrapper._call_prove_by_induction,
    "algebraic_equality":                wrapper._call_algebraic_equality,
}
