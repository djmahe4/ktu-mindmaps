## **Syntax-Directed Translation (SDT)**

### 1. Core Idea (Simple Explanation)
We attach **meaning** (semantics) to a grammar while parsing.  
Instead of just checking if a string is valid (syntax), we compute values, generate code, or build structures using **attributes** attached to grammar symbols.

**Two Notations:**
- **Syntax-Directed Definition (SDD)**: Grammar + semantic rules (hides evaluation order).
- **Syntax-Directed Translation (SDT) Scheme**: Grammar + embedded **semantic actions** (shows order explicitly).

**Mnemonic:** SDD = "Silent Definition" (order hidden), SDT = "Show The order" (actions visible).

### 2. Attributes – The Heart of SDT
Attributes are properties of grammar symbols (like `.val`, `.type`, `.inh`, etc.).

| Type                  | Flows From                  | Computed How?                  | Example                          | Mnemonic |
|-----------------------|-----------------------------|--------------------------------|----------------------------------|----------|
| **Synthesized**      | Children (bottom-up)       | From child attributes          | `E.val = E1.val + T.val`        | **S** = **S**on (children) |
| **Inherited**        | Parent or siblings (top-down/left-to-right) | From parent/siblings           | `T'.inh = F.val`                | **I** = **I**n from above |

**Key Rule:**  
- Synthesized attributes → **bottom-up** evaluation.  
- Inherited attributes → **top-down** or left-to-right.

**Simple Mnemonic for Direction:**
- **Synthesized** → **S**ons give value to **S**elf (up arrow).
- **Inherited** → **I**nherited from **I**mmediate parent/siblings (down/left arrow).

### 3. Types of SDDs

#### A. **S-attributed SDD**
- Contains **only synthesized attributes**.
- No inherited attributes.
- Can be evaluated **purely bottom-up** (perfect for LR parsers / shift-reduce).
- **Advantage:** Simple, no dependency issues from right-to-left.

**Example:** Simple Desk Calculator (all `.val` are synthesized)

```
L → E n          { L.val = E.val }
E → E1 + T       { E.val = E1.val + T.val }
E → T            { E.val = T.val }
T → T1 * F       { T.val = T1.val * F.val }
...
F → digit        { F.val = digit.lexval }
```

**Mind Map (Text Version):**
```
Input (3*5+4 n)
   ↓ (bottom-up)
Leaves (digits) → synthesize lexval
   ↓
F → synthesize val
   ↓
T → synthesize val (multiply)
   ↓
E → synthesize val (add)
   ↓
L → final val
```

#### B. **L-attributed SDD**
- Can have **both** synthesized and inherited attributes.
- Dependency edges in a production go **only left-to-right** (never right-to-left).
- Evaluated **top-down + left-to-right**.
- More powerful but complex.

**Example:** Simple Type Declaration
```
D → T L          { L.inh = T.type }
T → int          { T.type = integer }
L → L1 , id      { L1.inh = L.inh; addType(id, L.inh) }
L → id           { addType(id, L.inh) }
```

**Comparison Table (Easy to Memorize):**

| Feature                      | S-attributed                  | L-attributed                          |
|-----------------------------|-------------------------------|---------------------------------------|
| Attributes allowed          | Only synthesized             | Synthesized + Inherited              |
| Evaluation order            | Pure bottom-up               | Top-down + left-to-right             |
| Dependency direction        | Only upward                  | Left-to-right + upward               |
| Parser suitability          | LR (bottom-up) parsers       | LL (top-down) or modified LR         |
| Complexity                  | Simple                       | More powerful but careful ordering   |
| Mnemonic                    | **S**imple **S**ons only     | **L**eft-to-right flow               |

**Mnemonic to Remember Difference:**  
**S** = **S**ons only (pure bottom-up)  
**L** = **L**eft-to-right (can inherit from left siblings/parent)

### 4. Bottom-Up Evaluation of S-attributed Definitions
(Important for exams – [2023] Q17)

**Process (Step-by-Step):**
1. Use a **bottom-up parser** (shift-reduce / LR).
2. Maintain a **value stack** parallel to the parse stack.
3. When a reduction happens (e.g., `T → T1 * F`):
   - Pop values of right-hand side symbols.
   - Compute the semantic rule for LHS.
   - Push the new value onto the value stack.

**Example Walkthrough:** Input `4 * 5 + 3 n`

I will show it as a table (reverse-engineered from document):

| Stack (State + Value)          | Input          | Action                  | Computation                  |
|--------------------------------|----------------|-------------------------|------------------------------|
| digit 4                        | * 5 + 3 n     | Shift                   | -                            |
| F 4                            | * 5 + 3 n     | Reduce F → digit        | F.val = 4                    |
| T 4                            | * 5 + 3 n     | Reduce T → F            | T.val = 4                    |
| T *                            | 5 + 3 n       | Shift                   | -                            |
| T * digit 5                    | + 3 n         | Shift                   | -                            |
| T * F 5                        | + 3 n         | Reduce F → digit        | F.val = 5                    |
| T 20                           | + 3 n         | Reduce T → T * F        | T.val = 4 * 5 = 20           |
| E 20                           | + 3 n         | Reduce E → T            | E.val = 20                   |
| E +                            | 3 n           | Shift                   | -                            |
| ... (continue)                 | ...           | ...                     | Final L.val = 23             |

**Mnemonic for Bottom-up:**  
**"Reduce → Compute → Push"** (RCP)  
Every time you **R**educe, **C**ompute synthesized value from popped children, **P**ush to stack.

### 5. Dependency Graphs (How to Check Evaluation Order)
- Nodes = attribute instances in parse tree.
- Edge **c → b** means "b depends on c" (evaluate c first).
- No cycles → possible (topological sort exists).
- Cycle → impossible for that parse tree.

**S-attributed** → dependency graph has only upward edges → always acyclic if grammar is proper.

### 6. Quick Mind Map (Mermaid Style – Visualize This)

```mermaid
flowchart TD
    A[Syntax Directed Translation] --> B[SDD]
    A --> C[SDT Scheme]
    B --> D[S-attributed: Only Synthesized]
    B --> E[L-attributed: Synthesized + Inherited]
    D --> F[Bottom-up Evaluation<br/>Perfect for LR Parsers]
    E --> G[Top-down + Left-to-Right<br/>L-to-R dependency only]
    subgraph Attributes
        H[Synthesized: From Children ↑]
        I[Inherited: From Parent/Siblings ↓←]
    end
```

### 7. Learning Technique to Memorize
**"S-I-L" Mnemonic:**
- **S** → Synthesized, Sons, Simple (S-attributed)
- **I** → Inherited, In from above
- **L** → Left-to-right (L-attributed)

---

## Syntax Directed Translation & Intermediate Code Gen

### 4. Simple Desk Calculator – Classic S-attributed SDD (Memorize this!)

**Grammar + Semantic Rules:**

| Production              | Semantic Rule                     |
|------------------------|-----------------------------------|
| L → E n                | L.val = E.val                     |
| E → E₁ + T             | E.val = E₁.val + T.val            |
| E → T                  | E.val = T.val                     |
| T → T₁ * F             | T.val = T₁.val × F.val            |
| T → F                  | T.val = F.val                     |
| F → ( E )              | F.val = E.val                     |
| F → digit              | F.val = digit.lexval              |

**All attributes are synthesized → Pure S-attributed SDD**

**Annotated Parse Tree for 3 * 5 + 4 n** (Bottom-up evaluation)

```mermaid
flowchart TD
    L[L.val=19] --> E[E.val=19]
    E --> E1[E.val=15]
    E1 --> T1[T.val=15]
    T1 --> T11[T.val=3]
    T11 --> F1[F.val=3]
    F1 --> d1[digit.lexval=3]
    T1 --> mul[*]
    T1 --> F2[F.val=5]
    F2 --> d2[digit.lexval=5]
    E --> plus[+]
    E --> T2[T.val=4]
    T2 --> F3[F.val=4]
    F3 --> d3[digit.lexval=4]
    E --> n[n]
```

**Step-by-step bottom-up computation:**
1. digit 3 → F.val=3 → T.val=3
2. digit 5 → F.val=5
3. T → T * F → T.val = 3 * 5 = 15
4. digit 4 → F.val=4 → T.val=4
5. E → E + T → E.val = 15 + 4 = 19
6. L.val = 19

---

### 5. Inherited Attributes Example (L-attributed style)

**Grammar for multiplication chain (left-recursive removed):**

| Production       | Semantic Rules                          |
|------------------|-----------------------------------------|
| T → F T'         | T'.inh = F.val<br>T.val = T'.syn       |
| T' → * F T₁'     | T₁'.inh = T'.inh × F.val<br>T'.syn = T₁'.syn |
| T' → ε           | T'.syn = T'.inh                         |
| F → digit        | F.val = digit.lexval                    |

For input **3 * 5**:

- F.val = 3
- T'.inh = 3
- Then * F (5) → next T'.inh = 3 × 5 = 15
- Finally T'.syn = 15 → T.val = 15

**Key Point:** Inherited attributes flow **down**, synthesized flow **up**.

---

### 6. Dependency Graph & Evaluation Order

- **Dependency Graph**: Shows which attribute depends on which.
- Edge `c → b` means `b` depends on `c` → evaluate `c` **before** `b`.
- Use **Topological Sort** for evaluation order.
- If cycle → impossible to evaluate.

**Mnemonic:** Dependency Graph = "Who needs whom first?" (prerequisites)

---

### 7. Run-Time Environments (Quick Points)

- **Activation**: One execution of a procedure.
- **Activation Tree**: Shows nested/recursive calls (root = main).
- **Control Stack**: Tracks live activations (push on call, pop on return).
- **Storage Organization**:
  - **Code** (static)
  - **Static Data** (globals, known at compile time)
  - **Stack** (activation records, grows down)
  - **Heap** (dynamic, grows up)

**Activation Record (Frame) Layout (Top to Bottom):**
1. Returned value
2. Actual parameters
3. Optional control link
4. Optional access link
5. Saved machine status
6. Local data
7. Temporaries

**Allocation Strategies:**
- **Static**: Fixed at compile time (no recursion)
- **Stack**: LIFO, perfect for activations
- **Heap**: For dynamic data, retained across activations

---

### 8. Intermediate Code Generation

**Why Intermediate Code?**
- Machine-independent optimization
- Easy retargeting (change only back-end)

**Forms of Intermediate Code:**

1. **Graphical**:
   - **Syntax Tree** (condensed parse tree, operators as internal nodes)
   - **DAG** (more compact, shares common subexpressions)

2. **Linear**:
   - **Postfix** (operators after operands)
   - **Three-Address Code** (most popular)

**Three-Address Code Example:**
``` 
t1 := b * -c
t2 := t1
t3 := -c
t4 := b * t3
t5 := t2 + t4
a  := t5
```

**Representations of Three-Address Code:**

| Representation     | Fields                          | Advantage                     |
|--------------------|---------------------------------|-------------------------------|
| **Quadruples**     | op, arg1, arg2, result          | Easy to rearrange             |
| **Triples**        | op, arg1, arg2 (result = index) | Saves space (no result field) |
| **Indirect Triples**| List of pointers to triples     | Easier to reorder             |

---

### 9. Practice Question Solved: Annotated Parse Tree for 6 * 8 + 5

**Grammar (same as desk calculator, assume + and *):**

Input: **6 * 8 + 5**

**Step-by-step Annotated Parse Tree (S-attributed):**

1. 6 → digit.lexval=6 → F.val=6 → T.val=6
2. 8 → digit.lexval=8 → F.val=8
3. T → T * F → T.val = 6 * 8 = 48
4. 5 → digit.lexval=5 → F.val=5 → T.val=5
5. E → E + T → E.val = 48 + 5 = 53
6. L.val = 53

## Intermediate code gen


### 1. Why Bother with Intermediate Code?
Directly translating source code to machine code is like trying to translate ancient Sanskrit directly into modern Emoji—it's messy and inefficient. Intermediate Code (IC) provides:
* **Retargeting**: You can use the same front-end for different machines by just swapping the back-end.
* **Optimization**: It's much easier to clean up logic on a machine-independent representation than on raw assembly.

#### Common IC Representations :
1.  **Syntax Trees**: Condensed version of a parse tree.
2.  **DAG (Directed Acyclic Graphs)**: Like a syntax tree, but it identifies and "shares" common sub-expressions to save space.
3.  **Three-Address Code (TAC)**: A sequence of instructions where each has at most three addresses (two operands and one result).


---

### 2. Implementation of Three-Address Code
When you actually implement TAC in a compiler, you generally use one of three record structures :

| Method            | Fields                                      | Key Characteristic |
|------------------|----------------------------------------------|--------------------|
| Quadruples        | op, arg1, arg2, result                      | Uses explicit temporary variables (e.g., t1, t2) to store intermediate results. |
| Triples           | op, arg1, arg2                              | No explicit result field; results are referred to by their position (index) in the triple table. |
| Indirect Triples  | op, arg1, arg2 (args use pointer indices)   | A separate pointer table holds indices to triples; operands refer to these indices. The pointer index is obtained from this table, enabling easy reordering without changing the triple table. |
---

### 3. Practical Task: Solving the PYQs

### [2022] Constructing a DAG and TAC
**Expression**: $a + a * (b + c) + (b + c) * d$

1.  **Identify Common Sub-expressions**: Notice that $(b + c)$ appears twice.
2.  **Three-Address Code (TAC)**:
    * $t_1 = b + c$
    * $t_2 = a * t_1$
    * $t_3 = a + t_2$
    * $t_4 = t_1 * d$
    * $t_5 = t_3 + t_4$
3.  **DAG Construction**: The DAG will have only one node for $(b + c)$, and both the multiplication nodes for $a * \dots$ and $\dots * d$ will point to that single node.

---

#### [2023] Intermediate Code with Type Conversion
**Scenario**: `if(a > b) x = a * b else x = a - b` 
*(Note: $a, x$ are **real**, $b$ is **int**)*

To perform operations between a `real` and an `int`, we must convert the `int` to `real` first.

**TAC with Type Conversion**:
```text
100: if a > b goto 103
101: t1 = intToReal(b)
102: x = a - t1
103: goto 106
104: t2 = intToReal(b)
105: x = a * t2
106: ...
```

---

#### [2024] TAC for a `while` loop
A `while` loop requires labels to handle the repeated test and the exit jump.

**Example**: `while (i < 10) { i = i + 1; }`

**TAC**:
```text
L1: if i < 10 goto L2
    goto L3
L2: t1 = i + 1
    i = t1
    goto L1
L3: (exit)
```
---
## Mem alloc

### 1. Static Allocation
In this strategy, names are bound to storage locations as the program is compiled.

* **Mechanism:** Because bindings don't change at runtime, every time a procedure is activated, its local names are bound to the same physical memory location.
* **Characteristics:**
    * **Lifetime:** The lifetime of the data matches the entire execution of the program.
    * **Persistence:** Values of local names are retained across activations of a procedure.
* **Limitations:**
    * **No Recursion:** All activations of a procedure use the same bindings, so recursive calls would overwrite their own data.
    * **Known Size:** The size of all data objects must be known at compile time.
    * **No Dynamic Growth:** Data structures cannot be created dynamically.

---

### 2. Stack Allocation
Stack allocation manages runtime storage as a Last-In, First-Out (LIFO) structure using **Activation Records** (also called frames).

* **Mechanism:** An activation record is pushed onto the stack when a procedure is called and popped when it returns. A register (usually called `top`) marks the top of the stack and is incremented or decremented by the size of the record.
* **Activation Record Fields:**
    * **Returned Value:** To pass data back to the caller.
    * **Actual Parameters:** Supplied by the calling procedure.
    * **Control/Access Links:** To track the caller and refer to non-local data.
    * **Saved Machine Status:** Holds the program counter and register values.
    * **Local Data & Temporaries:** Storage for variables local to that specific execution.



* **Pros:** Supports **recursion** because each call gets its own fresh activation record.
* **Cons:** Values of locals are deleted as soon as the activation ends (the record is popped).

---

### 3. Heap Allocation
Heap allocation is used when the LIFO behavior of the stack isn't enough—specifically when data must outlive the procedure that created it.

* **Mechanism:** It parcels out pieces of contiguous storage as needed. These pieces can be deallocated in any order, which eventually leaves "holes" of free space in the heap.
* **Characteristics:**
    * **Flexibility:** Essential for dynamic data structures (like linked lists or trees) and objects of unknown size at compile time.
    * **Management:** Requires a heap manager to keep track of used and free space.
* **Typical Layout:** By convention, the **Stack grows down** and the **Heap grows up** into the free memory space between them.

---

### Comparison Summary

| Feature | Static Allocation | Stack Allocation | Heap Allocation |
| :--- | :--- | :--- | :--- |
| **Binding Time** | Compile time  | Runtime (on call)  | Runtime (as needed)  |
| **Recursion** | Not supported  | Supported  | Supported  |
| **Data Lifetime** | Program execution  | Procedure activation  | Manual/Garbage Collected  |
| **Typical Use** | Global variables, constants  | Local variables, parameters  | Dynamic arrays, objects  |

## Parsing conflicts

## 1. SLR Parsing Conflicts
Parsing conflicts occur when the SLR parser is in a state where it cannot decide on a single action based on the current input.

* **Shift-Reduce Conflict:** This occurs when the parser can either **shift** a new token onto the stack or **reduce** a "handle" already on the stack according to a grammar rule. The parser is unsure which path to take.
* **Reduce-Reduce Conflict:** This is more severe. It happens when the parser has identified a handle on the stack that could be **reduced by two or more different grammar rules**. It essentially doesn't know which production applies.

---

## 5. Expression Conversion

Let's convert:

\[
(a+b) * (b+c) * (a+b+c)
\]

into intermediate representations.

### Three-Address Code (TAC)

```
t1 = a + b
t2 = b + c
t3 = t1 * t2
t4 = t1 + c   // Optimized: reuse t1 for (a+b)
t5 = t3 * t4
```

### Quadruples Implementation

| Line | op | arg1 | arg2 | result |
|------|----|------|------|--------|
| (0)  | +  | a    | b    | t1     |
| (1)  | +  | b    | c    | t2     |
| (2)  | *  | t1   | t2   | t3     |
| (3)  | +  | t1   | c    | t4     |
| (4)  | *  | t3   | t4   | t5     |

### **Triples Implementation** 
| Index | op | arg1 | arg2 |
| :--- | :--- | :--- | :--- |
| (0) | + | a | b |
| (1) | + | b | c |
| (2) | * | (0) | (1) |
| (3) | + | (0) | c |
| (4) | * | (2) | (3) |

