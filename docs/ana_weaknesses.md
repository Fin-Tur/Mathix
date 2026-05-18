# ana.py — Schwachstellen & Robustheitsleitfaden

Jeder Abschnitt benennt das Problem, zeigt ein konkretes Gegenbeispiel und gibt eine direkt umsetzbare Lösung.

---

## 1. `check_convergence` — AccumulationBounds als False-Positive

### Problem
`sp.limit` gibt für oszillierende Folgen kein `nan` zurück, sondern ein `AccumulationBounds`-Objekt.  
Dessen `.is_finite` ist `True` → die Funktion meldet fälschlicherweise **Konvergenz**.

```python
check_convergence(sin(n), n)
# → {'converges': True, 'limit': AccumBounds(-1, 1)}  ← FALSCH
```

### Fix
```python
from sympy.calculus.accumulationbounds import AccumulationBounds

def check_convergence(expr, variable):
    lim = sp.limit(expr, variable, sp.oo)
    if isinstance(lim, AccumulationBounds):
        return {"converges": False, "limit": lim}
    converges = bool(lim.is_finite) and lim is not sp.nan
    return {"converges": converges, "limit": lim}
```

---

## 2. `classify_critical_points` — Zweite-Ableitungs-Test versagt bei f''(x₀) = 0

### Problem
Wenn die zweite Ableitung an einem kritischen Punkt null ist, gibt die Funktion immer `"inconclusive"` zurück — auch wenn höhere Ableitungen eine eindeutige Klassifikation erlauben.

```python
classify_critical_points(x**4, x)
# → {0: 'inconclusive (saddle/inflection)'}  ← FALSCH (ist globales Minimum)
```

Außerdem: Wenn `val.is_positive` den Wert `None` zurückgibt (symbolischer Ausdruck), wird keiner der `if/elif`-Zweige getroffen und der Punkt landet trotzdem in `"inconclusive"`, anstatt zu signalisieren, dass die Bestimmung nicht möglich war.

### Fix
Höhere Ableitungen iterativ prüfen (erste ungerade Ordnung mit `f^(k)(x₀) ≠ 0` entscheidet):

```python
def classify_critical_points(expr, variable):
    result = {}
    for cp in sp.solve(sp.diff(expr, variable), variable):
        classification = _classify_single(expr, variable, cp)
        result[cp] = classification
    return result

def _classify_single(expr, variable, cp):
    for k in range(2, 8):
        val = sp.diff(expr, variable, k).subs(variable, cp)
        if val == 0:
            continue
        determined = val.is_positive
        if determined is None:
            return f"inconclusive (f^({k}) not determinable symbolically)"
        if k % 2 == 1:
            return "saddle point"
        return "minimum" if determined else "maximum"
    return "inconclusive (all derivatives zero up to order 7)"
```

---

## 3. `solve_tangent_line` — Stille Fehler an nicht-differenzierbaren Stellen

### Problem
Wenn die Funktion am angegebenen Punkt nicht differenzierbar ist, liefert `subs` einen `nan`- oder `zoo`-Wert. Es wird kein Fehler geworfen, das Ergebnis ist aber sinnlos.

```python
solve_tangent_line(Abs(x), x, 0)
# → nan

solve_tangent_line(x**Rational(2,3), x, 0)
# → zoo*x
```

### Fix
Slope nach der Berechnung prüfen:

```python
def solve_tangent_line(expr, variable, point):
    slope = sp.diff(expr, variable).subs(variable, point)
    if not slope.is_finite:
        raise ValueError(
            f"Die Funktion ist an x={point} nicht differenzierbar (Steigung: {slope})."
        )
    y0 = expr.subs(variable, point)
    return slope * (variable - point) + y0
```

---

## 4. `solve_area_between` — `sp.Abs`-Integration bleibt unewertet

### Problem
`sp.integrate(Abs(f-g), ...)` gibt für Ausdrücke, bei denen sich das Vorzeichen im Intervall ändert, eine **unevaluierte** `Piecewise`-Integral zurück.

```python
solve_area_between(x**2, x, x, 0, 1)
# → Integral(Piecewise(...), (x, 0, 1))  ← nicht ausgewertet
```

### Fix
Nullstellen von `f - g` im Intervall suchen, das Integral dort aufteilen und die Teilintegrale aufsummieren:

```python
def solve_area_between(expr1, expr2, variable, a, b):
    diff = expr1 - expr2
    zeros = sp.solveset(diff, variable, domain=sp.Interval(a, b))
    if isinstance(zeros, sp.FiniteSet):
        breakpoints = sorted([a] + list(zeros) + [b], key=lambda z: sp.re(z))
    else:
        breakpoints = [a, b]

    total = sp.Integer(0)
    for i in range(len(breakpoints) - 1):
        piece = sp.integrate(diff, (variable, breakpoints[i], breakpoints[i + 1]))
        total += sp.Abs(piece)
    return sp.simplify(total)
```

---

## 5. `solve_improper_integral` — Divergenz wird als `nan` verschwiegen

### Problem
Ein divergentes Integral gibt `nan` zurück, ohne dass erkennbar ist, ob das Integral divergiert oder sympy es nicht berechnen konnte. Außerdem berechnet sympy `∫₋₁¹ 1/x dx` via Cauchy-Hauptwert als `0`, was ohne diesen Hinweis mathematisch irreführend ist.

```python
solve_improper_integral(1/x, x, -1, 1)
# → nan   (stille Divergenz)
```

### Fix
Ergebnis auf Divergenz prüfen und mit Kontext zurückgeben:

```python
def solve_improper_integral(expr, variable, a, b):
    result = sp.integrate(expr, (variable, a, b))
    if result is sp.nan or result.has(sp.nan):
        raise ValueError("Das uneigentliche Integral divergiert (oder konnte nicht berechnet werden).")
    if not result.is_finite:
        raise ValueError(f"Das uneigentliche Integral divergiert: {result}")
    return result
```

---

## 6. `find_discontinuities` — Nicht-algebraische Unstetigkeiten fehlen

### Problem
`singularities()` findet nur Pole und algebraische Singularitäten. Unstetigkeitsstellen von `floor`, `ceiling`, `Heaviside`, `sign` usw. werden **komplett übersehen**.

```python
find_discontinuities(floor(x), x)
# → EmptySet   ← FALSCH (Unstetigkeiten an allen ganzen Zahlen)
```

### Fix
Nach dem `singularities`-Aufruf zusätzlich nach bekannten unstetigen Funktionen suchen:

```python
STEP_FUNCTIONS = (sp.floor, sp.ceiling, sp.Heaviside, sp.sign, sp.DiracDelta)

def find_discontinuities(expr, variable):
    result = set()
    try:
        result.update(singularities(expr, variable))
    except Exception:
        denom_expr = sp.fraction(sp.cancel(expr))[1]
        result.update(sp.solve(denom_expr, variable))

    # Warnung für Funktionen, die singularities() nicht abdeckt
    if expr.has(*STEP_FUNCTIONS):
        raise NotImplementedError(
            "Unstetigkeiten von Stufenfunktionen (floor, Heaviside, …) "
            "können nicht vollständig automatisch bestimmt werden."
        )
    return result
```

---

## 7. `find_critical_points` — `sp.solve` gibt nur Hauptlösungen zurück

### Problem
Für periodische Ableitungen wie `cos(x)` gibt `sp.solve` nur eine endliche Liste von Lösungen zurück und **verschweigt**, dass unendlich viele existieren.

```python
find_critical_points(sin(x), x)
# → [pi/2, 3*pi/2]   ← nur Hauptlösungen, kein Hinweis auf + 2πk
```

### Fix
`sp.solveset` statt `sp.solve` verwenden — gibt ein `ConditionSet` oder `ImageSet` zurück, das die volle Lösungsmenge repräsentiert:

```python
def find_critical_points(expr, variable):
    deriv = sp.diff(expr, variable)
    return sp.solveset(deriv, variable, domain=sp.S.Reals)
```

**Achtung:** Das Rückgabeformat ändert sich von `list` zu `Set` — Downstream-Code (z. B. `classify_critical_points`) muss entsprechend angepasst werden.

---

## 8. `solve_taylor_series` / `solve_maclaurin_series` — Keine Prüfung der Analytizität

### Problem
Wird eine Funktion an einer Stelle entwickelt, an der sie nicht analytisch ist (z. B. `log(x)` bei `x=0`), gibt sympy den Ausdruck unewertet zurück statt einen Fehler zu werfen.

```python
solve_taylor_series(log(x), x, 0, 5)
# → log(x)   ← nicht entwickelt, kein Fehler
```

### Fix
Prüfen, ob das Ergebnis noch `sp.Integral`/unevaluiert ist:

```python
def solve_taylor_series(expr, variable, point, n):
    series = sp.series(expr, variable, point, n)
    if series.has(sp.Order) or series == expr:
        # Letzter Test: ist das Ergebnis identisch mit dem Input?
        pass  # removeO() trotzdem versuchen, aber warnen
    result = series.removeO()
    if result.has(sp.Integral) or result == expr:
        raise ValueError(
            f"Taylorreihe von '{expr}' um {variable}={point} konnte nicht berechnet werden. "
            f"Möglicherweise ist die Funktion dort nicht analytisch."
        )
    return result
```

---

## 9. `solve_radius_of_convergence` — Kein `n` im Ausdruck → Stilles Fehlverhalten

### Problem
Wenn der Ausdruck kein Symbol `n` enthält, greift der Fallback auf `sp.Symbol('n', ...)` und liefert `1` zurück — ohne jeden Hinweis, dass die Eingabe keine Potenzreihe war.

```python
solve_radius_of_convergence(x**2, x)
# → 1   ← bedeutungslos
```

### Fix
Explizit prüfen und Fehler werfen:

```python
def solve_radius_of_convergence(expr, variable):
    a_n = expr.subs(variable, 1)
    n_candidates = [s for s in a_n.free_symbols if s.name == 'n']
    if not n_candidates:
        raise ValueError(
            "Der Ausdruck enthält kein Symbol 'n'. "
            "Bitte als allgemeines Glied mit Summationsindex n übergeben, z. B. 'x**n/factorial(n)'."
        )
    n = n_candidates[0]
    # … restliche Berechnung
```

---

## 10. `solve_indefinite_integral` — Kein `+ C`

### Problem
Das Ergebnis enthält keine Integrationskonstante. In einem Lehrkontext ist das irreführend.

```python
solve_indefinite_integral(cos(x), x)
# → sin(x)   (erwartet: sin(x) + C)
```

### Fix
Konstante `C` als freies Symbol anhängen:

```python
def solve_indefinite_integral(expr, variable):
    C = sp.Symbol('C')
    return sp.integrate(expr, variable) + C
```

---

## Zusammenfassung

| Funktion | Schwere | Kernproblem |
|---|---|---|
| `check_convergence` | **Kritisch** | AccumBounds → falsche Konvergenzaussage |
| `classify_critical_points` | **Kritisch** | f''=0 → immer inconclusive, kein höherer Test |
| `solve_tangent_line` | **Hoch** | nan/zoo statt ValueError bei Nicht-Differenzierbarkeit |
| `solve_area_between` | **Hoch** | Abs-Integration bleibt unewertet bei Vorzeichenwechsel |
| `solve_improper_integral` | **Hoch** | nan statt expliziter Divergenz-Meldung |
| `find_discontinuities` | **Mittel** | floor/Heaviside/sign komplett übersehen |
| `find_critical_points` | **Mittel** | sp.solve gibt nur Hauptlösungen, kein ConditionSet |
| `solve_taylor_series` | **Mittel** | Kein Fehler bei nicht-analytischer Entwicklungsstelle |
| `solve_radius_of_convergence` | **Gering** | Kein n → stiller Fallback-Fehler |
| `solve_indefinite_integral` | **Gering** | Kein + C |
