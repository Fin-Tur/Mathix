# Analysis Functions

## ANA 1

### Folgen & Grenzwerte
| Funktion | Signatur | Beschreibung |
|---|---|---|
| `solve_limit` | `(expr, variable, point)` | Grenzwert einer Funktion ✓ |
| `solve_limit_direction` | `(expr, variable, point, direction)` | Einseitiger Grenzwert ('+' oder '-') |
| `check_convergence` | `(expr, variable)` | Konvergenz einer Folge für n→∞ |
| `solve_sequence_limit` | `(expr, n)` | Grenzwert einer Folge |

### Stetigkeit
| Funktion | Signatur | Beschreibung |
|---|---|---|
| `check_continuity` | `(expr, variable, point)` | Stetigkeit an einem Punkt |
| `find_discontinuities` | `(expr, variable)` | Alle Unstetigkeitsstellen |

### Differentialrechnung
| Funktion | Signatur | Beschreibung |
|---|---|---|
| `solve_derivative` | `(expr, variable)` | Ableitung ✓ |
| `solve_nth_derivative` | `(expr, variable, n)` | n-te Ableitung |
| `solve_tangent_line` | `(expr, variable, point)` | Tangente an einem Punkt |
| `find_critical_points` | `(expr, variable)` | Kritische Punkte (f'=0) |
| `classify_critical_points` | `(expr, variable)` | Minima / Maxima / Sattelpunkte |
| `solve_implicit_derivative` | `(expr, x, y)` | Implizite Differentiation |

### Integralrechnung
| Funktion | Signatur | Beschreibung |
|---|---|---|
| `solve_integral` | `(expr, integrand, a, b)` | Bestimmtes Integral ✓ |
| `solve_indefinite_integral` | `(expr, variable)` | Unbestimmtes Integral |
| `solve_improper_integral` | `(expr, variable, a, b)` | Uneigentliches Integral (a/b können ±∞ sein) |
| `solve_arc_length` | `(expr, variable, a, b)` | Bogenlänge einer Kurve |
| `solve_area_between` | `(expr1, expr2, variable, a, b)` | Fläche zwischen zwei Kurven |
| `solve_volume_of_revolution` | `(expr, variable, a, b, axis)` | Rotationsvolumen |

### Reihen
| Funktion | Signatur | Beschreibung |
|---|---|---|
| `solve_taylor_series` | `(expr, variable, point, n)` | Taylorreihe bis Ordnung n |
| `solve_maclaurin_series` | `(expr, variable, n)` | Maclaurin-Reihe (Entwicklung um 0) |
| `check_series_convergence` | `(expr, n)` | Konvergenz einer Reihe |
| `solve_radius_of_convergence` | `(expr, variable)` | Konvergenzradius einer Potenzreihe |

---

## ANA 2

### Differentialrechnung mehrerer Variablen
| Funktion | Signatur | Beschreibung |
|---|---|---|
| `solve_partial_derivative` | `(expr, variable)` | Partielle Ableitung |
| `solve_gradient` | `(expr, variables)` | Gradient ∇f |
| `solve_hessian` | `(expr, variables)` | Hesse-Matrix |
| `solve_directional_derivative` | `(expr, variables, direction)` | Richtungsableitung |
| `find_critical_points_multivar` | `(expr, variables)` | Kritische Punkte im Mehrdimensionalen |
| `classify_critical_points_multivar` | `(expr, variables)` | Klassifikation via Hesse-Matrix |
| `solve_lagrange_multiplier` | `(objective, constraint, variables)` | Lagrange-Multiplikatoren |
| `solve_jacobian` | `(exprs, variables)` | Jacobi-Matrix |

### Integralrechnung mehrerer Variablen
| Funktion | Signatur | Beschreibung |
|---|---|---|
| `solve_double_integral` | `(expr, x, x_a, x_b, y, y_a, y_b)` | Doppelintegral |
| `solve_triple_integral` | `(expr, x, x_a, x_b, y, y_a, y_b, z, z_a, z_b)` | Dreifachintegral |
| `solve_line_integral_scalar` | `(expr, curve, variable, a, b)` | Kurvenintegral 1. Art |
| `solve_line_integral_vector` | `(field, curve, variable, a, b)` | Kurvenintegral 2. Art |

### Vektoranalysis
| Funktion | Signatur | Beschreibung |
|---|---|---|
| `solve_divergence` | `(field, variables)` | Divergenz eines Vektorfeldes |
| `solve_curl` | `(field, variables)` | Rotation eines Vektorfeldes |
| `solve_laplacian` | `(expr, variables)` | Laplace-Operator Δf |
| `check_conservative` | `(field, variables)` | Prüft ob Feld konservativ (rot F = 0) |
| `solve_potential` | `(field, variables)` | Potentialfunktion eines konservativen Feldes |

### Gewöhnliche Differentialgleichungen
| Funktion | Signatur | Beschreibung |
|---|---|---|
| `solve_ode` | `(ode, func, variable)` | Allgemeine Lösung einer ODE |
| `solve_ode_ivp` | `(ode, func, variable, initial_conditions)` | ODE mit Anfangsbedingungen |
| `solve_ode_separable` | `(ode, func, variable)` | Trennbare ODE |
| `solve_ode_linear_first` | `(p, q, func, variable)` | Lineare ODE 1. Ordnung y' + p(x)y = q(x) |
| `solve_ode_linear_second` | `(ode, func, variable)` | Lineare ODE 2. Ordnung |
