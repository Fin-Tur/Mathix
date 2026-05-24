import functions.wrapper as wrapper

TOOLS = [
    # ── Limits & Sequences ───────────────────────────────────────────────────
    {
        "name": "solve_limit",
        "description": "Calculates the limit of a function as the variable approaches a point.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr":     {"type": "string", "description": "The expression, e.g. 'sin(x)/x'"},
                "variable": {"type": "string", "description": "The variable, e.g. 'x'"},
                "point":    {"type": "string", "description": "The point to approach, e.g. '0' or 'oo'"},
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
                "expr":      {"type": "string", "description": "The expression"},
                "variable":  {"type": "string", "description": "The variable"},
                "point":     {"type": "string", "description": "The point to approach"},
                "direction": {"type": "string", "enum": ["+", "-"], "description": "'+' for right-sided, '-' for left-sided"},
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
                "expr":     {"type": "string", "description": "The sequence expression, e.g. '1/n'"},
                "variable": {"type": "string", "description": "The sequence index variable, e.g. 'n'"},
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
                "expr": {"type": "string", "description": "The sequence expression, e.g. '(1 + 1/n)**n'"},
                "n":    {"type": "string", "description": "The index variable, e.g. 'n'"},
            },
            "required": ["expr", "n"],
        },
    },
    # ── Continuity ───────────────────────────────────────────────────────────
    {
        "name": "check_continuity",
        "description": "Checks whether a function is continuous at a given point.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr":     {"type": "string", "description": "The function expression"},
                "variable": {"type": "string", "description": "The variable"},
                "point":    {"type": "string", "description": "The point to check"},
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
                "expr":     {"type": "string", "description": "The function expression"},
                "variable": {"type": "string", "description": "The variable"},
            },
            "required": ["expr", "variable"],
        },
    },
    # ── Differential Calculus ────────────────────────────────────────────────
    {
        "name": "solve_derivative",
        "description": "Calculates the first derivative of a function with respect to a variable.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr":     {"type": "string", "description": "The expression, e.g. 'x**3 + 2*x'"},
                "variable": {"type": "string", "description": "The differentiation variable, e.g. 'x'"},
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
                "expr":     {"type": "string", "description": "The expression"},
                "variable": {"type": "string", "description": "The differentiation variable"},
                "n":        {"type": "string", "description": "The order of differentiation, e.g. '2'"},
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
                "expr":     {"type": "string", "description": "The function expression"},
                "variable": {"type": "string", "description": "The variable"},
                "point":    {"type": "string", "description": "The x-value of the point of tangency"},
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
                "expr":     {"type": "string", "description": "The function expression"},
                "variable": {"type": "string", "description": "The variable"},
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
                "expr":     {"type": "string", "description": "The function expression"},
                "variable": {"type": "string", "description": "The variable"},
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
                "expr": {"type": "string", "description": "The implicit equation (= 0 assumed), e.g. 'x**2 + y**2 - 4'"},
                "x":    {"type": "string", "description": "The independent variable, e.g. 'x'"},
                "y":    {"type": "string", "description": "The dependent variable, e.g. 'y'"},
            },
            "required": ["expr", "x", "y"],
        },
    },
    # ── Integral Calculus ────────────────────────────────────────────────────
    {
        "name": "solve_integral",
        "description": "Calculates a definite integral.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr":      {"type": "string", "description": "The integrand, e.g. 'x**2'"},
                "integrand": {"type": "string", "description": "The integration variable, e.g. 'x'"},
                "a":         {"type": "string", "description": "Lower limit"},
                "b":         {"type": "string", "description": "Upper limit"},
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
                "expr":     {"type": "string", "description": "The integrand"},
                "variable": {"type": "string", "description": "The integration variable"},
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
                "expr":     {"type": "string", "description": "The integrand"},
                "variable": {"type": "string", "description": "The integration variable"},
                "a":        {"type": "string", "description": "Lower limit, e.g. '0' or '-oo'"},
                "b":        {"type": "string", "description": "Upper limit, e.g. 'oo'"},
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
                "expr":     {"type": "string", "description": "The function expression"},
                "variable": {"type": "string", "description": "The variable"},
                "a":        {"type": "string", "description": "Start of interval"},
                "b":        {"type": "string", "description": "End of interval"},
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
                "expr1":    {"type": "string", "description": "First function"},
                "expr2":    {"type": "string", "description": "Second function"},
                "variable": {"type": "string", "description": "The variable"},
                "a":        {"type": "string", "description": "Left boundary"},
                "b":        {"type": "string", "description": "Right boundary"},
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
                "expr":     {"type": "string", "description": "The function expression"},
                "variable": {"type": "string", "description": "The variable"},
                "a":        {"type": "string", "description": "Start of interval"},
                "b":        {"type": "string", "description": "End of interval"},
                "axis":     {"type": "string", "enum": ["x", "y"], "description": "'x' for disc method, 'y' for shell method"},
            },
            "required": ["expr", "variable", "a", "b", "axis"],
        },
    },
    # ── Series ───────────────────────────────────────────────────────────────
    {
        "name": "solve_taylor_series",
        "description": "Computes the Taylor series of a function around a point up to order n. Raises an error if the function is not analytic there.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr":     {"type": "string", "description": "The function expression"},
                "variable": {"type": "string", "description": "The expansion variable"},
                "point":    {"type": "string", "description": "The expansion point, e.g. '0'"},
                "n":        {"type": "string", "description": "Number of terms (order), e.g. '5'"},
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
                "expr":     {"type": "string", "description": "The function expression"},
                "variable": {"type": "string", "description": "The variable"},
                "n":        {"type": "string", "description": "Number of terms (order), e.g. '6'"},
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
                "expr": {"type": "string", "description": "General term of the series, e.g. '1/n**2'"},
                "n":    {"type": "string", "description": "Summation index variable, e.g. 'n'"},
            },
            "required": ["expr", "n"],
        },
    },
    # ── Vectors ──────────────────────────────────────────────────────────────
    {
        "name": "vector_dot_product",
        "description": "Computes the dot product of two vectors.",
        "input_schema": {
            "type": "object",
            "properties": {
                "v1": {"type": "string", "description": "First vector as JSON array, e.g. '[1, 2, 3]'"},
                "v2": {"type": "string", "description": "Second vector as JSON array"},
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
                "v1": {"type": "string", "description": "First 3D vector as JSON array, e.g. '[1, 0, 0]'"},
                "v2": {"type": "string", "description": "Second 3D vector as JSON array"},
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
                "v": {"type": "string", "description": "Vector as JSON array, e.g. '[3, 4]'"},
                "p": {"type": "string", "description": "Norm order, e.g. '2' for Euclidean, '1' for Manhattan (default: '2')"},
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
                "v": {"type": "string", "description": "Vector as JSON array"},
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
                "v1": {"type": "string", "description": "First vector as JSON array"},
                "v2": {"type": "string", "description": "Second vector as JSON array"},
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
                "v":    {"type": "string", "description": "Vector to project, as JSON array"},
                "onto": {"type": "string", "description": "Target vector, as JSON array"},
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
                "v1": {"type": "string", "description": "First vector as JSON array"},
                "v2": {"type": "string", "description": "Second vector as JSON array"},
            },
            "required": ["v1", "v2"],
        },
    },
    # ── Matrices — Basic Operations ──────────────────────────────────────────
    {
        "name": "matrix_add",
        "description": "Adds two matrices A + B.",
        "input_schema": {
            "type": "object",
            "properties": {
                "A": {"type": "string", "description": "Matrix A as nested JSON array, e.g. '[[1,2],[3,4]]'"},
                "B": {"type": "string", "description": "Matrix B as nested JSON array"},
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
                "A": {"type": "string", "description": "Matrix A as nested JSON array"},
                "B": {"type": "string", "description": "Matrix B as nested JSON array"},
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
                "A": {"type": "string", "description": "Matrix as nested JSON array"},
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
                "A": {"type": "string", "description": "Square matrix as nested JSON array"},
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
                "A": {"type": "string", "description": "Square matrix as nested JSON array"},
                "n": {"type": "string", "description": "Integer exponent, e.g. '3'"},
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
                "A": {"type": "string", "description": "Square matrix as nested JSON array"},
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
                "A": {"type": "string", "description": "Square matrix as nested JSON array"},
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
                "A": {"type": "string", "description": "Matrix as nested JSON array"},
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
                "A": {"type": "string", "description": "Square matrix as nested JSON array"},
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
                "A": {"type": "string", "description": "Matrix as nested JSON array"},
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
                "A": {"type": "string", "description": "Coefficient matrix as nested JSON array"},
                "b": {"type": "string", "description": "Right-hand side vector as JSON array, e.g. '[1, 2, 3]'"},
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
                "A": {"type": "string", "description": "Coefficient matrix as nested JSON array"},
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
                "A": {"type": "string", "description": "Coefficient matrix as nested JSON array"},
                "b": {"type": "string", "description": "Right-hand side vector as JSON array"},
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
                "A": {"type": "string", "description": "Coefficient matrix as nested JSON array"},
                "b": {"type": "string", "description": "Right-hand side vector as JSON array"},
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
                "A": {"type": "string", "description": "Square matrix as nested JSON array"},
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
                "A": {"type": "string", "description": "Square matrix as nested JSON array"},
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
                "A": {"type": "string", "description": "Square matrix as nested JSON array"},
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
                "A": {"type": "string", "description": "Square matrix as nested JSON array"},
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
                "A": {"type": "string", "description": "Square matrix as nested JSON array"},
            },
            "required": ["A"],
        },
    },
    # ── Vector Spaces ────────────────────────────────────────────────────────
    {
        "name": "find_null_space",
        "description": "Returns a basis for the null space (kernel) of a matrix.",
        "input_schema": {
            "type": "object",
            "properties": {
                "A": {"type": "string", "description": "Matrix as nested JSON array"},
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
                "A": {"type": "string", "description": "Matrix as nested JSON array"},
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
                "A": {"type": "string", "description": "Matrix as nested JSON array"},
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
                "vectors": {"type": "string", "description": "JSON array of vectors, e.g. '[[1,0,0],[0,1,0]]'"},
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
                "vectors": {"type": "string", "description": "JSON array of vectors, e.g. '[[1,0],[0,1],[1,1]]'"},
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
                "v":     {"type": "string", "description": "Vector as JSON array, e.g. '[3, 5]'"},
                "basis": {"type": "string", "description": "JSON array of basis vectors, e.g. '[[1,1],[1,-1]]'"},
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
                "A":         {"type": "string", "description": "Matrix of the linear map in old_basis, as nested JSON array"},
                "old_basis": {"type": "string", "description": "JSON array of old basis vectors"},
                "new_basis": {"type": "string", "description": "JSON array of new basis vectors"},
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
                "vectors": {"type": "string", "description": "JSON array of linearly independent vectors"},
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
                "subspace": {"type": "string", "description": "JSON array of vectors spanning the subspace"},
            },
            "required": ["subspace"],
        },
    },
    {
        "name": "solve_least_squares",
        "description": "Computes the least-squares solution to the overdetermined system Ax ≈ b.",
        "input_schema": {
            "type": "object",
            "properties": {
                "A": {"type": "string", "description": "Matrix as nested JSON array"},
                "b": {"type": "string", "description": "Right-hand side vector as JSON array"},
            },
            "required": ["A", "b"],
        },
    },
    {
        "name": "solve_orthogonal_projection",
        "description": "Projects a vector v onto the subspace spanned by the given vectors.",
        "input_schema": {
            "type": "object",
            "properties": {
                "v":        {"type": "string", "description": "Vector to project, as JSON array"},
                "subspace": {"type": "string", "description": "JSON array of vectors spanning the subspace"},
            },
            "required": ["v", "subspace"],
        },
    },
    # ── Matrix Decompositions ────────────────────────────────────────────────
    {
        "name": "decompose_lu",
        "description": "Computes the LU decomposition of a matrix, returning (L, U, perm) where perm is a row permutation list.",
        "input_schema": {
            "type": "object",
            "properties": {
                "A": {"type": "string", "description": "Square matrix as nested JSON array"},
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
                "A": {"type": "string", "description": "Matrix as nested JSON array"},
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
                "A": {"type": "string", "description": "Matrix as nested JSON array"},
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
                "A": {"type": "string", "description": "Symmetric positive-definite matrix as nested JSON array"},
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
                "A": {"type": "string", "description": "Square matrix as nested JSON array"},
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
                "A": {"type": "string", "description": "Symmetric square matrix as nested JSON array"},
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
                "A": {"type": "string", "description": "Square matrix as nested JSON array"},
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
                "A":         {"type": "string", "description": "Matrix as nested JSON array"},
                "norm_type": {"type": "string", "enum": ["fro", "frobenius", "spectral", "2"], "description": "Norm type (default: 'fro')"},
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
                "A": {"type": "string", "description": "Square invertible matrix as nested JSON array"},
                "B": {"type": "string", "description": "Right-hand side matrix as nested JSON array"},
            },
            "required": ["A", "B"], 
        },
        "cache_control": {"type": "ephemeral"}
    },
]


TOOL_MAP = {
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
}
