**Module 3 Part B – Quick Master/Revise Notes**

**1. LR(0) items**  
All possible dotted productions (items) from the grammar:  
S' → .S | S.  
S → .L=R | L.=R | L=R.  
S → .R | R.  
L → .*R | *.R | *R.  
L → .id | id.  
R → .L | L.  

**2. Canonical LR(0) collection + prove not SLR(1)**  
States (I0–I9):  
- I0: S'→.S, S→.L=R, S→.R, L→.*R, L→.id, R→.L  
- I1: S'→S.  
- I2: S→L.=R, R→L. ← **conflict here**  
- I3: S→R.  
- I4: L→*.R, R→.L, L→.*R, L→.id  
- I5: L→id.  
- I6: S→L=.R, R→.L, L→.*R, L→.id  
- I7: L→*R.  
- I8: R→L.  
- I9: S→L=R.  

**Proof not SLR(1):** In I2 there is a reduce item (R→L.) **and** shift on =.  
FOLLOW(R) contains = (because S→L=R puts = in FOLLOW(L) and R→L puts FOLLOW(L) in FOLLOW(R)).  
So SLR table puts both **shift** and **reduce** on = → shift-reduce conflict. Hence not SLR(1).

**3. Shift-reduce parser for abbcde**  
Stack | Input | Action  
---|---|---  
$ | abbcde$ | shift a  
$a | bbcde$ | shift b  
$ab | bcde$ | reduce A→b → $aA  
$aA | bcde$ | shift b  
$aAb | cde$ | shift c  
$aAbc | de$ | reduce A→Abc → $aA  
$aA | de$ | shift d  
$aAd | e$ | reduce B→d → $aAB  
$aAB | e$ | shift e  
$aABe | $ | reduce S→aABe → $S  
$S | $ | accept  

**4. Prove grammar S→(S)|a is LR(0)**  
Augmented states:  
I0: S'→.S, S→.(S), S→.a  
I1: S→a. (pure reduce)  
I2: S→(.S), S→.(S), S→.a (only shifts)  
I3: S'→S. (accept)  
I4: S→(S.) (only shift on ))  
I5: S→(S). (pure reduce)  
**No state has both reduce item + shift item or two reduce items** → LR(0) grammar.

**5. Main actions in shift-reduce parser**  
- **Shift**: push next input symbol onto stack  
- **Reduce**: pop |RHS| symbols, push LHS  
- **Accept**: stack has start symbol + $  
- **Error**: no action possible  

**6. Conflicts in LR(0) parsing**  
- **Shift-reduce**: state has A→α.aβ and B→γ. (e.g., I2 of Q2 above)  
- **Reduce-reduce**: state has A→α. and B→β. (example: S→a, A→a, B→a)  

**7. Handle pruning**  
Handle = RHS of a production that can be reduced.  
Sentence: aaabbb  
Handles in order of reduction:  
aaabbb → aa**A**bbb  (handle: 3rd a)  
aa**A**bbb → a**A**bbb   (handle: 2nd a + A)  
aA b**b**b → aA b**B**b   (handle: 4th b)  
aA **bB**b → aA **B**b     (handle: 3rd b + B)  
a**A B b** → **S**          (handle: entire a A B b)

**Module 4 Part B – Quick Master/Revise Notes**

**1. Bottom-up evaluation of (3*5)–2 using desk-calculator SDD**  
SDD rules (synthesized .val):  
expr → expr + term {expr.val = expr1.val + term.val}  
expr → expr – term {expr.val = expr1.val – term.val}  
term → term * factor {term.val = term1.val * factor.val}  
factor → (expr) {factor.val = expr.val}  
factor → digit {factor.val = digit.lexval}  

Steps (reductions compute val on stack):  
- 3 → factor.val=3  
- 3 * 5 → term.val=15  
- (15) → expr.val=15  
- 15 – 2 → expr.val=13  

**2. Evaluate (3+5/2)*(2+4/3) + annotated parse tree**  
Value = (3 + 2.5) × (2 + 1.333) = 5.5 × 3.333 ≈ 18.333  
Annotated tree (bottom-up .val):  
- 5/2 = 2.5  
- 3+2.5 = 5.5  
- 4/3 = 1.333  
- 2+1.333 = 3.333  
- 5.5 * 3.333 = 18.333 (root)  

**3. Three-address code representations**  
- **Quadruples**  
(+, a, b, t1)  
(+, b, c, t2)  
(+, a, b, t3)  
(+, t3, c, t4)  
(*, t1, t2, t5)  
(*, t5, t4, t6)  

- **Triples**  
0: + a b  
1: + b c  
2: + a b  
3: + (2) c  
4: * (0) (1)  
5: * (4) (3)  

- **Indirect triples** (pointers to above triples).

**4. DAG for T1=a+b, T2=a–b, T3=T1*T2, T4=T1–T3, T5=T4+T3**  
Nodes:  
- a, b (leaves)  
- + (T1)  
- – (T2)  
- * (T3, children T1 & T2)  
- – (T4, children T1 & T3)  
- + (T5, children T4 & T3)  
(Common subexpressions T1 & T3 are shared.)

**5. Syntax tree & DAG for e := (a*b) + (c-d)*(a*b)**  
**Syntax tree**: assignment node, left=e, right= + node with left=(a*b), right= *( (c-d), (a*b) ) – two separate (a*b) subtrees.  
**DAG**: same but single shared node for (a*b) → common subexpression eliminated.

**6. Static vs Heap allocation**  
- **Static**: fixed at compile time (globals, static locals). Fast, no runtime overhead, but no recursion/dynamic size.  
- **Heap**: runtime (malloc/new). Flexible for arrays/objects, but slower, fragmentation, needs garbage collection.

**Module 5 Part B – Quick Master/Revise Notes**

**1. Loop optimisation techniques**  
- **Code motion** (loop-invariant): move x=5*y out of while(i<n){x=5*y; …}  
- **Strength reduction**: i*4 → i<<2 (or incremental pointer)  
- **Induction variable elimination**: remove extra counters  
- **Loop unrolling**: duplicate body, reduce branch overhead.

**2. Code optimisation techniques**  
- Local (within block): common subexpr, dead-code elim, constant folding  
- Global (across blocks): data-flow analysis  
- Loop optimisations (above)  
- Peephole (small patterns)  
- Machine-dependent (register allocation).

**3. Function-preserving transformations**  
(Do not change program meaning)  
- Common subexpression elimination  
- Dead-code elimination  
- Copy propagation  
- Constant folding/propagation  
- Algebraic simplification (x+0 → x).

**4. Needs for optimisation phase**  
- Faster execution  
- Smaller code size  
- Better register/cache use  
- Produce efficient code automatically.

**Revision Tip**: Focus on **I2 conflict** (Module 3), **handle sequence** (Q7), **DAG sharing** (Module 4), and **loop-invariant + strength reduction** (Module 5). These repeat in exams. Revise once with these notes → you’re set!
