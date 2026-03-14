# LR parsing
```mermaid
graph TD
    %% Global Style
    classDef start fill:#f9f,stroke:#333,stroke-width:2px;
    classDef items fill:#fff4dd,stroke:#d4a017,stroke-width:2px;
    classDef slr fill:#e1f5fe,stroke:#01579b,stroke-width:2px;
    classDef clr fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px;
    classDef lalr fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;

    Start((<b>Augmented Grammar</b>)) --> ItemChoice{Which <b>Items</b><br/>to use?}

    %% SLR Path
    ItemChoice -- "Simple" --> LR0["`**LR(0) Items**  
    Just dots: A → α.β`"]
    LR0 --> SLR["`**SLR Table**`"]
    SLR -.-> SLRRule["`**Reduction Rule:**  
    Reduce if the next token is in  
    **FOLLOW(A)**`"]

    %% CLR/LALR Path
    ItemChoice -- "Powerful" --> LR1["`**LR(1) Items**  
    Dots + Lookahead: A → α.β, **a**`"]
    
    LR1 --> CLR["`**CLR Table**`"]
    CLR -.-> CLRRule["`**Reduction Rule:**  
    Reduce **only** if next token  
    matches the **Lookahead 'a'**`"]
    
    CLR --> Merge{"`Merge states with  
    same 'Core'?'`"}
    Merge -- "Yes (Compress)" --> LALR["`**LALR Table**`"]
    
    %% Annotations
    subgraph Legend
        direction LR
        L1[Smallest Table / Weakest] --- L2[Largest Table / Strongest] --- L3[Medium Table / Balanced]
    end

    %% Class Assigning
    class Start start;
    class LR0,LR1 items;
    class SLR slr;
    class CLR clr;
    class LALR lalr;
```

---

### The "Noob" Summary Table
If the diagram is the "Map," this table is the "Cheat Sheet" for your exams:

| Feature | **SLR** (Simple) | **CLR** (Canonical) | **LALR** (Look-Ahead) |
| :--- | :--- | :--- | :--- |
| **Items Used** | **LR(0)** (No lookaheads) | **LR(1)** (Lookaheads) | **LR(1)** (Lookaheads) |
| **Number of States** | Smallest | **Largest** (Can be huge) | Same as SLR (Merged) |
| **Reduction Logic** | Uses **FOLLOW(A)** set | Uses **specific lookahead** | Uses **specific lookahead** |
| **Power** | Weak (Many conflicts) | **Strongest** | Strong (Best balance) |
| **Memory** | Low | High | Low |

### How to remember the "Reduce" difference:
1.  **SLR (The Lazy Parser):** "I see a finished rule? I'll reduce it if the next token is *any* valid follower of this variable." (Often gets confused).
2.  **CLR (The Strict Parser):** "I only reduce if the next token is *exactly* the one I predicted when I built my state." (Very accurate, but very bulky).
3.  **LALR (The Smart Parser):** "I'll use the strict logic of CLR, but I'll combine similar states together to save space." (What most real-world tools like Yacc/Bison use).
