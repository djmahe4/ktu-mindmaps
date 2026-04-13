# Comp

Here is a **module-wise complexity cheatsheet** designed for easy memorization. It uses concise tables, mnemonics, and simple tips to help you recall key concepts and time/space complexities from the KTU CST306 (Algorithm Analysis and Design) syllabus.

### Module 1: Introduction to Algorithm Analysis
**Core Focus**: Characteristics of algorithms, time & space complexity (best/worst/average), asymptotic notations, and solving recurrences.

**Mnemonic for Notations**:
- **O** (Big-Oh) → **Upper bound** (Worst-case ceiling, "Oh no, maximum time!").
- **Ω** (Big-Omega) → **Lower bound** (Best-case floor, "Omega – at least this much").
- **Θ** (Big-Theta) → **Tight bound** (Average-case sandwich, "Theta – exactly between both").
- **o** (little-oh) → Strictly smaller than O (grows slower).
- **ω** (little-omega) → Strictly larger than Ω (grows faster).

**Easy Tip**: Think of O as "overestimate (worst)", Ω as "underestimate (best)", and Θ as "tight/average".

#### Asymptotic Notations Summary Table

| Notation       | Meaning                          | Represents          | Example Usage                  | Easy Tip to Remember                  |
|----------------|----------------------------------|---------------------|--------------------------------|---------------------------------------|
| **O(g(n))**   | Upper bound                     | Worst-case         | O(n²) for Insertion Sort      | "Oh – maximum possible time"         |
| **Ω(g(n))**   | Lower bound                     | Best-case          | Ω(n) for Linear Search        | "Omega – at least this much"         |
| **Θ(g(n))**   | Tight bound                     | Average-case       | Θ(n log n) for Merge Sort     | "Theta – sandwiched exactly"         |
| **o(g(n))**   | Strict upper bound              | Much slower        | n = o(n²)                     | "Little o – strictly slower"         |
| **ω(g(n))**   | Strict lower bound              | Much faster        | n² = ω(n)                     | "Little omega – strictly faster"     |

**Properties Tip**: O ignores constants & lower terms (e.g., 5n² + 3n → O(n²)). Classify growth: 1 < log n < n < n log n < n² < n³ < 2ⁿ < n!.

#### Recurrence Solving Quick Tips (Master Theorem – No Proof Needed)
**Form**: T(n) = a T(n/b) + f(n), a ≥ 1, b > 1.

**Three Cases (Easy Mnemonic: Compare f(n) with n^{log_b a})**:
1. If f(n) grows **slower** than n^{log_b a} → T(n) = Θ(n^{log_b a})  
   (Subproblems dominate)
2. If f(n) grows **same** as n^{log_b a} (with log factor) → T(n) = Θ(n^{log_b a} log^k n)  
   (Balanced)
3. If f(n) grows **faster** than n^{log_b a} → T(n) = Θ(f(n))  
   (Merge/combine dominates)

**Examples to Memorize**:
- Merge Sort: T(n) = 2T(n/2) + O(n) → **Θ(n log n)** (Case 2)
- Binary Search: T(n) = T(n/2) + O(1) → **Θ(log n)** (Case 1)

**Space Complexity Tip**: Usually O(1) for iterative; O(depth) for recursion (e.g., O(n) stack in linear recursion).

### Module 2: Advanced Data Structures and Graph Algorithms

**Key Tip**: Self-balancing ensures logarithmic height.

#### Complexity Table – Module 2

| Algorithm / Operation              | Time Complexity                  | Space Complexity | Easy Mnemonic / Tip                          |
|------------------------------------|----------------------------------|------------------|----------------------------------------------|
| AVL Tree (Insert/Delete/Search)   | O(log n) worst & average        | O(n)            | "AVL Always Log" (rotations keep balance)   |
| Disjoint Set (Union-Find) with Path Compression + Union by Rank | Amortized **O(α(n))** ≈ O(1)   | O(n)            | "Almost Constant" (α(n) grows very slowly) |
| DFS / BFS Traversal               | O(V + E)                        | O(V)            | "Visit every Vertex + Edge once"            |
| Strongly Connected Components (DFS-based) | O(V + E)                   | O(V)            | Same as DFS                                 |
| Topological Sorting (DFS/Kahn)    | O(V + E)                        | O(V)            | "Only on DAGs"                              |

**Tip**: For graphs, adjacency list is efficient → O(V + E) is standard.

### Module 3: Divide & Conquer and Greedy Strategy

**Divide & Conquer Tip**: Break → Solve → Combine (recurrence often solved by Master Theorem).

**Greedy Tip**: Always pick local optimum (works for fractional knapsack, MST, shortest path).

#### Complexity Table – Module 3

| Algorithm                          | Time Complexity                  | Easy Tip / Mnemonic                          |
|------------------------------------|----------------------------------|----------------------------------------------|
| Merge Sort (2-way)                 | Θ(n log n)                      | "Divide & Conquer Classic – n log n"        |
| Strassen’s Matrix Multiplication   | O(n^{2.807}) ≈ O(n^{log_2 7})   | "Faster than O(n³) by clever divide"        |
| Fractional Knapsack (Greedy)       | O(n log n)                      | "Sort by value/weight ratio"                |
| Kruskal’s MST                      | O(E log E) or O(E log V)        | "Sort edges + Union-Find"                   |
| Dijkstra’s Single-Source Shortest Path | O((V + E) log V) with heap   | "Priority queue for greedy choice"          |

### Module 4: Dynamic Programming, Backtracking, and Branch & Bound

**DP Tip**: Optimality Principle + Overlapping subproblems + Tabulation/Memoization (usually polynomial).

**Backtracking/Branch & Bound Tip**: Exponential in worst case (pruning helps).

#### Complexity Table – Module 4

| Algorithm                          | Time Complexity                          | Easy Tip / Mnemonic                          |
|------------------------------------|------------------------------------------|----------------------------------------------|
| Matrix Chain Multiplication (DP)   | O(n³)                                   | "Three nested loops for optimal parenthesization" |
| Floyd-Warshall (All-Pairs Shortest Path) | Θ(n³)                              | "Triple loop – dynamic programming on paths" |
| N-Queens (Backtracking)            | O(n!) worst-case                        | "Exponential – try & backtrack"             |
| Travelling Salesman (Branch & Bound) | O(n² 2ⁿ) or better with pruning      | "Explores state space with bounding"        |

**Space Tip for DP**: Usually O(n²) table for 2D problems like Matrix Chain or Floyd-Warshall.

### Module 5: Introduction to Complexity Theory

**Key Concepts**:
- **Tractable**: Solvable in polynomial time → **P** class.
- **Intractable**: Not solvable in polynomial time.
- **NP**: Verifiable in polynomial time (nondeterministic).
- **NP-hard / NP-complete**: Hardest problems in NP (e.g., Clique, Vertex Cover).

**Easy Mnemonic**:
- **P** → Polynomial (easy, tractable).
- **NP** → Nondeterministic Polynomial (guess + verify quickly).
- **NP-complete** → If one is solved in P, all NP problems are in P.

**Approximation & Randomized Algorithms**:
- Bin Packing, Graph Colouring → Approximation algorithms (no exact poly-time solution).
- Randomized Quicksort → Average **O(n log n)**, worst O(n²) but unlikely with random pivot (Las Vegas / Monte Carlo types).

**Tip to Remember**: Clique and Vertex Cover are classic **NP-complete** problems. Randomized algorithms trade determinism for better average performance.

### General Memorization Tips Across Modules
1. **Worst-case is default** unless specified (use O for guarantees).
2. **Log n** appears in divide-and-conquer or balanced trees.
3. **n log n** is the sweet spot for sorting/comparison-based algorithms.
4. **n² or n³** → Polynomial but slow for large n (common in DP/graph).
5. **Exponential (2ⁿ, n!)** → Only for small n or with heavy pruning.
6. **Practice Rule**: For any code → Count loops (single → O(n), nested → O(n²), multiplicative → O(log n)).

Review these tables daily. Focus on Module 1 first (foundational), then link complexities to specific algorithms in later modules. For example, "AVL = log n, Kruskal = E log E, Floyd = n³".

If you need expanded explanations, practice questions with step-by-step solutions, or a Mermaid decision tree combining these, let me know. This structured format should help you grasp and retain the concepts efficiently for exams.
