To help you visualize how a compiler actually "thinks" during bottom-up evaluation, we can use Mermaid diagrams to show the **Annotated Parse Tree** and the **Stack States**.

### 1. The Annotated Parse Tree (The "Goal")
In bottom-up evaluation, we start at the leaves (the numbers) and work our way up to the root ($L$). Each node shows the value ($val$) calculated from its children.

```mermaid
graph BT
    %% Nodes
    D1[digit: 3] --> F1[F.val: 3]
    F1 --> T1[T.val: 3]
    
    D2[digit: 5] --> F2[F.val: 5]
    
    T1 --> T2[T.val: 15]
    star[*] --> T2
    F2 --> T2
    
    T2 --> E1[E.val: 15]
    
    lp["("] --> F3[F.val: 15]
    E1 --> F3
    rp[")"] --> F3
    
    F3 --> T3[T.val: 15]
    T3 --> E2[E.val: 15]
    
    minus[-] --> E3[E.val: 13]
    E2 --> E3
    
    D3[digit: 2] --> F4[F.val: 2]
    F4 --> T4[T.val: 2]
    T4 --> E3
    
    E3 --> L[L.val: 13]

    %% Styling
    style L fill:#f96,stroke:#333,stroke-width:4px
    style E3 fill:#bbf,stroke:#333
    style T2 fill:#dfd,stroke:#333
```

---

### 2. Stack Evolution (The "Process")
Bottom-up parsing uses a **Stack**. Think of the stack as a tray where we pile symbols until they match a rule in our SDD. Once they match, we "Reduce" (replace the pile with a single result).

Here is the flow of the stack for `(3*5)-2`:

```mermaid
stateDiagram-v2
    state "Empty Stack" as s1
    state "( " as s2
    state "( 3 " as s3
    state "( F:3 " as s4
    state "( T:3 " as s5
    state "( T:3 * " as s6
    state "( T:3 * 5 " as s7
    state "( T:3 * F:5 " as s8
    state "( T:15 " as s9
    state "( E:15 " as s10
    state "( E:15 ) " as s11
    state "F:15 " as s12
    state "E:15 - 2" as s13
    state "E:13" as s14

    s1 --> s2 : Shift '('
    s2 --> s3 : Shift '3'
    s3 --> s4 : Reduce F -> digit
    s4 --> s5 : Reduce T -> F
    s5 --> s6 : Shift '*'
    s6 --> s7 : Shift '5'
    s7 --> s8 : Reduce F -> digit
    s8 --> s9 : Reduce T -> T * F (3*5)
    s9 --> s10 : Reduce E -> T
    s10 --> s11 : Shift ')'
    s11 --> s12 : Reduce F -> (E)
    s12 --> s13 : ...Reduce and Shift - 2
    s13 --> s14 : Reduce E -> E - T
```

---

### 3. Shift vs. Reduce Logic
If you are confused about when to "Shift" and when to "Reduce," follow this logic flow:

```mermaid
flowchart TD
    A[Look at Next Input Token] --> B{Does Stack Top match\n RHS of a Rule?}
    B -- No --> C[SHIFT: Move token from\n Input to Stack]
    B -- Yes --> D{Is there a higher\n precedence op coming?}
    D -- Yes --> C
    D -- No --> E[REDUCE: Replace symbols with\n LHS and calc value]
    E --> A
    C --> A
```

### Key Takeaways for your SDD:
1.  **Shift:** You are "waiting" for more information (like waiting for the `5` after seeing `3 *`).
2.  **Reduce:** You have found a complete "phrase" (like `3 * 5`) and can now perform the math.
3.  **Synthesis:** In a bottom-up SDD, values always flow **upward** from the children to the parent. This is why it is called "Synthesized Attributes."
