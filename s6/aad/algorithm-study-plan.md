# Algorithm Analysis & Design — KTU Study Plan

> **Exam Pattern:** Part A = Q1–Q10 (3 marks each, no choice) | Part B = Q11–Q20 (14 marks each, with choice)
> Each module maps to 2 Part A questions + 2 Part B pairs (with internal choice).
> 🔴 **Priority = how many years the question appeared in Part B.**

---

## TODAY — Module 1: Introduction to Algorithm Analysis

**KTU Module Mapping:** Q1, Q2 (Part A) | Q11, Q12 (Part B)

---

### 🔴 CRITICAL (Part B — 14 marks) — MUST master today

#### Topic: Asymptotic Notations
**Skill:** `asymptotic-notations-skill`
> Appeared in Part B every year (2022–2025)

| Year | Question |
|------|----------|
| 2022 | Q12: Define Big Oh, Big Omega and Theta notations and illustrate them graphically. |
| 2023 | Q11: Define the asymptotic notations: Big Oh, Big Omega, Theta, little oh and little omega. |
| 2023 | Q11: Define Big Oh, Big Omega and Theta notations and illustrate them graphically. |
| 2024 | Q11: Define the asymptotic notations: Big Oh, Big Omega, Theta and little omega. |
| 2025 | Q11: Give the mathematical definition of any three asymptotic notations. |

**Study checklist:**
- [ ] Define O, Ω, Θ, o, ω formally with constants c, n₀
- [ ] Draw all 5 notation graphs
- [ ] Prove: f(n)=3n³+2n²+3 is O(n³) [2022 Q1]
- [ ] Prove: (n+a)^b = O(n^b) [2023 Q1]
- [ ] Know: is n² ∈ o(n²)? → No (little-o is strict) [2024 Q2]

---

#### Topic: Recurrence Relations & Master Theorem
**Skill:** `solve-the-recurrence-tn-ta---nlogn-skill` + `analysis-of-recursive-algorithms-skill`
> **Highest frequency topic in Module 1 — every exam, both Q11 and Q12**

| Year | Question |
|------|----------|
| 2022 | Q2: Solve T(n)=4(n/4) + n·log(n) using Master Theorem |
| 2022 | Q11: Substitution method — T(n)=2T(n/2)+n |
| 2022 | Q12: Recursion tree — T(n)=T(n/2)+T(n/4)+cn & T(n)=2T(n/2)+n |
| 2023 | Q2: Master Theorem — T(n)=aT(n/2)+n² |
| 2023 | Q2: Master Theorem — T(n)=3T(n/2)+n² and T(n)=2T(n/2)+n·log(n) |
| 2023 | Q11: Recursion tree — T(n)=T(n/2)+1 and T(n)=T(n/3)+n² |
| 2024 | Q2: Master Theorem — T(n)=4T(n/2)+n³ |
| 2024 | Q11: Iteration method — T(n)=2T(n/2)+n |
| 2024 | Q11: Recursion tree — T(n)=2T(n/2)+1 |
| 2024 | Q12: Recursion tree — T(n)=T(n/3)+T(2n/3)+cn |
| 2024 | Q12: Substitution — T(n)=2T(n/2)+cn² |
| 2024 | Q12: Master Theorem — T(n)=2T(n/2)+1 and T(n)=2T(n/2)+n |
| 2025 | Q1: Binary search recurrence → solve with Master Theorem |
| 2025 | Q12: Master Theorem — T(n)=3T(n/3)+n² and T(n)=T(n/4)+1 |
| 2025 | Q11: Recursion tree — T(n)=3T(n/3)+cn·n² |

**Study checklist:**
- [ ] Memorize all 3 cases of Master Theorem (a, b, f(n) comparison to n^log_b(a))
- [ ] Practice: T(n)=2T(n/2)+n → O(n·log n) [case 2]
- [ ] Practice: T(n)=4T(n/2)+n³ → O(n³) [case 3]
- [ ] Practice: T(n)=T(n/3)+T(2n/3)+cn via recursion tree
- [ ] Practice substitution: assume T(n)≤cn·log(n), prove induction

---

#### Topic: Best/Worst/Average Case Complexity
**Skill:** `time-and-space-complexity-skill`

| Year | Question |
|------|----------|
| 2022 | Q11: Best/average/worst case with Insertion Sort |
| 2023 | Q12: Best/worst/average with Linear Search |
| 2023 | Q12: Best/worst/average of Binary Search |
| 2024 | Q12: Best/average/worst case with Insertion Sort |
| 2024 | Q11: Best/worst/average of Linear Search with examples |
| 2025 | Q11: Time complexity using recursion tree |

**Study checklist:**
- [ ] Insertion Sort: best O(n), worst O(n²), average O(n²)
- [ ] Linear Search: best O(1), worst O(n), average O(n/2)
- [ ] Binary Search: best O(1), worst O(log n)
- [ ] Analyze nested loop code segments for complexity

---

### 🟡 MODERATE (Part A — 3 marks)

| Skill | Question to practice |
|-------|----------------------|
| `characteristics-and-analysis-criteria` | [2024 Q1] List characteristics of a good algorithm |
| `asymptotic-notations` | [2023 Q1] Prove f(n)=7n+4 is O(n) |
| `solve-recurrence` | [2025 Q1] Binary search recurrence + Master Theorem |
| `is-n2-o-n2-skill` | [2024 Q2] Is n² ∈ o(n²)? Justify |
| `s-2n1-skill` | [2025 Q2] Is 2^(n+1) = O(2^n)? → Yes, prove |

---

## DAY 2 MORNING — Module 2: Advanced Data Structures & Graph Algorithms

**KTU Module Mapping:** Q3, Q4 (Part A) | Q13, Q14 (Part B)

---

### 🔴 CRITICAL (Part B — 14 marks)

#### Topic: BFS and DFS Graph Traversals
**Skill:** `graph-traversals-and-connectivity-skill`
> Appeared in Q13 or Q14 every single year

| Year | Question |
|------|----------|
| 2022 | Q14: DFS algorithm + time complexity analysis |
| 2022 | Q14: DFS traversal from node A + classify edges |
| 2023 | Q14: BFS algorithm + complexity |
| 2023 | Q14: DFS algorithm + time complexity |
| 2023 | Q14: Strongly connected components of directed graph |
| 2024 | Q13: BFS algorithm + complexity analysis |
| 2024 | Q14: Algorithm for strongly connected components |
| 2024 | Q14: DFS algorithm + edge classification |
| 2024 | Q14: DFS in connected graph + time complexity justification |
| 2024 | Q14: Strongly connected components with example |
| 2025 | Q13: BFS algorithm + time complexity |
| 2025 | Q13: DFS traversal from A + edge classification |
| 2025 | Q14: Topological ordering of given graph |

**Study checklist:**
- [ ] Write BFS pseudocode with queue; derive time O(V+E)
- [ ] Write DFS pseudocode with stack/recursion; derive time O(V+E)
- [ ] Know edge types in DFS: tree, back, forward, cross edges
- [ ] Kosaraju's algorithm for Strongly Connected Components
- [ ] Topological sort via DFS (reverse finishing time)

---

#### Topic: AVL Trees & Self-Balancing
**Skill:** `avl-tree-skill` + `self-balancing-trees-skill`

| Year | Question |
|------|----------|
| 2023 | Q13: Advantages of AVL + all 4 rotation types during insert/delete |
| 2023 | Q14: Insert 54 in Tree1 + Delete 15 from Tree2 |

**Study checklist:**
- [ ] 4 rotations: LL, RR, LR, RL — draw and memorize triggers
- [ ] Balance factor = height(left) − height(right), must be {−1, 0, 1}
- [ ] Trace insert/delete with rebalancing step-by-step

---

#### Topic: Disjoint Sets (Union-Find)
**Skill:** `disjoint-sets-skill`

| Year | Question |
|------|----------|
| 2022 | Q13: Disjoint set operations + connected components |
| 2023 | Q13: Disjoint set operations + connected components of undirected graph |

**Study checklist:**
- [ ] Operations: MAKE-SET, UNION, FIND-SET
- [ ] Union by rank + path compression
- [ ] Use to compute connected components of undirected graph

---

### 🟡 Part A (3 marks)

| Year | Question |
|------|----------|
| 2023 | Q4: Topological ordering of graph |
| 2024 | Q3: Can DFS detect cycles? Justify |
| 2024 | Q4: Topological sort order |
| 2025 | Q3: Define strongly connected component + example |

---

## DAY 2 AFTERNOON — Module 3: Divide & Conquer and Greedy Strategy

**KTU Module Mapping:** Q5, Q6 (Part A) | Q15, Q16 (Part B)

---

### 🔴 CRITICAL (Part B — 14 marks)

#### Topic: Dijkstra's Shortest Path + Kruskal's MST
**Skill:** `apply-dijkstras-algorithm-skill`
> Both appear together as Q15/Q16 every year — one is Dijkstra, the other Kruskal

| Year | Question |
|------|----------|
| 2022 | Q15: Dijkstra from node A on given graph |
| 2022 | Q16: Kruskal for minimum cost spanning tree |
| 2023 | Q15: Kruskal's MST algorithm + apply to graph |
| 2023 | Q16: Dijkstra's algorithm + complexity analysis |
| 2023 | Q16: Kruskal's for MST on graph |
| 2023 | Q16: Dijkstra from vertex A to all others |
| 2024 | Q15: Dijkstra on given graph (from vertex 1) |
| 2024 | Q15: Kruskal's MST + time complexity justification |
| 2024 | Q16: Dijkstra's algorithm + complexity |
| 2025 | Q15: Kruskal's MST algorithm + complexity |
| 2025 | Q16: Dijkstra's algorithm for shortest path from given vertex |

**Study checklist:**
- [ ] Dijkstra: greedy, uses min-priority queue, O((V+E)·log V)
- [ ] Trace Dijkstra step-by-step on a 5-6 node graph
- [ ] Kruskal: sort edges by weight, use Union-Find, O(E·log E)
- [ ] Trace Kruskal on a 6-7 node graph

---

#### Topic: Fractional Knapsack (Greedy)
**Skill:** `greedy-strategy-skill` + `find-an-optimal-solution-fractional-knapsack-skill`
> Appears in Q15 or Q16 almost every year (with Dijkstra as the other choice)

| Year | Question |
|------|----------|
| 2022 | Q16: Fractional Knapsack — 3 items, capacity=20, weights/profits given |
| 2023 | Q6: Fractional Knapsack — capacity=15, 3 items |
| 2023 | Q15: Fractional Knapsack — n=7, capacity=15 |
| 2023 | Q16: Greedy control abstraction for knapsack |
| 2024 | Q15: Greedy control abstraction + fractional knapsack algorithm |
| 2024 | Q16: Fractional knapsack — n=5, capacity=10 (profits & weights given) |
| 2024 | Q16: Fractional knapsack — 3 objects, capacity=20 |
| 2024 | Q16: Greedy control abstraction |
| 2025 | Q15: Fractional knapsack — n=7, capacity=15 |
| 2025 | Q6: Greedy control abstraction |

**Study checklist:**
- [ ] Greedy: sort by profit/weight ratio descending
- [ ] Take fractions of last item if needed
- [ ] Memorize control abstraction (pseudocode)
- [ ] Practice on n=5, M=10, p=(3,2,1,0,9), w=(5,1,0,3,4) type inputs

---

#### Topic: Divide & Conquer — Merge Sort + Strassen
**Skill:** `divide-and-conquer-strategy-skill` + `strassens-matrix-multiplication-skill`

| Year | Question |
|------|----------|
| 2022 | Q6: Why Strassen > naive D&C? Recurrence for steps? |
| 2022 | Q15: 2-way merge sort on [15,12,14,17,11,13,12,16] + recurrence + complexity |
| 2023 | Q5: Control abstraction of D&C |
| 2023 | Q6: Compare Strassen vs ordinary matrix multiplication |
| 2023 | Q15: D&C merge sort algorithm + complexity |
| 2024 | Q5: Strassen when n is not a power of 2? |
| 2024 | Q15: 2-way merge sort on [15,12,14,17,11,13,12,16] + complexity |
| 2025 | Q5: Compare Strassen vs ordinary — which is faster? |
| 2025 | Q16: D&C 2-way merge sort + time complexity |

**Study checklist:**
- [ ] Merge sort recurrence: T(n)=2T(n/2)+n → O(n·log n)
- [ ] Trace merge sort on [15,12,14,17,11,13,12,16]
- [ ] Strassen: 7 multiplications vs 8; T(n)=7T(n/2)+O(n²) → O(n^2.81)
- [ ] Explain padding strategy when n is not a power of 2

---

## DAY 3 MORNING — Module 4: Dynamic Programming, Backtracking & Branch and Bound

**KTU Module Mapping:** Q7, Q8 (Part A) | Q17, Q18 (Part B)

---

### 🔴 CRITICAL (Part B — 14 marks)

#### Topic: Matrix Chain Multiplication (DP)
**Skill:** `find-the-optimal-parenthesis-skill` + `dynamic-programming-skill`
> Appears in Q17 or Q18 every year — most numerical DP question

| Year | Question |
|------|----------|
| 2022 | Q18: MCM as DP example with elements |
| 2023 | Q17: MCM for 4 matrices 5×4, 4×6, 6×2, 2×7 |
| 2023 | Q18: MCM for A,B,C,D (4 matrices given) |
| 2024 | Q7: Recurrence for number of parenthesizations |
| 2024 | Q17: MCM for 4×10, 10×3, 3×12, 12×20, 20×7 |
| 2024 | Q17: MCM for ⟨5×4, 4×6, 6×2, 2×7⟩ |
| 2025 | Q8: Recursive definition for minimum cost |
| 2025 | Q17: MCM for ⟨5×6, 6×4, 4×8, 8×10⟩ |

**Study checklist:**
- [ ] Recurrence: m[i,j] = min over k of {m[i,k] + m[k+1,j] + p[i-1]·p[k]·p[j]}
- [ ] Fill DP table bottom-up (chain length 2 → 3 → n)
- [ ] Reconstruct optimal parenthesization from s-table
- [ ] Practice the "5×4, 4×6, 6×2, 2×7" standard example from scratch

---

#### Topic: Floyd-Warshall (All-Pairs Shortest Path)
**Skill:** `floyd-warshall-algorithm-skill`

| Year | Question |
|------|----------|
| 2022 | Q17: Floyd-Warshall + solve an instance |
| 2023 | Q17: Floyd-Warshall algorithm + complexity |
| 2023 | Q18: Floyd-Warshall algorithm for all-pairs |
| 2024 | Q18: Explain + find all-pair shortest paths |
| 2024 | Q18: Construct D² matrix using Floyd-Warshall on given graph |
| 2025 | Q17: Apply Floyd-Warshall on given directed weighted graph |

**Study checklist:**
- [ ] Triple nested loop: for k, for i, for j: D[i][j] = min(D[i][j], D[i][k]+D[k][j])
- [ ] Time complexity O(n³), space O(n²)
- [ ] Trace the D⁰→D¹→D²→…→Dⁿ matrices on a 4-node graph

---

#### Topic: Backtracking vs Branch & Bound (TSP + N-Queens)
**Skill:** `backtracking-skill` + `branch-and-bound-skill`

| Year | Question |
|------|----------|
| 2022 | Q8: Differentiate backtracking vs B&B |
| 2023 | Q8: Distinguish B&B from backtracking |
| 2023 | Q7: Differentiate backtracking from B&B |
| 2023 | Q17: TSP using Branch & Bound (cost matrix given) |
| 2023 | Q17: 4-Queens state space tree (backtracking) |
| 2023 | Q18: TSP using B&B |
| 2024 | Q8: Differences between Backtracking and B&B (3 differences) |
| 2024 | Q17: TSP using Branch & Bound |
| 2024 | Q18: 4-Queens state space diagram using backtracking |
| 2024 | Q8: Define TSP |
| 2025 | Q17: Floyd-Warshall / TSP minimum tour |

**Study checklist:**
- [ ] Backtracking: DFS, prune when constraint violated, no bound
- [ ] Branch & Bound: uses cost/bound function, eliminates infeasible nodes early
- [ ] 4-Queens: draw the complete state space tree (4 levels deep)
- [ ] TSP B&B: reduced cost matrix → lower bound calculation

---

### 🟡 Part A (3 marks)

| Year | Question |
|------|----------|
| 2022 | Q7: Elements of dynamic programming |
| 2023 | Q8: What is Principle of Optimality? |
| 2024 | Q7: Steps to solve a problem using DP |
| 2025 | Q7: Desirable characteristics for DP |

---

## DAY 3 AFTERNOON — Module 5: Introduction to Complexity Theory

**KTU Module Mapping:** Q9, Q10 (Part A) | Q19, Q20 (Part B)

---

### 🔴 CRITICAL (Part B — 14 marks)

#### Topic: Randomized Algorithms (Randomized QuickSort)
**Skill:** `randomized-algorithms-skill`
> **Highest frequency Module 5 Part B topic — appeared 4 years in a row**

| Year | Question |
|------|----------|
| 2022 | Q19: Randomized QuickSort + expected running time analysis |
| 2022 | Q20: Advantages over deterministic + Las Vegas vs Monte Carlo |
| 2023 | Q19: Benefits of randomized + Las Vegas vs Monte Carlo categories |
| 2023 | Q20: Randomized QuickSort + expected running time |
| 2023 | Q20: Randomized QuickSort with examples |
| 2024 | Q19: Advantages over deterministic + Las Vegas vs Monte Carlo |
| 2024 | Q19: Randomized QuickSort + expected running time |
| 2024 | Q19: Prove expected comparisons = O(n·log₂n) |
| 2025 | Q20: Randomized QuickSort + expected running time |

**Study checklist:**
- [ ] Randomized QS: swap A[r] with random element before partition
- [ ] Expected time analysis: E[X] = Σᵢ Σⱼ Pr(Aᵢ compared with Aⱼ) = O(n·log n)
- [ ] Las Vegas: always correct, random runtime (e.g., Randomized QS)
- [ ] Monte Carlo: always fast, possibly incorrect (e.g., Miller-Rabin primality)
- [ ] Advantages: avoids adversarial worst-case, simple implementation

---

#### Topic: NP-Completeness Proofs (CLIQUE + Vertex Cover)
**Skill:** `np-completeness-proofs-skill` + `graph-coloring-problem-skill`

| Year | Question |
|------|----------|
| 2022 | Q19: Prove CLIQUE is NP-Complete |
| 2023 | Q19: Prove Clique Decision problem is NP-Complete |
| 2023 | Q20: Prove Vertex Cover is NP-Complete |
| 2024 | Q19: Prove Clique decision version is in NP |
| 2024 | Q20: Prove Vertex Cover decision version is NP-Hard |
| 2024 | Q20: Prove Vertex Cover is NP-Complete |
| 2025 | Q19: Prove CLIQUE is NP-Complete |

**Study checklist:**
- [ ] NP-completeness proof structure: (1) show in NP → polynomial verifier; (2) show NP-Hard → reduce known NPC to it
- [ ] CLIQUE: show it's in NP (verify k-clique in poly time); reduce 3-SAT → CLIQUE
- [ ] Vertex Cover: complement of CLIQUE (k-clique in G ↔ (n−k) vertex cover in G̅)
- [ ] Know the reduction diagram by heart

---

#### Topic: Approximation Algorithms (Bin Packing)
**Skill:** `approximation-algorithms-skill`

| Year | Question |
|------|----------|
| 2022 | Q20: Bin packing with First Fit heuristic + approximation ratio |
| 2023 | Q19: Bin packing + First Fit strategy + approximation ratio |
| 2023 | Q19: First Fit Decreasing strategy |
| 2024 | Q20: Bin packing + First Fit + approximation ratio |
| 2024 | Q20: First Fit heuristic + approximation ratio |
| 2025 | Q19: Approximation ratio + PTAS + FPTAS definitions |
| 2025 | Q20: Bin Packing + First Fit strategy |

**Study checklist:**
- [ ] First Fit: place item in first bin where it fits; ratio ≤ 17/10 = 1.7
- [ ] First Fit Decreasing: sort items desc first; better ratio ≤ 11/9 OPT + 6/9
- [ ] Define approximation ratio ρ(n): C/C* ≤ ρ(n)
- [ ] PTAS: (1+ε)-approximation for any fixed ε in poly time
- [ ] FPTAS: poly in both n and 1/ε

---

### 🟡 Part A (3 marks)

| Year | Question |
|------|----------|
| 2022 | Q9: Define P, NP and NP-Complete domains |
| 2022 | Q10: Compare Las Vegas and Monte Carlo |
| 2023 | Q9: Differentiate P and NP, one example each |
| 2023 | Q10: Define graph coloring problem |
| 2024 | Q9: Define optimization + decision version of CLIQUE |
| 2024 | Q10: Compare Las Vegas vs Monte Carlo |
| 2025 | Q9: Define P, NP and NP-Hard |
| 2025 | Q10: Compare Las Vegas and Monte Carlo |

---

## Overall Priority Matrix

| Priority | Topic | Module | Frequency |
|----------|-------|--------|-----------|
| 🔴🔴🔴 | Recurrence Relations (Master Theorem + Recursion Tree + Substitution) | M1 | Every year Q11+Q12 |
| 🔴🔴🔴 | Randomized QuickSort expected analysis | M5 | Every year Q19+Q20 |
| 🔴🔴🔴 | Matrix Chain Multiplication (DP) | M4 | Every year Q17/Q18 |
| 🔴🔴 | Dijkstra + Kruskal | M3 | Every year Q15/Q16 |
| 🔴🔴 | BFS + DFS + SCC | M2 | Every year Q13/Q14 |
| 🔴🔴 | NP-Completeness (CLIQUE + Vertex Cover) | M5 | Every year Q19/Q20 |
| 🔴🔴 | Floyd-Warshall | M4 | Every year Q17/Q18 |
| 🔴🔴 | Asymptotic Notations (formal definitions + proofs) | M1 | Every year Q11/Q12 |
| 🔴 | Backtracking vs B&B (TSP, 4-Queens) | M4 | Every year Q17/Q18 |
| 🔴 | Fractional Knapsack + Greedy abstraction | M3 | Every year Q15/Q16 |
| 🟡 | Merge Sort D&C + Strassen's | M3 | Every year Q15 |
| 🟡 | AVL Trees + Disjoint Sets | M2 | Less frequent |
| 🟡 | Bin Packing approximation | M5 | Every year Q19/Q20 |
| 🟢 | P/NP/NP-Hard definitions | M5 | Part A only (3 marks) |
| 🟢 | Algorithm characteristics | M1 | Part A only (3 marks) |
