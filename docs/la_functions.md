# Linear Algebra Functions

## Vektoren
| Funktion | Signatur | Beschreibung |
|---|---|---|
| `vector_dot_product` | `(v1, v2)` | Skalarprodukt |
| `vector_cross_product` | `(v1, v2)` | Kreuzprodukt (3D) |
| `vector_norm` | `(v, p)` | p-Norm (Standard: p=2) |
| `vector_normalize` | `(v)` | Normierter Vektor |
| `vector_angle` | `(v1, v2)` | Winkel zwischen zwei Vektoren |
| `vector_projection` | `(v, onto)` | Projektion von v auf onto |
| `check_orthogonal` | `(v1, v2)` | Prüft Orthogonalität |

## Matrizen — Grundoperationen
| Funktion | Signatur | Beschreibung |
|---|---|---|
| `matrix_add` | `(A, B)` | Addition |
| `matrix_multiply` | `(A, B)` | Multiplikation |
| `matrix_transpose` | `(A)` | Transponierte |
| `matrix_inverse` | `(A)` | Inverse |
| `matrix_power` | `(A, n)` | Matrixpotenz Aⁿ |
| `matrix_trace` | `(A)` | Spur (Summe der Diagonale) |

## Determinante & Rang
| Funktion | Signatur | Beschreibung |
|---|---|---|
| `matrix_determinant` | `(A)` | Determinante |
| `matrix_rank` | `(A)` | Rang |
| `check_invertible` | `(A)` | Prüft ob A invertierbar (det ≠ 0) |
| `matrix_nullity` | `(A)` | Defekt (n - Rang) |

## Lineare Gleichungssysteme
| Funktion | Signatur | Beschreibung |
|---|---|---|
| `solve_linear_system` | `(A, b)` | Löst Ax = b |
| `solve_homogeneous_system` | `(A)` | Löst Ax = 0, gibt Lösungsraum zurück |
| `gaussian_elimination` | `(A, b)` | Gaußsches Eliminationsverfahren (mit Schritten) |
| `check_system_consistency` | `(A, b)` | Prüft Lösbarkeit (Rang A = Rang [A|b]) |

## Eigenwerte & Eigenvektoren
| Funktion | Signatur | Beschreibung |
|---|---|---|
| `solve_eigenvalues` | `(A)` | Eigenwerte |
| `solve_eigenvectors` | `(A)` | Eigenvektoren |
| `solve_characteristic_polynomial` | `(A)` | Charakteristisches Polynom det(A - λI) |
| `matrix_diagonalize` | `(A)` | Diagonalisierung A = PDP⁻¹ |
| `check_diagonalizable` | `(A)` | Prüft ob A diagonalisierbar |

## Vektorräume
| Funktion | Signatur | Beschreibung |
|---|---|---|
| `find_null_space` | `(A)` | Nullraum (Kern) von A |
| `find_column_space` | `(A)` | Spaltenraum (Bild) von A |
| `find_row_space` | `(A)` | Zeilenraum von A |
| `check_linear_independence` | `(vectors)` | Prüft lineare Unabhängigkeit |
| `find_basis` | `(vectors)` | Basis aus einer Vektorenmenge |
| `solve_coordinates` | `(v, basis)` | Koordinaten von v in gegebener Basis |
| `change_of_basis` | `(A, old_basis, new_basis)` | Basiswechsel |

## Orthogonalität
| Funktion | Signatur | Beschreibung |
|---|---|---|
| `gram_schmidt` | `(vectors)` | Gram-Schmidt-Orthogonalisierung |
| `find_orthogonal_complement` | `(subspace)` | Orthogonalkomplement |
| `solve_least_squares` | `(A, b)` | Kleinste-Quadrate-Lösung |
| `solve_orthogonal_projection` | `(v, subspace)` | Orthogonalprojektion auf Unterraum |

## Matrixzerlegungen
| Funktion | Signatur | Beschreibung |
|---|---|---|
| `decompose_lu` | `(A)` | LU-Zerlegung |
| `decompose_qr` | `(A)` | QR-Zerlegung |
| `decompose_svd` | `(A)` | Singulärwertzerlegung (SVD) |
| `decompose_cholesky` | `(A)` | Cholesky-Zerlegung (für pos. def. A) |

## Spezielle Matrizen & Eigenschaften
| Funktion | Signatur | Beschreibung |
|---|---|---|
| `check_symmetric` | `(A)` | Prüft Symmetrie (A = Aᵀ) |
| `check_positive_definite` | `(A)` | Prüft positive Definitheit |
| `check_orthogonal_matrix` | `(A)` | Prüft ob A orthogonal (AᵀA = I) |
| `matrix_norm` | `(A, norm_type)` | Matrixnorm (Frobenius, Spektral, ...) |
| `solve_matrix_equation` | `(A, B)` | Löst AX = B |
