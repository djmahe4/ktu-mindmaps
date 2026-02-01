# 🚀 Compiler Design (CST 302) - Module 2 Cheatsheet

## 1. Grammar Pre-Processing (Essential for Top-Down Parsing)
Top-down parsers (LL(1)) cannot handle **Left Recursion** or **Ambiguous Prefixes**.

| Problem | Rule Example | Solution (New Rules) |
| :--- | :--- | :--- |
| **Left Recursion** | $A \rightarrow A\alpha \mid \beta$ | $A \rightarrow \beta A'$ <br> $A' \rightarrow \alpha A' \mid \epsilon$ |
| **Left Factoring** | $A \rightarrow \alpha\beta_1 \mid \alpha\beta_2$ | $A \rightarrow \alpha A'$ <br> $A' \rightarrow \beta_1 \mid \beta_2$ |

---

## 2. Ambiguity & The "Dangling Else"
A grammar is **ambiguous** if one string produces $\geq 2$ Parse Trees or Leftmost Derivations (LMD).

### The Dangling Else Problem
**Ambiguous:** $S \rightarrow \text{if } E \text{ then } S \mid \text{if } E \text{ then } S \text{ else } S \mid a$
**The Logic:** An `else` should always match the closest unmatched `then`.

**Unambiguous Fix (Conceptual):**
1.  **Matched Statement:** An `if-then-else` where the nested statement is also matched.
2.  **Open Statement:** An `if-then` or an `if-then-else` where the nested statement is open.

---

## 3. FIRST and FOLLOW Rules (The "DNA" of LL(1))
These sets determine where a production rule should be placed in the parsing table.

### FIRST(X) Rules
1.  If $X$ is a **terminal**, $FIRST(X) = \{X\}$.
2.  If $X \rightarrow \epsilon$, then add $\epsilon$ to $FIRST(X)$.
3.  If $X \rightarrow Y_1 Y_2...Y_n$:
    *   Add $FIRST(Y_1)$ to $FIRST(X)$.
    *   If $Y_1 \rightarrow \epsilon$, add $FIRST(Y_2)$... and so on.

### FOLLOW(A) Rules

1. If **A** is the **start symbol**, then  
   FOLLOW(A) = { $ }.

2. If there is a production  
   B → α A β,  
   then **everything in FIRST(β) except ε** is added to FOLLOW(A).

3. If there is a production  
   B → α A  
   **or**  
   B → α A β where **ε ∈ FIRST(β)**,  
   then **everything in FOLLOW(B)** is added to FOLLOW(A).

---

## 4. LL(1) Parsing Table Construction
To be **LL(1)**, every cell in the table must contain **at most one** rule.

```mermaid
graph TD
    G[Grammar] --> LR[Eliminate Left Recursion]
    LR --> LF[Apply Left Factoring]
    LF --> FF[Calculate FIRST & FOLLOW]
    FF --> Table[Construct LL-1 Table]
    Table --> Check{Conflict?}
    Check --> |Multiple Rules in 1 Cell| NA[Not LL-1]
    Check --> |Max 1 Rule per Cell| A[LL-1 Grammar]
```

### Table Entry Rules:
For each production $A \rightarrow \alpha$:
1.  For every terminal $a \in FIRST(\alpha)$, add $A \rightarrow \alpha$ to $M[A, a]$.
2.  If $\epsilon \in FIRST(\alpha)$, for every terminal $b \in FOLLOW(A)$, add $A \rightarrow \alpha$ to $M[A, b]$.

---

## 5. Recursive Descent vs. Predictive Parsers
Both are Top-Down parsers, but they differ in how they handle choices.

| Feature | Recursive Descent | Predictive Parser (Non-Recursive) |
| :--- | :--- | :--- |
| **Method** | Uses a set of recursive procedures. | Uses an explicit Stack and a Parsing Table. |
| **Backtracking** | May use backtracking (trial and error). | **No backtracking** (lookahead symbol decides). |
| **Efficiency** | Slower (high overhead). | Faster and more systematic. |
| **Requirement** | Simple grammar. | Grammar must be LL(1). |

---

## 6. Logic Flow for Part B Problems
When solving a 10-14 mark question, follow this exact order:

1.  **Check for Left Recursion:** If $A \rightarrow A...$ exists, fix it first.
2.  **Check for Left Factoring:** If rules share a prefix, fix it.
3.  **Compute FIRST:** Start from bottom non-terminals and move up.
4.  **Compute FOLLOW:** Start from the Start Symbol ($\$$).
5.  **Build Table:** Rows = Non-terminals, Columns = Terminals.
6.  **Verify LL(1):** Explicitly state: "Since there are no multiple entries, the grammar is LL(1)."
