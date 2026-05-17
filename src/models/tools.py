import functions.wrapper as wrapper

TOOLS = [
    {
        "name": "solve_integral",
        "description": "Calculates a definite integral of a mathematical function.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr":      {"type": "string", "description": "The integrand as a Python expression, e.g., 'x**2'"},
                "integrand": {"type": "string", "description": "The integration variable, e.g., 'x'"},
                "a":         {"type": "string", "description": "Lower integration limit, e.g., '0'"},
                "b":         {"type": "string", "description": "Upper integration limit, e.g., '1'"},
            },
            "required": ["expr", "integrand", "a", "b"],
        },
    },
    {
        "name": "solve_derivative",
        "description": "Calculates the derivative of a mathematical function with respect to a variable.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr":     {"type": "string", "description": "The expression as a Python expression, e.g., 'x**3 + 2*x'"},
                "variable": {"type": "string", "description": "The differentiation variable, e.g., 'x'"},
            },
            "required": ["expr", "variable"],
        },
    },
    {
        "name": "solve_limit",
        "description": "Calculates the limit of a mathematical function as the variable approaches a point.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expr":     {"type": "string", "description": "The expression as a Python expression, e.g., 'x**2'"},
                "variable": {"type": "string", "description": "The variable, e.g., 'x'"},
                "point":    {"type": "string", "description": "The point to which the variable approaches, e.g., '0'"},
            },
            "required": ["expr", "variable", "point"],
        },
    },
]


TOOL_MAP = {
    "solve_integral":  wrapper._call_solve_integral,
    "solve_derivative": wrapper._call_solve_derivative,
    "solve_limit": wrapper._call_solve_limit,
}