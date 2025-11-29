### 1. Designing Automata and Regular Expressions

This table breaks down how to approach designing each model.

| Model | Formal Definition | Key Design Points | Example (L = {w ∣ w contains "ab" over Σ={a,b}) |
|-------|-------------------|-------------------|------------------------------------------------|
| **NFA** (Nondeterministic Finite Automaton) | (Q, Σ, δ, q0, F) δ: Q × Σ → 2^Q | - States track pattern progress.<br>- Multiple or zero transitions per symbol.<br>- Compact due to nondeterminism.<br>- Final states for acceptance. | `q0 → q0 on a,b`<br>`q0 → q1 on a`<br>`q1 → q2 on b (final)`<br>`q2 → q2 on a,b` |
| **DFA** (Deterministic Finite Automaton) | (Q, Σ, δ, q0, F) δ: Q × Σ → Q | - One transition per symbol per state.<br>- Total function (use trap state).<br>- States track input history.<br>- Deterministic path. | `q0`: Start<br>`q1`: Saw 'a'<br>`q2`: Saw "ab" (final)<br>`q0 → q0 on b`, `q0 → q1 on a`<br>`q1 → q1 on a`, `q1 → q2 on b`<br>`q2 → q2 on a,b` |
| **ε-NFA** (NFA with Epsilon Moves) | (Q, Σ ∪ {ε}, δ, q0, F) δ: Q × (Σ ∪ {ε}) → 2^Q | - ε-transitions for free moves.<br>- Compute ε-closure for reachability.<br>- Modular for combining patterns.<br>- Flexible design. | `q0 → q1 on ε`<br>`q1 → q2 on a`<br>`q2 → q3 on b (final)`<br>`q0 → q0 on a,b`<br>ε-links for `(a\|b)*` |
| **RE** (Regular Expression) | Pattern using operators on Σ | - Union (+ or \|): Choice.<br>- Concatenation: Sequence.<br>- Kleene Star (*): Zero or more.<br>- Match language pattern. | `(a\|b)*ab(a\|b)*`<br>Any a's, b's, then "ab", then any a's, b's |


### 2. Conversions Between Models

This table summarizes the standard algorithms for converting from one model to another.

| **Conversion** | **Core Process** | **Key Formulas & Points** | **Example Insight** |
|----------------|------------------|---------------------------|---------------------|
| **ε-NFA → NFA** | Remove ε-transitions by creating direct paths | - ε-closure(q): States reachable via ε-moves.<br>- δ'(q, a) = ∪_{r ∈ ε-closure(q)} δ(r, a).<br>- Final states if ε-closure contains old final.<br>- Remove ε-transitions. | q0 → q1 on ε, q1 → q2 on a → q0 → q2 on a |
| **NFA → DFA** | Subset construction: DFA states as NFA state sets | - DFA state = subset of NFA states.<br>- δ(S, a) = ∪_{q ∈ S} δ_NFA(q, a).<br>- Start = {q0}.<br>- Final = subsets with NFA final state. | q0 → {q0, q1} on a → DFA state {q0, q1} |
| **DFA → NFA** | Trivial: DFA is an NFA | - δ_DFA(q, a) = p → δ_NFA(q, a) = {p}.<br>- Same Q, Σ, q0, F.<br>- No behavior change. | q0 → q1 on a stays same in NFA |
| **FA → RE** (NFA or DFA) | State elimination or GNFA | - Eliminate state q: p → q (R1), q → q (R2), q → r (R3) → p → r on R1 R2* R3.<br>- Final transition = RE.<br>- Arden’s Theorem for equations. | q0 → q1 on a, q1 → q2 on b → RE = ab |
| **RE → ε-NFA** | Thompson’s construction: Build per RE structure | - Symbol a: start → final on a.<br>- R+S: ε to R, S starts.<br>- RS: ε from R final to S start.<br>- R*: ε-loops around R. | ab → q0 → q1 on a, q1 → q2 on b via ε |
| **DFA → RE** | Same as NFA → RE | - Use state elimination.<br>- Solve Arden’s Rule.<br>- Capture all paths to final states. | Same as NFA → RE, simpler due to determinism |
