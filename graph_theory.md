Proofs of Key Graph Theory Theorems

This document provides detailed proofs for the key theorems in graph theory as specified in the modules, focusing exclusively on the mathematical derivations without conceptual explanations. Each proof is presented concisely, with references to reliable sources for further reading.

**Module 1: Introduction to Graphs**

**Handshaking Lemma**

* **Statement:** In any undirected graph $G = (V, E)$, the sum of the degrees of all vertices equals twice the number of edges: $\sum_{v \in V} \deg(v) = 2 |E|$.
* **Proof:**
    Consider an undirected graph $G$ with vertex set $V$ and edge set $E$. Each edge $e \in E$ is incident to exactly two vertices, contributing 1 to the degree of each endpoint. Summing the degrees of all vertices, each edge is counted twice (once for each endpoint). Thus, $\sum_{v \in V} \deg(v) = 2 |E|$.
* **Source:** [Handshaking Lemma](https://en.wikipedia.org/wiki/Handshaking_lemma)

**Module 2: Eulerian and Hamiltonian Graphs**

**Eulerian Circuit Theorem**

* **Statement:** A connected graph $G$ has an Eulerian circuit if and only if every vertex has even degree.
* **Proof (Necessity):**
    Suppose $G$ has an Eulerian circuit, a closed walk traversing each edge exactly once. For each vertex $v$, the circuit enters and leaves $v$ an equal number of times, using two edges per visit (one to enter, one to leave). Thus, $\deg(v)$ is even for all $v$.
* **Proof (Sufficiency):**
    Assume $G$ is connected, and all vertices have even degree. Prove by induction on the number of edges $|E|$.
    * **Base Case:** If $|E| = 0$, $G$ has one vertex, and the trivial circuit (the vertex itself) is Eulerian.
    * **Inductive Step:** Assume for any connected graph with fewer than $k$ edges and all vertices of even degree, an Eulerian circuit exists. For a graph with $k$ edges:
        Start at any vertex $v_0$, choose an edge to a neighbor, and continue choosing unused edges. Since all degrees are even, at each vertex, there is an unused edge to leave until returning to $v_0$, forming a circuit $C$.
        If $C$ includes all edges, it is an Eulerian circuit.
        If not, remove edges of $C$. In the remaining graph $G'$, each vertex has even degree (since $C$ uses an even number of edges per vertex).
        $G'$ may have multiple connected components, each with even degrees and fewer edges than $k$. By the inductive hypothesis, each component has an Eulerian circuit.
        Combine these with $C$: when $C$ passes through a vertex in a component, insert the component’s Eulerian circuit, covering all edges exactly once.
* **Source:** [Eulerian Path](https://en.wikipedia.org/wiki/Eulerian_path)

**Eulerian Path Theorem**

* **Statement:** A connected graph $G$ has an Eulerian path if and only if exactly two vertices have odd degree.
* **Proof (Necessity):**
    An Eulerian path is a walk using each edge exactly once, starting at vertex $s$ and ending at vertex $t$. For vertices other than $s$ and $t$, the path enters and leaves an equal number of times, using an even number of edges, so their degrees are even. For $s$, the path starts with one edge out; for $t$, it ends with one edge in, making their degrees odd. Thus, exactly two vertices have odd degree.
* **Proof (Sufficiency):**
    Suppose $G$ is connected with exactly two vertices, $u$ and $v$, of odd degree. Add an edge $\{u, v\}$ to form graph $G'$. In $G'$, all vertices have even degree (since adding $\{u, v\}$ increases the degree of $u$ and $v$ by 1, making them even). By the Eulerian Circuit Theorem, $G'$ has an Eulerian circuit. Remove edge $\{u, v\}$ from this circuit, resulting in a path from $u$ to $v$ in $G$, which uses each edge of $G$ exactly once, an Eulerian path.
* **Source:** [Eulerian Path](https://en.wikipedia.org/wiki/Eulerian_path)

**Dirac’s Theorem**

* **Statement:** If a graph $G$ with $n \geq 3$ vertices has each vertex degree at least $\frac{n}{2}$, then $G$ has a Hamiltonian cycle.
* **Proof:**
    Assume $G$ does not have a Hamiltonian cycle. Let $P = v_1, v_2, \ldots, v_k$ be a longest path in $G$. Since $P$ is longest, all neighbors of $v_1$ and $v_k$ are on $P$. Define sets:
    $S = \{ v_i \mid \{v_1, v_{i+1}\} \in E, 1 \leq i \leq k-1 \}$, vertices where $v_1$ is adjacent to the next vertex on $P$.
    $T = \{ v_i \mid \{v_k, v_i\} \in E, 1 \leq i \leq k-1 \}$, vertices adjacent to $v_k$.

    Since $\deg(v_1) \geq \frac{n}{2}$, $|S| \geq \frac{n}{2}$. Similarly, $\deg(v_k) \geq \frac{n}{2}$, so $|T| \geq \frac{n}{2}$.
    $S, T \subseteq \{v_1, v_2, \ldots, v_{k-1}\}$, which has $k-1$ elements.
    If $k < n$, then $|S| + |T| \geq n > k-1$, so $|S \cap T| \geq |S| + |T| - (k-1) > 0$.
    Thus, there exists $v_i \in S \cap T$, meaning $\{v_1, v_{i+1}\} \in E$ and $\{v_k, v_i\} \in E$.
    Form cycle $C$: $v_1 \to v_{i+1} \to v_{i+2} \to \cdots \to v_k \to v_i \to v_{i-1} \to \cdots \to v_2 \to v_1$.
    This cycle includes all vertices of $P$, since it traverses from $v_{i+1}$ to $v_k$, then back from $v_i$ to $v_2$, and to $v_1$.
    If $k < n$, there exists a vertex $w \notin P$. Since $G$ is connected, there is a path from $w$ to some $v_j \in P$. Since $C$ contains all vertices of $P$, adjust $C$ to include $w$, forming a longer path than $P$, contradicting the assumption that $P$ is the longest path.
    Thus, $k = n$, and $C$ is a Hamiltonian cycle.
* **Source:** [Dirac’s Theorem](https://en.wikipedia.org/wiki/Dirac%27s_theorem)

**Module 3: Trees and Graph Algorithms**

**Tree Edge Count**

* **Statement:** A tree with $n$ vertices has exactly $n-1$ edges.
* **Proof:**
    Prove by induction on the number of vertices $n$.
    * **Base Case:** For $n = 1$, a tree has one vertex and no edges: $1-1 = 0$.
    * **Inductive Step:** Assume a tree with $k$ vertices has $k-1$ edges. For a tree $T$ with $k+1$ vertices:
        Since $T$ is a tree, it has a leaf $v$ (vertex of degree 1). Remove $v$ and its incident edge, forming graph $T'$. $T'$ is connected (removing a leaf doesn’t disconnect a tree) and acyclic (no cycles were introduced), so $T'$ is a tree with $k$ vertices.
        By the inductive hypothesis, $T'$ has $k-1$ edges. $T$ has the edges of $T'$ plus the edge incident to $v$, totaling $(k-1) + 1 = k$ edges, which is $(k+1)-1$.
    Thus, the statement holds for all $n$.
* **Source:** [Tree (graph theory)](https://en.wikipedia.org/wiki/Tree_(graph_theory))

**Prim’s Algorithm Correctness**

* **Statement:** Prim’s algorithm produces a minimum spanning tree (MST) for a connected weighted graph.
* **Proof:**
    Prim’s algorithm starts with a single vertex and iteratively adds the minimum-weight edge connecting a vertex in the tree to a vertex outside it. Use the cut property: For any cut (partition of vertices into two sets), the minimum-weight edge crossing the cut is in some MST.
    At each step, consider the cut where one set is the vertices in the current tree $T$, and the other is the remaining vertices. Prim’s selects the minimum-weight edge $e$ crossing this cut. By the cut property, $e$ is in some MST. Since $T$ remains a tree (no cycles) and spans all vertices eventually, it is a spanning tree. Since all edges added are part of an MST, $T$ is an MST (if another spanning tree had lower weight, it would contradict the cut property).
* **Source:** [Minimum Spanning Tree](https://en.wikipedia.org/wiki/Minimum_spanning_tree)

**Kruskal’s Algorithm Correctness**

* **Statement:** Kruskal’s algorithm produces a minimum spanning tree for a connected weighted graph.
* **Proof:**
    Kruskal’s algorithm sorts edges by weight and adds them if they don’t form a cycle, using a union-find structure to detect cycles. Use the cycle property: The maximum-weight edge in any cycle is not in some MST.
    Suppose Kruskal’s produces tree $T$, and there exists an MST $T'$ with lower weight. Let $e$ be the first edge in $T$ not in $T'$. Adding $e$ to $T'$ forms a cycle $C$. Since $e$ was chosen by Kruskal’s, its weight is at most that of any other edge in $C$ (as edges are processed in non-decreasing order). There exists an edge $f \in C$ in $T'$ but not in $T$. Replacing $f$ with $e$ in $T'$ forms a new spanning tree $T''$. Since $w(e) \leq w(f)$, $w(T'') \leq w(T')$, so $T''$ is also an MST. Repeat until all edges of $T$ are in the MST, showing $T$ is an MST.
* **Source:** [Minimum Spanning Tree](https://en.wikipedia.org/wiki/Minimum_spanning_tree)

**Dijkstra’s Algorithm Correctness**

* **Statement:** Dijkstra’s algorithm finds the shortest paths from a source vertex to all vertices in a graph with non-negative edge weights.
* **Proof:**
    Dijkstra’s maintains a set $S$ of vertices with finalized shortest-path distances and a priority queue for tentative distances. Initialize $\text{dist}(s) = 0$, others infinity, and $S = \emptyset$. At each step, extract vertex $u$ with minimum tentative distance, add to $S$, and relax neighbors $v$: if $\text{dist}(u) + w(u,v) < \text{dist}(v)$, update $\text{dist}(v)$.
    Claim: When $u$ is extracted, $\text{dist}(u)$ is the shortest-path distance.
    Suppose the first time the claim fails is for vertex $u$, so there exists a shorter path $P$ from $s$ to $u$. Let $y$ be the first vertex on $P$ not in $S$, and $x \in S$ the vertex before $y$. Since $x \in S$, $\text{dist}(x)$ is correct. The subpath from $s$ to $x$ has length $\text{dist}(x)$, and from $x$ to $y$, weight $w(x,y) \geq 0$. Thus, the distance to $y$ via $P$ is at least $\text{dist}(x) + w(x,y)$. When $x$ was added to $S$, $y$’s tentative distance was updated to at most $\text{dist}(x) + w(x,y)$. Since $y \notin S$, its tentative distance is at least $\text{dist}(x) + w(x,y)$, and since $u$ was chosen, $\text{dist}(u) \leq \text{dist}(y)$. But the path to $u$ via $y$ has length at least $\text{dist}(y)$, contradicting that $P$ is shorter. Thus, $\text{dist}(u)$ is correct for all vertices.
* **Source:** [Dijkstra’s Algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)

**Module 4: Connectivity and Planar Graphs**

**Euler’s Formula for Planar Graphs**

* **Statement:** For a connected planar graph $G$, $v - e + f = 2$, where $v$ is the number of vertices, $e$ is edges, and $f$ is faces.
* **Proof:**
    Prove by induction on the number of edges $e$.
    * **Base Case:** Consider a tree (acyclic planar graph) with $v$ vertices. Then $e = v-1$, $f = 1$ (only the exterior face). Thus, $v - e + f = v - (v-1) + 1 = 2$.
    * **Inductive Step:** Assume for a connected planar graph with $k$ edges, $v - e + f = 2$. For a graph with $k+1$ edges:
        If the graph is a tree, $e = v-1$, and the formula holds.
        Otherwise, it has a cycle. Remove an edge $e'$ from a cycle. This merges two faces (since $e'$ was on the boundary of two faces), reducing $f$ by 1 and $e$ by 1, forming graph $G'$ with $k$ edges.
        By the inductive hypothesis, for $G'$, $v - (e-1) + (f-1) = 2$.
        For the original graph, $v - e + f = v - (e-1+1) + (f-1+1) = 2$.
    Thus, the formula holds for all connected planar graphs.
* **Source:** [Planar Graph](https://en.wikipedia.org/wiki/Planar_graph)

**Module 5: Graph Representations and Vertex Colouring**

**Five Color Theorem**

* **Statement:** Every planar graph can be colored with at most five colors such that no adjacent vertices share the same color.
* **Proof:**
    Prove by induction on the number of vertices $n$.
    * **Base Case:** For $n \leq 5$, the graph can be colored with at most five colors (since there are at most five vertices).
    * **Inductive Step:** Assume every planar graph with $k$ vertices is 5-colorable. For a planar graph $G$ with $k+1$ vertices:
        Every planar graph has a vertex $v$ with $\deg(v) \leq 5$ (by the fact that planar graphs satisfy $\sum \deg(v) = 2e \leq 6v - 12$). Remove $v$, forming $G'$ with $k$ vertices.
        By the inductive hypothesis, $G'$ can be colored with five colors. Assign $v$ a color different from its neighbors (at most five). Since there are five colors available, at least one color is unused by the neighbors, allowing $v$ to be colored.
    Thus, $G$ is 5-colorable.
* **Source:** [Five Color Theorem](https://en.wikipedia.org/wiki/Five_color_theorem)

**Notes on Excluded Theorems**

* **Kuratowski’s Theorem:** The module specifies that the proof is not required.
* **Four Color Theorem:** The proof is complex, involving computer-assisted case analysis, and is typically not included in standard courses, so it is omitted here.
* **Floyd-Warshall Algorithm:** While mentioned, its proof is similar to Dijkstra’s but more complex, and standard texts provide it without controversy.
* **Greedy Coloring Algorithm:** Does not have a theorem per se, but its performance depends on vertex ordering, not requiring a formal proof here.

**Table of Theorems and Proof Techniques**

| Theorem              | Statement Summary                   | Proof Technique         |
| :------------------- | :--------------------------------- | :---------------------- |
| Handshaking Lemma    | Sum of degrees = 2 × edges         | Edge counting           |
| Eulerian Circuit     | Even degrees for circuit           | Induction on edges      |
| Eulerian Path        | Exactly two odd degrees for path     | Graph modification      |
| Dirac’s Theorem      | Degree ≥ n/2 implies Hamiltonian cycle | Longest path contradiction |
| Tree Edge Count      | Tree with n vertices has n-1 edges | Induction on vertices   |
| Prim’s Algorithm     | Produces MST                       | Cut property            |
| Kruskal’s Algorithm  | Produces MST                       | Cycle property          |
| Dijkstra’s Algorithm | Shortest paths for non-negative weights | Greedy invariant        |
| Euler’s Formula      | v - e + f = 2 for planar graphs    | Induction on edges      |
| Five Color Theorem   | Planar graphs 5-colorable          | Induction on vertices   |

This table summarizes the theorems and their proof methods for quick reference.

* Module 2 *
| **Type**                          | **Description**                                                       |
|-----------------------------------|-----------------------------------------------------------------------|
| **Simple DiGraph**                | No multiple edges or loops.                                           |
| **Multidigraph**                  | Multiple edges allowed between vertices.                               |
| **Weighted DiGraph**              | Edges have weights (values).                                           |
| **Acyclic Directed Graph (DAG)**  | No cycles in the graph.                                               |
| **Strongly Connected DiGraph**    | All vertices are reachable from each other.                          |
| **Weakly Connected DiGraph**      | Ignoring edge direction, the graph is connected.                      |
| **Symmetric DiGraph**             | If A → B, then B → A must also exist.                                |
| **Asymmetric DiGraph**            | If A → B, there's no guarantee for B → A.                            |
| **Complete Symmetric DiGraph**    | Every pair of distinct vertices is connected bidirectionally (A ↔ B). |
| **Complete Asymmetric DiGraph**   | Every pair of distinct vertices is connected unidirectionally (A → B or B → A, but not both). |
