The user wants concise, understandable notes using Mermaid diagrams for quick grasping. I'll go through each question and provide a suitable Mermaid diagram and a brief explanation.

---

### **PART - A**

#### 1. Explain Strassen's matrix multiplication.
Strassen's algorithm is a divide-and-conquer algorithm for matrix multiplication that reduces the number of recursive multiplications from 8 to 7, improving time complexity from O(n³) to O(n^log₂(7)) ≈ O(n^2.81).

<summary>
<details>
<summary>View Diagram</summary>

```mermaid
graph TD
    A[Start: Multiply A * B] --> B{Divide A, B into<br/>n/2 x n/2 sub-matrices}
    B --> C{Compute 7 intermediate<br/>products M1-M7 recursively}
    C --> D{Combine M1-M7 with<br/>additions/subtractions}
    D --> E[End: Resulting matrix C]
```

</details>
</summary>

#### 2. Write the control abstraction of greedy strategy to solve a problem.
A greedy algorithm makes the locally optimal choice at each step with the hope that this choice will lead to a globally optimal solution.

<summary>
<details>
<summary>View Diagram</summary>

```mermaid
graph TD
    A[Start] --> B(Initialize Solution)
    B --> C{While problem not solved<br/>and choices available?}
    C -- Yes --> D{Select best local choice}
    D --> E{Check if choice<br/>is feasible}
    E -- Yes --> F{Add choice to Solution}
    E -- No --> G{Discard choice}
    G --> C
    F --> C
    C -- No --> H[End: Return Solution]
```

</details>
</summary>

#### 3. List out the main steps involved in solving a computational problem using the algorithm design strategy in dynamic programming.
Dynamic programming solves complex problems by breaking them into overlapping subproblems, solving each subproblem only once, and storing the solutions.

<summary>
<details>
<summary>View Diagram</summary>

```mermaid
graph TD
    A[Start] --> B(Characterize optimal solution structure)
    B --> C(Define recurrence relation)
    C --> D(Compute values bottom-up or via memoization)
    D --> E(Construct optimal solution from computed info)
    E --> F[End]
```

</details>
</summary>

#### 4. Define the control abstraction for Backtracking.
Backtracking is a general algorithmic technique for finding all (or some) solutions to a computational problem, especially constraint satisfaction problems, by incrementally building candidates to the solutions and abandoning a candidate ("backtracking") as soon as it determines that the candidate cannot possibly be completed to a valid solution.

<summary>
<details>
<summary>View Diagram</summary>

```mermaid
graph TD
    A[Start: Solve path] --> B{Is path a solution?}
    B -- Yes --> C[Add path to solutions]
    B -- No --> D{For each choice 'c'<br/>from current state:}
    D --> E{Add 'c' to path}
    E --> F{Is path feasible?}
    F -- Yes --> A
    F -- No --> G{Remove 'c' from path<br/>backtrack}
    G --> D
    D --> H[End]
```

</details>
</summary>

#### 5. Write the control abstraction for Divide and Conquer strategy for solving a problem.
Divide and Conquer is an algorithmic paradigm that recursively breaks down a problem into two or more sub-problems of the same or related type, until these become simple enough to be solved directly. The solutions to the sub-problems are then combined to give a solution to the original problem.

<summary>
<details>
<summary>View Diagram</summary>

```mermaid
graph TD
    A[Start: Solve Problem] --> B{Is Problem<br/>small enough?}
    B -- Yes --> C[Solve directly]
    B -- No --> D(Divide Problem into sub-problems)
    D --> E(Recursively Solve P1)
    D --> F(Recursively Solve P2)
    E --> G(Combine solutions)
    F --> G
    G --> H[End: Return Combined Solution]
```

</details>
</summary>

#### 6. Analyze the time complexity of Strassen's multiplication.
The time complexity of Strassen's matrix multiplication algorithm is O(n^log₂(7)), which is approximately O(n^2.81). This is an improvement over the brute-force O(n³) algorithm.

<summary>
<details>
<summary>View Diagram</summary>

```mermaid
graph TD
    A[Start] --> B(List all edges and weights)
    B --> C(Sort edges ascending by weight)
    C --> D{Check next edge u,v}
    
    D -- "No Cycle" --> E[Add to MST & Union Sets]
    D -- "Forms Cycle" --> F[Discard Edge]
    
    E --> G{V-1 edges found?}
    F --> G
    
    G -- No --> D
    G -- Yes --> H[End]

```

</details>
</summary>

#### 7. Draw the State space tree of 4 queens' problem.
The 4-Queens problem state-space tree represents all possible placements of queens on a 4x4 chessboard. Each level corresponds to placing a queen in a row, and branches represent valid column choices. (A full 4-queens tree is too large for a concise diagram, so a conceptual structure is provided.)

<summary>
<details>
<summary>View Diagram</summary>

```mermaid
graph TD
    A[Root: Empty Board] --> B1[Q1 at 1,1]
    A --> B2[Q1 at 1,2]
    A --> B3[Q1 at 1,3]
    A --> B4[Q1 at 1,4]
    B1 --> C1[Q2 at 2,x - valid]
    B1 --> C2[Q2 at 2,y - invalid]
    C1 --> D1[Q3 at 3,z - valid]
    D1 --> E1[Q4 - solution/conflict]
```

</details>
</summary>

#### 8. Compare backtracking and branch and bound design techniques.
Backtracking and Branch and Bound are both state-space search techniques. Backtracking finds all (or any) feasible solutions and typically uses Depth-First Search (DFS) with a feasibility function. Branch and Bound finds the optimal solution, can use DFS or Breadth-First Search (BFS), and employs a bounding function to prune unpromising branches.

<summary>
<details>
<summary>View Diagram</summary>

```mermaid
graph TD
    subgraph BT [Backtracking]
        BT1(Start) --> BT2{Explore DFS}
        BT2 --> BT3{Feasible?}
        BT3 -- No --> BT4(Backtrack)
        BT4 --> BT2
        BT3 -- Yes --> BT5{Solution?}
        BT5 -- No --> BT2
        BT5 -- Yes --> BT6(End)
    end

    subgraph BB [Branch and Bound]
        BB1(Start) --> BB2{Explore DFS/BFS}
        BB2 --> BB3{Compute Bound}
        BB3 --> BB4{Prune if worse<br/>than best?}
        BB4 -- Yes --> BB5(Discard)
        BB5 --> BB2
        BB4 -- No --> BB6{Optimal?}
        BB6 -- No --> BB2
        BB6 -- Yes --> BB7(End)
    end
```

</details>
</summary>

---

### **PART - B - Module 3**

#### 5. Fractional Knapsack problem.
The Fractional Knapsack problem is solved using a greedy approach by prioritizing items with the highest profit-to-weight ratio.

<summary>
<details>
<summary>View Diagram</summary>

```mermaid
graph TD
    A[Start] --> B(Calculate Profit/Weight Ratios)
    B --> C(Sort items descending by ratio)
    C --> D{For each item:}
    D -- Fits --> E[Take whole item]
    D -- Doesn't fit --> F[Take fraction to fill capacity]
    E --> G{Capacity left?}
    G -- Yes --> D
    G -- No --> H[End: Return Total Profit]
    F --> H
```

</details>
</summary>

#### 6. Compute the Minimum Spanning Tree and its cost for the following graph using Kruskal's Algorithm. Indicate each step clearly. Find the complexity.
Kruskal's Algorithm is a greedy algorithm that finds a Minimum Spanning Tree (MST) for a weighted undirected graph. It sorts all edges by weight and adds the smallest-weight edges that do not form a cycle.
The complexity of Kruskal's algorithm is O(E log E) or O(E log V), where E is the number of edges and V is the number of vertices, primarily due to sorting the edges.

<summary>
<details>
<summary>View Diagram</summary>

```mermaid
graph TD
    A[Start] --> B(List all edges and weights)
    B --> C(Sort edges ascending by weight)
    C --> D{Check next edge u,v}
    
    D -- "No" --> E[Add to MST & Union Sets]
    D -- "Yes" --> F[Discard Edge]
    
    E --> G{"V-1 edges found?"}
    F --> G
    
    G -- No --> D
    G -- Yes --> H[End]

```

</details>
</summary>

#### 7. Explain 2-way merge sort algorithm using divide and conquer strategy and analyze its complexity.
Merge Sort is a divide-and-conquer sorting algorithm. It recursively divides an array into two halves, sorts them, and then merges the sorted halves. Its time complexity is O(n log n) in all cases.

<summary>
<details>
<summary>View Diagram</summary>

```mermaid
graph TD
    A[Start] --> B{Size <= 1?}
    B -- No --> C[Split Array into Mid]
    C --> D[Recursively Sort Left]
    C --> E[Recursively Sort Right]
    D --> F[Merge Sorted Halves]
    E --> F
    F --> G[Return Result]
    B -- Yes --> G
```

</details>
</summary>

#### 8. Using Dijkstra's algorithm, find the shortest distance from source vertex ‘S' to remaining vertices in the following graph. Also write the order of visit.
Dijkstra's algorithm finds the shortest paths from a single source vertex to all other vertices in a weighted graph with non-negative edge weights.

<summary>
<details>
<summary>View Diagram</summary>

```mermaid
graph TD
    A[Start] --> B(Set all distances to infinity, source to 0)
    B --> C{Priority Queue empty?}
    C -- No --> D[Extract min distance node u]
    D --> E{For each neighbor v:}
    E --> F{dist u + weight < dist v?}
    F -- Yes --> G[Update dist v]
    G --> E
    F -- No --> E
    E --> C
    C -- Yes --> H[End]
```

</details>
</summary>

---

### **PART - B - Module 4**

#### 9. Write the greedy Knapsack algorithm and solve the given instance of 0/1 Knapsack problem using Dynamic Programming.
The 0/1 Knapsack problem is solved using dynamic programming because items cannot be broken (0 or 1, take or leave). A greedy approach is not optimal for 0/1 Knapsack. The dynamic programming approach typically involves building a table `K[i][w]` representing the maximum profit for `i` items with a knapsack capacity of `w`.

<summary>
<details>
<summary>View Diagram</summary>

```mermaid
graph TD
    A[Start] --> B(Create DP Table K item, weight)
    B --> C{Loop through items i and weights w}
    C --> D{weight i <= w?}
    D -- Yes --> E[K i,w = Max of skip or take]
    D -- No --> F[K i,w = skip item]
    E --> C
    F --> C
    C --> G[End: Max Profit = K n,W]
```

</details>
</summary>

#### 11. Construct the weight adjacency matrix of the given graph. Apply the Floyd Warshall algorithm to construct the matrix D2 that represents the shortest paths distance between all vertices i and j (1 <= i <= 5 and 1 <= j <= 5) through intermediate vertices 1 and 2.
The Floyd-Warshall algorithm finds the shortest paths between all pairs of vertices in a weighted graph. It works by iteratively improving estimates for shortest paths by considering intermediate vertices.

<summary>
<details>
<summary>View Diagram</summary>

```mermaid
graph TD
    A[Start] --> B(Initialize D0 from Adjacency Matrix)
    B --> C{Loop k: 1 to V<br/>Intermediate node}
    C --> D{Loop i: 1 to V<br/>Source node}
    D --> E{Loop j: 1 to V<br/>Target node}
    E --> F[Dk i,j = min Dk-1 i,j, Dk-1 i,k + Dk-1 k,j]
    F --> E
    E --> D
    D --> C
    C --> G[End: Final Distance Matrix DV]
```

</details>
</summary>

#### 12. Define Travelling Salesman Problem (TSP). Apply branch and bound technique to solve the following instance of TSP. Assume the starting vertex as A. Draw the state space tree for each step.
The Travelling Salesman Problem (TSP) asks for the shortest possible route that visits each city exactly once and returns to the origin city. Branch and Bound is an optimization technique that explores a state-space tree, using bounding functions to prune branches that cannot lead to an optimal solution.

<summary>
<details>
<summary>View Diagram</summary>

```mermaid
graph TD
    A[Start] --> B(Initialize best cost = infinity)
    B --> C[Extract node with lowest bound]
    C --> D{Bound < best cost?}
    D -- Yes --> E{Is complete tour?}
    E -- Yes --> F[Update best cost if lower]
    E -- No --> G[Generate children & add to Queue]
    G --> C
    D -- No --> H[Prune branch]
    H --> C
```

</details>
</summary>

---

### **PART - B - Module 5**

#### 13. Given matrices A1, A2, A3 and A4 of order 5x6, 6x4, 4x2, and 2x3 respectively. Compute M using matrix chain multiplication algorithm. Also write the optimal parenthesis.
Matrix Chain Multiplication is a dynamic programming problem that finds the most efficient way to multiply a given sequence of matrices. The goal is to minimize the total number of scalar multiplications.

<summary>
<details>
<summary>View Diagram</summary>

```mermaid
graph TD
    A[Start] --> B(Initialize DP table M and split table S)
    B --> C{Loop chain length 2 to n}
    C --> D{For each split k between i and j}
    D --> E[Calculate cost = M i,k + M k+1,j + dimensions]
    E --> F{Is cost < current min?}
    F -- Yes --> G[Update M i,j and S i,j]
    G --> D
    F -- No --> D
    D --> C
    C --> H[End: Min operations in M 1,n]
```

</details>
</summary>

#### 15. Prove that vertex cover problem is NP Complete.
To prove that the Vertex Cover problem is NP-Complete, you need to show two things:
1.  **Vertex Cover is in NP:** Given a graph G=(V, E) and an integer k, and a candidate set C ⊆ V, we can verify if C is a vertex cover of size at most k in polynomial time. (Check if |C| ≤ k and if every edge in E has at least one endpoint in C).
2.  **Vertex Cover is NP-Hard:** Every problem in NP can be reduced to Vertex Cover in polynomial time. This is typically done by showing a polynomial-time reduction from a known NP-Complete problem (e.g., 3-SAT or Independent Set) to Vertex Cover.

<summary>
<details>
<summary>View Diagram</summary>

```mermaid
graph LR
    subgraph Proof
        NP[In NP: Verifiable in poly-time]
        NPH[NP-Hard: Reduction from 3-SAT]
        NP --> NPC[Vertex Cover is NP-Complete]
        NPH --> NPC
    end
```

</details>
</summary>

#### 16. Explain the four different complexity classes with suitable examples.
The four common complexity classes are P, NP, NP-Complete, and NP-Hard.

<summary>
<details>
<summary>View Diagram</summary>

```mermaid
graph TD
    A[Complexity Classes] --> P(P: Poly-time solvable)
    A --> NP(NP: Poly-time verifiable)
    A --> NPC(NP-Complete: Hardest NP)
    A --> NPH(NP-Hard: Harder than NPC)
    P --> NP
    NPC --> NP
    NPC --> NPH
```

</details>
</summary>
