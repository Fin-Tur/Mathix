import functions.wrapper as wrapper

TOOLS = [
    # ── Series & Limits ──────────────────────────────────────────────────
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
    # ── Differential Equations ─────────────────────────────────────────────────
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
        "description": "Finds the critical points of a function (where f'(x) = 0).",
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
        "description": "Classifies the critical points of a function as local minima, maxima, or inconclusive using the second derivative test.",
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
    # ── Integrals ─────────────────────────────────────────────────────
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
        "description": "Calculates the indefinite integral (antiderivative) of a function.",
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
        "description": "Calculates an improper integral where limits can be ±∞ (use 'oo' for ∞, '-oo' for -∞).",
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
        "description": "Computes the area between two curves from a to b.",
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
                "axis":     {"type": "string", "enum": ["x", "y"], "description": "'x' for disc method (rotation around x-axis), 'y' for shell method"},
            },
            "required": ["expr", "variable", "a", "b", "axis"],
        },
    },
    # ── Series ───────────────────────────────────────────────────────────────
    {
        "name": "solve_taylor_series",
        "description": "Computes the Taylor series expansion of a function around a point up to order n.",
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
]


TOOL_MAP = {
    "solve_limit":                  wrapper._call_solve_limit,
    "solve_limit_direction":        wrapper._call_solve_limit_direction,
    "check_convergence":            wrapper._call_check_convergence,
    "solve_sequence_limit":         wrapper._call_solve_sequence_limit,
    "check_continuity":             wrapper._call_check_continuity,
    "find_discontinuities":         wrapper._call_find_discontinuities,
    "solve_derivative":             wrapper._call_solve_derivative,
    "solve_nth_derivative":         wrapper._call_solve_nth_derivative,
    "solve_tangent_line":           wrapper._call_solve_tangent_line,
    "find_critical_points":         wrapper._call_find_critical_points,
    "classify_critical_points":     wrapper._call_classify_critical_points,
    "solve_implicit_derivative":    wrapper._call_solve_implicit_derivative,
    "solve_integral":               wrapper._call_solve_integral,
    "solve_indefinite_integral":    wrapper._call_solve_indefinite_integral,
    "solve_improper_integral":      wrapper._call_solve_improper_integral,
    "solve_arc_length":             wrapper._call_solve_arc_length,
    "solve_area_between":           wrapper._call_solve_area_between,
    "solve_volume_of_revolution":   wrapper._call_solve_volume_of_revolution,
    "solve_taylor_series":          wrapper._call_solve_taylor_series,
    "solve_maclaurin_series":       wrapper._call_solve_maclaurin_series,
    "check_series_convergence":     wrapper._call_check_series_convergence,
}
