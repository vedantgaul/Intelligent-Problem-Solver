"""
Recurrence Relation Analyzer and Recursion Tree Generator
Parses recurrence equations, selects optimal solving methods,
and generates step-by-step recursion tree expansions.
"""

import re

def analyze_recurrence_equation(eq_str):
    """
    Parses recurrence string and categorizes it mathematically.
    Matches Master Theorem, Linear Decrement, Characteristic Equation, etc.
    """
    raw = " ".join(eq_str.strip().split())
    normalized = raw.replace("−", "-").replace("–", "-")

    # Match T(n) = aT(n/b) + f(n)
    master_match = re.search(r"T\s*\(\s*n\s*\)\s*=\s*(\d+)\s*T\s*\(\s*n\s*/\s*(\d+)\s*\)\s*([+-])\s*(.+)$", normalized, re.I)
    # Match T(n) = T(n/b) + f(n)
    one_match = re.search(r"T\s*\(\s*n\s*\)\s*=\s*T\s*\(\s*n\s*/\s*(\d+)\s*\)\s*([+-])\s*(.+)$", normalized, re.I)
    # Match T(n) = c1 T(n-1) + c2 T(n-2)
    characteristic_match = re.search(r"T\s*\(\s*n\s*\)\s*=.*T\s*\(\s*n\s*-\s*\d+\s*\).*T\s*\(\s*n\s*-\s*\d+\s*\)", normalized, re.I)
    # Match T(n) = T(n - k) + f(n)
    linear_match = re.search(r"T\s*\(\s*n\s*\)\s*=\s*T\s*\(\s*n\s*-\s*(\d+)\s*\)\s*([+-])\s*(.+)$", normalized, re.I)

    if characteristic_match:
        return {
            "category": "Linear Homogeneous / Non-Homogeneous",
            "summary": "This recurrence contains multiple previous terms such as T(n-1) and T(n-2) (e.g. Fibonacci sequence). It is uniquely suited for the Characteristic Equation method.",
            "recommended": "Characteristic Equation",
            "methods": [
                {
                    "name": "Characteristic Equation",
                    "why": "The recurrence expresses T(n) as a linear combination of previous discrete terms. Characteristic roots immediately yield the closed-form general solution.",
                    "match": "Optimal Mathematical Match"
                },
                {
                    "name": "Substitution Method",
                    "why": "Once the asymptotic order is guessed from characteristic roots, mathematical induction proves the upper/lower bounds.",
                    "match": "Verification Approach"
                },
                {
                    "name": "Iteration Method",
                    "why": "Repeated unrolling can expose recursive coefficients, but becomes complex with multiple terms.",
                    "match": "Alternative Technique"
                }
            ]
        }

    if linear_match:
        k = linear_match.group(1)
        return {
            "category": "Linear Decrease Recurrence",
            "summary": f"The argument decreases additively by {k}: T(n) = T(n-{k}) + f(n). Repeated unrolling (Iteration) directly exposes the arithmetic series summation.",
            "recommended": "Iteration Method",
            "methods": [
                {
                    "name": "Iteration Method",
                    "why": f"Repeatedly expanding T(n) into T(n-{k}), T(n-{2*int(k)}), ..., until base case exposes the total work sum over n/{k} steps.",
                    "match": "Direct Algebraic Solution"
                },
                {
                    "name": "Substitution Method",
                    "why": "Assume an asymptotic hypothesis O(n) or O(n^2) and establish induction base and step.",
                    "match": "Inductive Proof"
                },
                {
                    "name": "Recursion Tree",
                    "why": "Unfolds into a linear chain of recursive calls. Useful conceptually, though functionally equivalent to iteration.",
                    "match": "Visual Representation"
                }
            ]
        }

    if one_match:
        b = one_match.group(1)
        return {
            "category": "Single Subproblem Divide-and-Conquer",
            "summary": f"The equation has a single recursive call with input reduced by factor {b} (e.g., Binary Search). Master Theorem or Substitution directly yields the logarithmic bound.",
            "recommended": "Substitution Method",
            "methods": [
                {
                    "name": "Substitution Method",
                    "why": f"With only one branch T(n/{b}), establishing an inductive bound (e.g., c * log n) is straightforward and clean.",
                    "match": "Recommended for Single Branch"
                },
                {
                    "name": "Master Theorem",
                    "why": f"Fits standard Master Theorem with a=1, b={b}. Directly determines log_b(a) = 0.",
                    "match": "Direct Theorem Match"
                },
                {
                    "name": "Recursion Tree",
                    "why": f"Visualizes the linear tree of depth log_{b}(n) and constant or polynomial work per level.",
                    "match": "Structural Visualization"
                },
                {
                    "name": "Iteration Method",
                    "why": f"Expanding T(n/{b}) iteratively demonstrates geometric or logarithmic progression.",
                    "match": "Expansion Method"
                }
            ]
        }

    if master_match:
        a = master_match.group(1)
        b = master_match.group(2)
        f_n = master_match.group(4)
        return {
            "category": "Divide-and-Conquer Recurrence",
            "summary": f"Matches standard Master Theorem form T(n) = {a}T(n/{b}) + {f_n}. Branching factor a={a}, division factor b={b}.",
            "recommended": "Master Theorem",
            "methods": [
                {
                    "name": "Master Theorem",
                    "why": f"Directly applicable. Compare f(n)={f_n} with n^(log_{b} {a}) to classify into Case 1, 2, or 3.",
                    "match": "Direct Structural Formula"
                },
                {
                    "name": "Recursion Tree",
                    "why": f"Shows a tree of height log_{b}(n) with {a}^i subproblems at depth i, helping calculate total work across all levels.",
                    "match": "Intuitive Tree Visualization"
                },
                {
                    "name": "Substitution Method",
                    "why": "Proves the tight bound derived from Master Theorem using mathematical induction.",
                    "match": "Rigorous Proof"
                },
                {
                    "name": "Iteration Method",
                    "why": "Algebraically sums work level by level.",
                    "match": "Alternative Algebraic Expansion"
                }
            ]
        }

    # General fallback
    return {
        "category": "General Recurrence",
        "summary": "Could not recognize an exact closed pattern. Showing general recurrence methods.",
        "recommended": "Substitution Method",
        "methods": [
            {
                "name": "Substitution Method",
                "why": "Applicable to almost all recurrences once a good upper bound guess is formulated.",
                "match": "General Universal Method"
            },
            {
                "name": "Recursion Tree",
                "why": "Provides a graphical breakdown of problem expansion and work distribution.",
                "match": "Visual Analysis"
            },
            {
                "name": "Iteration Method",
                "why": "Expands terms backwards toward the base case to recognize series summation patterns.",
                "match": "Expansion Technique"
            }
        ]
    }

def generate_rec_tree(n=16, depth=4, branching=2):
    """
    Builds tree node hierarchy for recursive visualization.
    Returns nodes with levels, coordinates, and labels.
    """
    nodes = []
    edges = []
    counter = [0]

    def build_node(val, level, parent_id=None):
        node_id = counter[0]
        counter[0] += 1
        label = f"T({int(val)})" if val >= 1 else "T(1)"
        nodes.append({
            "id": node_id,
            "level": level,
            "val": val,
            "label": label
        })
        if parent_id is not None:
            edges.append((parent_id, node_id))

        if level < depth and val > 1:
            for _ in range(branching):
                build_node(val / branching, level + 1, node_id)

    build_node(float(n), 0)
    return {"nodes": nodes, "edges": edges, "max_depth": depth}
