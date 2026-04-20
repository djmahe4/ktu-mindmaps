# Mod 5

## Code opt

### **1. Introduction to Code Optimization**

**What is Code Optimization?**  
It is the process of transforming the code (source / intermediate / target) to make it:
- **Faster** (less execution time)
- **Smaller** (less memory)
- **Better** (efficient use of resources)

**Important Rules (Criteria):**
- Must **preserve meaning** of the program (same output for same input)
- Must give **noticeable improvement**
- Effort should be **worth it**

**Need for Optimization:**
- Compiler-generated code is usually not perfect
- Hand optimization is tedious and error-prone
- Programmer doesnt know machine level details
- Modern CPUs (pipelining, caches) need optimized code
- Improves reusability & maintainability

**Mnemonic:**  
**P.E.W.** → Preserve meaning, Efficiency gain, Worth the effort

---

### **2. Where & How Optimization is Done**

Optimization can be applied at **3 places**:

1. **Source code** (Programmer does – loop tuning, better algorithm)
2. **Intermediate code** (Compiler does – most optimizations happen here)
3. **Target code** (Compiler does – peephole, register usage)

**Two Types of Optimization:**

| Type                      | Meaning                              | Example                     |
|---------------------------|--------------------------------------|-----------------------------|
| **Machine Independent**   | Works on any machine                 | CSE, Constant folding, Loop opts |
| **Machine Dependent**     | Specific to a particular CPU         | Peephole, Register allocation |

**Two Phases of Optimization:**

- **Local Optimization** → Inside one **Basic Block** (small straight-line code)
- **Global Optimization** → Across multiple blocks, loops, functions

**Mnemonic (Order):**  
**L**ocal **first**, then **G**lobal → **L**ove **G**lobal (Local before Global)

---

### **3. Basic Block & Flow Graph** (Foundation)

**Basic Block:**  
A sequence of consecutive 3-address statements that:
- Can be entered only at the **beginning**
- Executed **sequentially** without branches

**How to find Basic Blocks? (Algorithm 8.5)**  
Find **Leader** statements using 3 rules:

1. First statement of the program
2. Target of any jump (conditional or unconditional)
3. Statement immediately following a jump

**Flow Graph:**  
Pictorial representation of control flow.  
- **Nodes** = Basic Blocks  
- **Edges** = Possible control flow between blocks  
- Directed graph G = (N, E, n₀)

**Mind Map for Basic Block:**

```
Basic Block
   ├── Leader Rules (3)
   ├── Sequence without branch
   └── Used for Local Optimization
```

---

### **4. Principal Sources of Optimization**

#### **A. Function-Preserving Transformations** (Local + Global)

1. **Common Subexpression Elimination (CSE)**  
   If same expression computed again and variables not changed → reuse previous value.

   **Example (in B5 block):**
   ``` 
   Before: t6=4*i; x=a[t6]; t7=4*i; ...
   After:  t6=4*i; x=a[t6]; t7=t6; ...   (reuse t6)
   ```

2. **Copy Propagation**  
   Replace `x = y` by using `y` directly wherever possible.  
   Often turns the copy into **dead code**.

3. **Dead Code Elimination**  
   Remove statements whose result is never used.

   **Example:**
   ```c
   i=0;
   if(i==1) { a=b+5; }   // if is dead code (never true)
   ```

4. **Constant Folding**  
   Evaluate constant expressions at **compile time**.

   **Example:** `a = 3.14157 / 2` → `a = 1.570785`

**Mnemonic for 4 Function-Preserving:**  
**C**ommon **C**opy **D**ead **C**onstant → **CCDC** (See See Dead Constant)

---

#### **B. Loop Optimization** (Mostly Global)

1. **Code Motion (Loop Invariant Code Motion)**  
   Move code that gives **same value** in every iteration **outside** the loop.

   **Example:**
   ``` 
   Before: for(i=1; i<=100; i++) { x=25*a; y=x+z; }
   After:  x=25*a; for(i=1; i<=100; i++) { y=x+z; }
   ```

2. **Induction Variable Elimination**  
   Variables that change in a predictable way inside loop (usually +1 or *constant).

3. **Strength Reduction**  
   Replace expensive operation with cheaper one.

   **Example:**
   - `t4 = 4 * j`  →  `t4 = t4 - 4` (after j = j-1)
   - Multiplication → Addition/Subtraction or Shift

**Mnemonic for Loop Opts:**  
**C**ode **M**otion → **I**nduction **S**trength → **C**ode **M**otion **I**nduction **S**trength (CMIS)

**Extra Loop Techniques:**
- Loop Jamming (merge two loops into one)
- Loop Unrolling (replace loop with repeated statements)

---

### **5. Optimization of Basic Blocks (Local Optimization)**

**Two Types:**
1. **Structure Preserving Transformations**
2. **Algebraic Transformations**

**Structure Preserving (Important ones):**
- Dead code elimination
- Copy propagation (Variable + Constant)
- Common subexpression elimination
- Strength reduction
- Constant folding
- Interchange of independent statements

**Algebraic Transformations:**
- `x + 0 = x`, `x * 1 = x`
- `x**2 → x*x`, `2*x → x+x`

**Mnemonic:**  
**D**ead **C**opy **C**ommon **S**trength **C**onstant **I**nterchange → **DCCSCI**

---

### **6. Directed Acyclic Graph (DAG)**

**Why use DAG?**  
Helps detect **common subexpressions** visually.

**Rules for constructing DAG:**
1. Leaf nodes = identifiers/constants
2. Interior nodes = operators
3. Check if same node (same children + same operator) already exists → reuse it

**Applications of DAG:**
- Find common subexpressions
- Identify live variables
- Simplify quadruples

**Mind Map:**
```
DAG
 ├── Leaf: variables, constants
 ├── Internal: operators
 └── Reuse identical nodes → CSE
```

---

### **7. Machine Dependent Optimization → Peephole Optimization**

**Peephole** = Small window on target code.

**Techniques:**
1. **Redundant Load/Store elimination**  
   `MOV R0, x; MOV x, R0` → remove second
2. **Remove Unreachable Code**
3. **Flow of Control Optimization** (remove unnecessary jumps)
4. **Algebraic Simplifications**
5. **Use Machine Idioms** (INC, auto-increment)

**Mnemonic:**  
**R**edundant **U**nreachable **F**low **A**lgebraic **M**achine → **RUFAM**

---

### **Quick Mind Map for Whole Code Optimization**

```
Code Optimization
   ├── Machine Independent
   │     ├── Function Preserving (CCDC)
   │     └── Loop Optimization (CMIS + Jamming + Unrolling)
   ├── Machine Dependent (Peephole - RUFAM)
   ├── Local  → Basic Block + DAG
   └── Global → Loops + Procedures
```

## Code gen

### 2. Code Generation – Core Concepts (Reverse Engineered)

**What is Code Generation?**  
The **final phase** of the compiler.  
It takes **optimized intermediate code** (usually 3-address code) and produces **target machine code** (assembly or binary) that can run on the actual hardware.

**Goal:** Generate correct, efficient target code (fast + small size).

---

### 3. Issues in the Design of a Code Generator (Most Asked)

**6 Major Issues** (Learn in order):

1. **Input to Code Generator**  
   - Intermediate Representation (3-address code, quadruples, DAG, etc.)  
   - Symbol table information (type, width, address)

2. **Target Program**  
   - Absolute machine code → fixed memory, fast but inflexible  
   - Relocatable machine code → can be linked  
   - Assembly language → easier to generate  
   **Mnemonic:** ARA (Absolute, Relocatable, Assembly)

3. **Memory Management**  
   - Mapping names → addresses (using symbol table width)  
   - Relative addressing for instructions

4. **Instruction Selection**  
   - Choosing best machine instructions for IR statements  
   - Depends on: IR level, nature of instruction set architecture, quality of the generated code .
   **Example:**  
   `x = y + z`  
   Poor: MOV y,R0; ADD z,R0; MOV R0,x  
   Better: Use INC if available

5. **Register Allocation**  
   - Registers are fastest storage  
   - Two sub-problems:  
     - **Register Allocation** → which values stay in registers?  
     - **Register Assignment** → which specific register?  
   **Key Problem:** Limited registers

6. **Evaluation Order**  
   - Order of computing sub-expressions affects register usage  
   - Optimal order is NP-complete → solved partially by optimization

---

### 4. Target Machine (Simple Model used in your notes)

- Byte-addressable, 4 bytes/word  
- n general-purpose registers: R0, R1, ..., Rn-1  
- Two-address instructions: `op source, destination`  
- Important addressing modes (memorize with costs):

| Mode                     | Form          | Added Cost | Mnemonic |
|--------------------------|---------------|------------|----------|
| Register                 | R             | 0          | Free     |
| Absolute                 | M             | 1          | Memory   |
| Indexed                  | c(R)          | 1          | Index    |
| Indirect Register        | *R            | 0          | Indirect |
| Indirect Indexed         | *c(R)         | 1          | Const    |

**Instruction Cost Rule:**  
**Cost = 1 (base) + cost of source + cost of destination**

---

### 5. Simple Code Generator (Most Important for Exams)

#### Tools Used:
- **Register Descriptor**: What is currently in each register?
- **Address Descriptor**: Where is the current value of a name (register/memory)?

### Code Generation Algorithm (Simple Code Generator) – 14 Marks

**Introduction**  
The **simple code generator** converts optimized **three-address intermediate code** (from a basic block) into target machine code (usually assembly). It efficiently uses registers to reduce memory access.  

Two important **data structures** are maintained:  
- **Register Descriptor**: Tells what variables are currently stored in each register (initially all registers are empty).  
- **Address Descriptor**: Tells the current location (register or memory) of each variable/name.

**Main Components**:
- Register & Address Descriptors  
- **getreg()** Function (heart of register allocation)  
- Code Generation Algorithm (step-by-step for each statement `x := y op z`)

#### 1. getreg() Function (Very Important – Explain with Steps)

**Purpose**: Selects a suitable location **L** (preferably a register) to store the result of computation `y op z`.

**Algorithm for getreg(y, z)** (Step-by-Step):

1. **If y is already in a register R** and  
   - R contains **only y** (no other variables), **and**  
   - y has **no next use** in the block (and not live on exit),  
   → **Return R** (reuse the same register). Update address descriptor of y (remove R if needed).

2. **Else**, if there is an **empty (free) register R** available,  
   → **Return that empty register R**.

3. **Else** (no free register), find an **occupied register R** whose variable can be spilled:  
   - Choose R that minimizes the cost (spill the one not used soon).  
   - Generate **store instruction** `MOV R, M` (spill contents to memory) for every memory location M in its address descriptor.  
   → **Return R** (now freed).

4. **If nothing works** (rare), operate directly on **memory location** (no register).

**Key Rule**: Prefer register over memory. Use **next-use information** to decide spilling (this reduces unnecessary load/store).

**Mnemonic for getreg()**:  
**"Reuse → Free → Spill → Memory"** (R-F-S-M)

#### 2. Code Generation Algorithm (Step-by-Step)

**Input**: Sequence of three-address statements in a **basic block**.  
**Output**: Target assembly code.

**For each three-address statement of the form `x := y op z`** (or `x := y` for copy):

1. **Call getreg()** to determine location **L** where the result of `y op z` will be stored. (L is usually a register).

2. **Load y into L** (if not already there):  
   - Consult **address descriptor** of y to find y' (current location of y).  
   - Prefer **register** if y is in both memory and register.  
   - If y is **not already in L**, generate: `MOV y', L`

3. **Perform the operation**:  
   - Find z' (current location of z) from address descriptor.  
   - Prefer **register** over memory if z is in both.  
   - Generate the instruction: `OP z', L`  
     (Example: `ADD R2, R1` if L = R1)

4. **Update descriptors** for the result **x**:  
   - Update **address descriptor** of x → now includes L (and remove x from other locations if needed).  
   - Update **register descriptor** of L → now contains only x.

5. **Free registers if possible** (using next-use info):  
   - If y and/or z have **no further use** in the block and are not live on exit,  
     remove them from their register descriptors (register becomes free for reuse).

**Special Case – Copy Statement `x := y`**:
- Get L = getreg() for x.  
- If y is not in L, generate `MOV y', L`.  
- Update descriptors so both x and y point to L (or make x point only to L).

**At the end of the basic block**:
- For any variable whose value is in a register and needed outside the block (live on exit), generate **store** instruction: `MOV R, M` (store back to memory).

**Example** (Quick to reproduce in exam):  
Consider statements:  
`t1 := a + b`  
`t2 := t1 + c`

Assume registers R0, R1, R2 available.  
- For t1 := a + b → Load a into R0, b into R1, ADD R1, R0 → t1 in R0  
- Update descriptors.  
- For t2 := t1 + c → Reuse R0 (if possible) or use R1, generate ADD, store result.

**Advantages**:
- Simple and efficient for basic blocks.  
- Reduces memory accesses using registers.  
- Uses **next-use** information for smart spilling.

**Disadvantages**:
- Works only within a basic block (local).  
- May generate more spills if registers are limited.

**Related Issues in Code Generation Design** (Add 1-2 lines for extra marks):
- Instruction selection, Register allocation (solved by getreg()), Evaluation order, Memory management, Target language (RISC/CISC/Stack).

**Quick Recall Mnemonic for Whole Algorithm**:  
**G**etreg → **L**oad y → **O**p z → **U**pdate x → **F**ree unused (GLOUF)

---

### 6. Example: Generating Code for Assignment

**Statement:** `d := (a-b) + (a-c) + (a-c)`  
(Assume d is live at end)

**3-Address Code:**
```
t := a - b
u := a - c
v := t + u
d := v + u
```

**Step-by-step Code Generation** (from your PDF):

| Statement       | Code Generated                  | Register Descriptor          | Address Descriptor          |
|-----------------|---------------------------------|------------------------------|-----------------------------|
| (initial)       | -                               | All empty                    | -                           |
| t := a - b      | MOV a, R0<br>SUB b, R0         | R0 = t                       | t in R0                     |
| u := a - c      | MOV a, R1<br>SUB c, R1         | R0=t, R1=u                   | t in R0, u in R1            |
| v := t + u      | ADD R1, R0                     | R0=v, R1=u                   | v in R0, u in R1            |
| d := v + u      | ADD R1, R0<br>MOV R0, d        | R0=d                         | d in R0 (and memory)        |

**Total Cost:** Very efficient (reused R0 cleverly)

---

### 7. Practice Questions Mastery

**Q: Role of Register & Address Descriptor**  
- **Register Descriptor**: Tracks **what value** is in **each register** (updated after every instruction)
- **Address Descriptor**: Tracks **where** the current value of a **variable** is (register or memory)

They work together so the code generator knows whether to generate MOV or not.

---

