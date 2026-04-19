### **1. [2024] Q9: Differentiate local and global optimizations.**

**Local vs Global Optimization** (Easy Comparison Table + Mnemonic)

| Feature                  | **Local Optimization**                          | **Global Optimization**                          |
|--------------------------|--------------------------------------------------|--------------------------------------------------|
| **Scope**                | Inside **one basic block** (straight-line code) | Across multiple blocks, **loops**, procedures, functions |
| **When applied**         | First (before global)                           | After local optimization                         |
| **Techniques**           | Dead code elim, Copy prop, CSE, Constant folding, Strength reduction, Algebraic transforms | Code motion, Induction variable elim, Strength reduction, Loop jamming, Loop unrolling |
| **Complexity**           | Simple & fast                                   | More powerful but complex                        |
| **Example**              | Inside B5 block: remove redundant `x = t3`      | Move `x=25*a` outside for-loop                   |
| **Data Structure**       | DAG inside block                                | Flow Graph (entire program)                      |

**Mnemonic:**  
**L**ocal = **L**imited (one block) → **G**lobal = **G**reat (whole program)  
**Order:** Local **first** → Global **later** (Like cleaning your room before cleaning the whole house)

**Mind Map:**
```
Optimization
   ├── Local (Basic Block) → Structure + Algebraic
   └── Global (Loops + Flow) → Code Motion, Induction, Strength
```

**Key Point to Remember:** Local must be done **before** global.

---

### **2. [2023] Q19: Explain the optimization of basic blocks.**

**Optimization of Basic Blocks** (Local Optimization)

There are **two types**:

1. **Structure Preserving Transformations** (keep the shape of code)
2. **Algebraic Transformations** (use math rules)

#### **Structure Preserving Transformations** (Most Important)
- **Dead Code Elimination** – Remove statements whose result is never used.
- **Copy Propagation** (2 types)
  - Variable Propagation: `x = y` → use `y` directly
  - Constant Propagation: `x = 3` → replace `x` with `3`
- **Common Subexpression Elimination (CSE)**
- **Strength Reduction** – Replace costly op with cheap one (`*2` → `+` or `<<1`)
- **Constant Folding**
- **Interchange of two independent statements**

#### **Algebraic Transformations**
- `x + 0 = x`, `x * 1 = x`, `x - 0 = x`
- `x**2 → x * x`, `2*x → x + x`
- Associative law to expose more CSE: `e = c + d + b` → `e = a + d` (if `a = b + c`)

**Mnemonic for Structure Preserving:**  
**D**ead **C**opy **C**ommon **S**trength **C**onstant **I**nterchange → **DCCSCI**

**How DAG Helps Basic Block Optimization?**  
DAG detects common subexpressions visually. Same operator + same children = reuse node → automatic CSE.

**Mind Map:**
```
Basic Block Optimization
   ├── Structure Preserving (DCCSCI)
   └── Algebraic (x+0, x*1, **2 → * , etc.)
         └── Supported by DAG
```

**Exam Tip:** Always mention **two types** + list techniques under structure preserving + one small example of each.

---

### **3. [2024] Q19: Explain any four principal sources of optimization.**

**Principal Sources of Optimization** (4 Important Ones)

1. **Common Subexpression Elimination (CSE)**  
   Reuse previously computed expression if variables have not changed.  
   **Example:** In QuickSort B5 block, `4*i` computed many times → compute once and reuse.

2. **Copy Propagation**  
   After `f := g`, replace uses of `f` with `g`.  
   **Advantage:** Often creates dead code that can be removed.

3. **Dead Code Elimination**  
   Remove code whose computed value is never used.  
   **Example:** `i=0; if(i==1) a=b+5;` → entire if-block is dead.

4. **Constant Folding**  
   Evaluate constant expressions at compile time.  
   **Example:** `a = 3.14157 / 2` → `a = 1.570785` (no division at runtime).

**Bonus (if you want 5):** Loop optimizations (Code Motion, Strength Reduction).

**Mnemonic:** **C**ommon **C**opy **D**ead **C**onstant → **CCDC**

**Mind Map:**
```
Principal Sources
   ├── Function Preserving
   │     ├── CSE
   │     ├── Copy Propagation
   │     ├── Dead Code
   │     └── Constant Folding
   └── Loop Optimization
```

---

### **4. [2023] Q19: With suitable examples explain the following loop optimization techniques: (i) Code motion (ii) Induction variable elimination and (iii) strength reduction**

**Loop Optimization Techniques** (With Clear Examples)

#### **(i) Code Motion (Loop Invariant Code Motion)**
Move a statement that produces the **same value** in every iteration **outside** the loop.

**Example 1:**
``` 
Before:
for i = 1 to 100 {
   z := 1;
   x := 25 * a;     ← loop invariant
   y := x + z;
}
```
**After:**
``` 
x := 25 * a;        ← moved outside
for i = 1 to 100 {
   z := 1;
   y := x + z;
}
```

**Example 2:** `while (i <= limit-2)` → compute `t = limit-2` once outside.

**Mnemonic:** **Move Invariant Code Out** → **MICO**

#### **(ii) Induction Variable Elimination**
An **induction variable** changes in a predictable way (usually +1 or *constant) inside a loop.

**Example (QuickSort B3 loop):**
``` 
j = j - 1
t4 = 4 * j     ← induction variable (t4 always = 4*j)
```
We can eliminate one by relating them.

#### **(iii) Strength Reduction**
Replace **expensive** operation (multiply, divide) with **cheaper** one (add, subtract, shift).

**Example (from notes – QuickSort):**
``` 
Before: t4 := 4 * j
After:  t4 := t4 - 4     (after j = j-1)
```
Multiplication replaced by subtraction → faster on most machines.

**Another Example:**
- `x = 2 * y` → `x = y + y` or `x = y << 1`

**Full Process (Strength Reduction + Induction Elim):**
1. Identify induction vars (j and t4)
2. Add initialization in B1: `t4 = 4*j`
3. Replace multiply with subtract inside loop
4. Eventually eliminate j if possible

**Mind Map for Loop Opts:**
```
Loop Optimization
   ├── Code Motion → Move invariant out
   ├── Induction Variables → Predictable change
   └── Strength Reduction → * → + / -
```

**Exam Tip:** Draw small before-after code boxes + mention QuickSort example.

---

### **5. [2023] Q10: How the peephole optimization technique makes its role in the compilation Process?**

**Peephole Optimization** (Machine Dependent – Target Code)

**Definition:**  
Simple, effective local improvement on **target code** by looking at a small **window** (peephole) of 2–3 instructions and replacing them with shorter/faster equivalent.

**Role in Compilation:**  
- It is the **last optimization phase** (after machine-independent opts).
- Applied on **target/machine code**.
- Improves **speed** and **size** of final executable.
- Very cheap to implement.

**Techniques (RUFAM Mnemonic):**

1. **Redundant Load/Store**  
   `MOV R0, x; MOV x, R0` → delete second instruction.

2. **Remove Unreachable Code**  
   Code after `return` or impossible branch.

3. **Flow of Control Optimization**  
   Remove unnecessary jumps:  
   `GOTO L1; L1: GOTO L2` → directly `GOTO L2`

4. **Algebraic Simplifications**  
   `x + 0 → x`, `x * 1 → x`

5. **Use of Machine Idioms**  
   Use hardware instructions: `i = i+1` → `INC i` or auto-increment mode.

**Mind Map:**
```
Peephole Optimization
   └── Window on Target Code
         ├── Redundant Load/Store
         ├── Unreachable
         ├── Flow Control
         ├── Algebraic
         └── Machine Idioms
```

**Key Point:** Peephole is **machine-dependent** and works as a final polish on the generated code.

---

### **6. [2022] & [2023] Q19: With suitable examples explain different code optimization techniques.**

**Different Code Optimization Techniques** (Comprehensive Answer)

**Classification:**
- **Machine Independent** vs **Machine Dependent**
- **Local** vs **Global**

**Major Techniques with Examples:**

1. **Common Subexpression Elimination (CSE)** – Function preserving  
2. **Copy Propagation** + **Dead Code Elimination**  
3. **Constant Folding**  
4. **Code Motion** (Loop)  
5. **Strength Reduction** (Loop)  
6. **Peephole Optimization** (Machine dependent)

**Quick Summary Table (use in exam):**

| Technique                  | Type          | Example (Before → After)                     |
|---------------------------|---------------|---------------------------------------------|
| CSE                       | Function      | Reuse `4*i` instead of recomputing          |
| Copy + Dead               | Function      | `x=t3; a[t4]=x` → `a[t4]=t3` (remove x)     |
| Constant Folding          | Function      | `3.14/2` → `1.57`                           |
| Code Motion               | Loop          | Move `x=25*a` outside for-loop              |
| Strength Reduction        | Loop          | `4*j` → `t4 = t4-4`                         |
| Peephole                  | Machine dep   | `MOV R0,x; MOV x,R0` → delete second        |

**Mnemonic:** **C**ommon **C**opy **D**ead **C**onstant **M**otion **S**trength **P**eephole → **CCDC MSP**
