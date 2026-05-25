from algebraic_equality import verify
import sympy as sp


def prove_by_induction(
    claim_lhs: sp.Expr,
    claim_rhs: sp.Expr,
    n: sp.Symbol,
    base: sp.Expr,
    step_term: sp.Expr | None = None,
) -> dict:
    """
    Proves P(n): claim_lhs(n) = claim_rhs(n) by mathematical induction.

    Base case:      verify claim_lhs(base) = claim_rhs(base)
    Inductive step: assuming P(n), verify P(n+1)
      - With step_term: verifies claim_rhs(n) + step_term(n+1) = claim_rhs(n+1)
        (step_term is a(n), the general summand as a function of n)
      - Without step_term: verifies claim_lhs(n+1) = claim_rhs(n+1) directly
    """
    steps = []

    # ── Base case ──────────────────────────────────────────────────────────────
    lhs_base = sp.simplify(claim_lhs.subs(n, base).doit())
    rhs_base = sp.simplify(claim_rhs.subs(n, base).doit())
    base_ok = verify(lhs_base, rhs_base)
    steps.append({
        "step": "Base case",
        "lhs": str(lhs_base),
        "rhs": str(rhs_base),
        "verified": base_ok,
    })

    if not base_ok:
        return {
            "valid": False,
            "steps": steps,
            "conclusion": f"Base case failed: {lhs_base} ≠ {rhs_base}",
        }

    # ── Inductive step ─────────────────────────────────────────────────────────
    if step_term is not None:
        lhs_step = sp.expand(claim_rhs + step_term.subs(n, n + 1))
    else:
        lhs_step = sp.simplify(claim_lhs.subs(n, n + 1).doit())

    rhs_step = sp.simplify(claim_rhs.subs(n, n + 1))
    step_ok = verify(lhs_step, rhs_step)
    steps.append({
        "step": "Inductive step",
        "hypothesis": f"Assume P({n}): {claim_rhs}",
        "lhs": str(lhs_step),
        "rhs": str(rhs_step),
        "verified": step_ok,
    })

    valid = base_ok and step_ok
    return {
        "valid": valid,
        "steps": steps,
        "conclusion": (
            f"Proof by induction complete: P({n}) holds for all {n} ≥ {base}"
            if valid
            else "Inductive step could not be verified automatically"
        ),
    }
