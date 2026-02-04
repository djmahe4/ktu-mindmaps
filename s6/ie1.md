
### 1. Complexity Analysis & Asymptotic Notations
**Time Complexity:** The amount of time an algorithm takes to run as a function of the input size ($n$).
**Space Complexity:** The amount of memory space required by an algorithm during execution.

| Notation | Name | Meaning | Graphical Relation |
| :--- | :--- | :--- | :--- |
| **$O(g(n))$** | Big-Oh | Upper Bound (Worst Case) | $f(n) \le c \cdot g(n)$ |
| **$\Omega(g(n))$** | Big-Omega | Lower Bound (Best Case) | $f(n) \ge c \cdot g(n)$ |
| **$\Theta(g(n))$** | Theta | Tight Bound (Average Case) | $c_1 g(n) \le f(n) \le c_2 g(n)$ |
| **$o(n) / \omega(n)$**| Little-o/$\omega$ | Non-tight Upper/Lower bound | Strict inequality ($<$ or $>$) |

**Common Complexities (Low to High):**
$O(1) < O(\log n) < O(n) < O(n \log n) < O(n^2) < O(n^3) < O(2^n)$

---

### 2. Solving Recurrences

#### The Extended Master Theorem
For the recurrence: **$T(n) = aT(n/b) + \Theta(n^k \log^p n)$**
First, calculate the critical value: **$c = \log_b a$**

##### **Case 1: $c > k$ (Work at root is insignificant)**
The recursive part dominates.
*   **Result:** $T(n) = \Theta(n^c)$

##### **Case 2: $c = k$ (Work is balanced)**
The $\log$ power $p$ determines the extra logarithmic factor.
*   If **$p > -1$**: $T(n) = \Theta(n^k \log^{p+1} n)$  *(Most common case)*
*   If **$p = -1$**: $T(n) = \Theta(n^k \log \log n)$
*   If **$p < -1$**: $T(n) = \Theta(n^k)$

##### **Case 3: $c < k$ (Work at root dominates)**
$f(n)$ dominates, provided it satisfies the **Regularity Condition**: $a f(n/b) \le \delta f(n)$ for some $\delta < 1$.
*   If **$p \ge 0$**: $T(n) = \Theta(n^k \log^p n)$
*   If **$p < 0$**: $T(n) = \Theta(n^k)$

---

#### Application to your Exam Questions

Using this extended logic, let's solve the specific problems from your paper:

**1. Question 2b: $T(n) = 2T(n/2) + n \log n$**
*   $a = 2, b = 2 \implies c = \log_2 2 = \mathbf{1}$
*   $f(n) = n^1 \log^1 n \implies k = \mathbf{1}, p = \mathbf{1}$
*   **Comparison:** $c = k$ (Case 2) and $p = 1$.
*   **Formula:** $n^k \log^{p+1} n$
*   **Result:** $T(n) = \Theta(n \log^2 n)$

**2. Question 5b: $T(n) = 2T(n/2) + 10n$**
*   $a = 2, b = 2 \implies c = \log_2 2 = \mathbf{1}$
*   $f(n) = 10n^1 \log^0 n \implies k = \mathbf{1}, p = \mathbf{0}$
*   **Comparison:** $c = k$ (Case 2) and $p = 0$.
*   **Formula:** $n^1 \log^{0+1} n$
*   **Result:** $T(n) = \Theta(n \log n)$

**3. Question 2a: $T(n) = 3T(n/2) + n^2$**
*   $a = 3, b = 2 \implies c = \log_2 3 \approx \mathbf{1.58}$
*   $f(n) = n^2 \log^0 n \implies k = \mathbf{2}, p = \mathbf{0}$
*   **Comparison:** $c < k$ (Case 3)
*   **Check Regularity:** $3(n/2)^2 \le \delta n^2 \implies \frac{3}{4}n^2 \le \delta n^2$ (True for $\delta = 0.75$)
*   **Result:** $T(n) = \Theta(n^2)$

---

#### Quick Summary Table for Cheat Sheet
| Condition | $p$ value | Result |
| :--- | :--- | :--- |
| **$c > k$** | Any | $\Theta(n^c)$ |
| **$c = k$** | $p > -1$ | $\Theta(n^k \log^{p+1} n)$ |
| **$c = k$** | $p = -1$ | $\Theta(n^k \log \log n)$ |
| **$c < k$** | $p \ge 0$ | $\Theta(n^k \log^p n)$ |

To complete your cheat sheet, here are the sections for **Substitution Method** (Guess & Prove) and **Recursion Tree Method**, including a diagram for the complex case found in your exam paper (Question 3, Module 1).

---

### 1. Substitution Method (Mathematical Induction)
This method is used to prove a bound by guessing the form of the solution and then using induction to find the constants.

**Steps:**
1.  **Guess:** Based on the Master Theorem or experience, guess the complexity (e.g., $T(n) \le cn^2$).
2.  **Assumption:** Assume the guess holds for all $k < n$ (e.g., $T(n/2) \le c(n/2)^2$).
3.  **Substitution:** Plug the assumption into the original recurrence.
4.  **Proof:** Show that $T(n) \le c \cdot (\text{guessed function})$ for a specific constant $c > 0$.

**Example from Paper ($T(n) = 2T(n/2) + n$):**
*   **Guess:** $T(n) \le cn \log n$.
*   **Substitute:** $T(n) \le 2(c \frac{n}{2} \log \frac{n}{2}) + n$
*   **Solve:** $T(n) \le cn (\log n - \log 2) + n \implies cn \log n - cn + n$.
*   **Condition:** For $T(n) \le cn \log n$ to be true, $-cn + n$ must be $\le 0$, which is true if **$c \ge 1$**.

---

### 2. Recursion Tree Method
This is a visual way to sum the work done at each level of the recursion. It is best for recurrences that don't fit the standard Master Theorem.

**Steps:**
1.  **Root:** Write the non-recursive part ($f(n)$) as the root.
2.  **Expand:** Branch out into sub-problems.
3.  **Level Sum:** Calculate the total work done at each horizontal level.
4.  **Height:** Determine the depth of the tree (when the sub-problem size reduces to 1).
5.  **Total:** Sum of (Work per level $\times$ Number of levels) + Leaf costs.

**Diagram for Q3: $T(n) = T(n/3) + T(2n/3) + n$**
This is an asymmetrical tree. The longest path determines the height.

```mermaid
graph TD
    n((n)) -- n/3 --- n3((n/3))
    n -- 2n/3 --- 2n3((2n/3))
    
    n3 -- n/9 --- n9((n/9))
    n3 -- 2n/9 --- 2n9((2n/9))
    
    2n3 -- 2n/9 --- 2n9b((2n/9))
    2n3 -- 4n/9 --- 4n9((4n/9))

    style n fill:#f9f,stroke:#333
```

**Analysis of the Tree above:**
*   **Level 0 Cost:** $n$
*   **Level 1 Cost:** $n/3 + 2n/3 = \mathbf{n}$
*   **Level 2 Cost:** $n/9 + 2n/9 + 2n/9 + 4n/9 = \mathbf{n}$
*   **General Pattern:** Every level sums to $n$.
*   **Height ($h$):** The longest branch follows $(2/3)^h \cdot n = 1$. This gives $h = \log_{3/2} n$.
*   **Total Work:** $n \times \text{height} = n \log_{3/2} n \approx \mathbf{O(n \log n)}$.

---

### 3. Iteration Method (Q1b, Q2b)
Unlike the tree, you expand the formula mathematically until you find a series.

**Example ($T(n) = 2T(n/2) + 2$):**
1.  $T(n) = 2[2T(n/4) + 2] + 2 = 4T(n/4) + 4 + 2$
2.  $T(n) = 4[2T(n/8) + 2] + 4 + 2 = 8T(n/8) + 8 + 4 + 2$
3.  **$k$-th iteration:** $2^k T(n/2^k) + \sum_{i=1}^{k} 2^i$
4.  Stop when $n/2^k = 1 \implies k = \log_2 n$.
5.  **Result:** $n T(1) + (2^{\log n + 1} - 2) \approx n + 2n \approx \mathbf{O(n)}$.

---

### Comparison Table for Cheat Sheet
| Method | Best Use Case | Risk |
| :--- | :--- | :--- |
| **Master Theorem** | Standard forms $aT(n/b) + f(n)$ | Doesn't work for $T(n-1)$ or mixed fractions. |
| **Recursion Tree** | Visualizing work distribution | Can get messy with asymmetrical branches. |
| **Iteration** | Simple linear recurrences | High chance of algebraic errors in the series. |
| **Substitution** | Proving a guess is correct | Requires a good initial guess. |
---

### 3. AVL Trees (Height-Balanced Trees)
An AVL tree is a self-balancing Binary Search Tree (BST) where the **Balance Factor (BF)** of every node is **-1, 0, or 1**.

$$\text{Balance Factor (BF)} = \text{Height(Left Subtree)} - \text{Height(Right Subtree)}$$

#### **AVL Rotations (To fix imbalance)**
Imbalance occurs when $|BF| > 1$. Identify the "Critical Node" (the lowest ancestor where BF is invalid).

```mermaid
graph TD
    subgraph LL_Rotation_Right_Rotate
    A((Crit)) -- L --> B((Child)) -- L --> C((GrandChild))
    end
    subgraph RR_Rotation_Left_Rotate
    D((Crit)) -- R --> E((Child)) -- R --> F((GrandChild))
    end
```

| Type of Insertion | Rotation Required | Description |
| :--- | :--- | :--- |
| **Left-Left (LL)** | **Single Right** | Rotate the critical node to the right. |
| **Right-Right (RR)** | **Single Left** | Rotate the critical node to the left. |
| **Left-Right (LR)** | **Left then Right** | Left rotate child, then Right rotate critical node. |
| **Right-Left (RL)** | **Right then Left** | Right rotate child, then Left rotate critical node. |

#### **AVL Properties**
*   **Search/Insert/Delete Time:** $O(\log n)$ (Guaranteed due to balancing).
*   **Max Height:** Approximately $1.44 \log_2 n$.
*   **Difference from BST:** BST can become a "skewed tree" ($O(n)$ complexity); AVL stays logarithmic.

---

### 4. Code Analysis (Algorithm Multiply)
```cpp
for (int i=0; i<n; i++)          // Runs n times
  for (int j=0; j<n; j++)        // Runs n times
    for (int k=0; k<n; k++)      // Runs n times
      C[i][j] += A[i][k] * B[k][j];
```
*   **Time Complexity:** $n \times n \times n = \mathbf{O(n^3)}$.
*   **Space Complexity:** $\mathbf{O(n^2)}$ (to store the 2D matrices).

---

### 5. Quick Check for Balance Factors (Ref: Q8)
To solve the diagram in Question 8:
1.  **Leaves** always have BF = 0.
2.  Work bottom-up.
3.  **Example:** If a node has a left child of height 2 and a right child of height 0, $BF = 2 - 0 = 2$ (**Imbalance: Left-Heavy**). Requires a Right Rotation.
