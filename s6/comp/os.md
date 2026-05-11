**Operating Systems Cheat Sheet**  
**Formulas + Key Concepts** (Exam-Focused | Easy to Memorize)

### 1. Memory Management - Fragmentation & Paging

**Internal Fragmentation**  
**Formula**:  
**Internal Fragmentation = Page Size – (Process Size % Page Size)**  
(If remainder = 0, then fragmentation = 0)

**Example**: Page size = 4KB, Process = 103KB → 103 % 4 = 3 → Fragmentation = 4 – 3 = **1KB**

**Physical Memory Addressable (Paging)**  
**Total Physical Memory = (2^{PTE Size in bits}) × Frame Size**

**Example**: Frame size = 4KB (= 2¹²), PTE = 2 bytes (= 16 bits)  
→ **2¹⁶ × 2¹² = 2²⁸ bytes**

**Key Tip**: Number of bits in Page Table Entry = log₂(Max Frames)

---

### 2. CPU Utilization

**CPU Utilization (ρ)**  
**ρ = (Arrival Rate λ) / (Service Rate μ)** × 100%

**Unit Conversion Rule**: Convert both λ and μ to same time unit (per second or per minute).

**Example**: 12 processes/min, service time = 5 sec/process  
μ = 60/5 = 12 processes/min  
ρ = 12/12 = **100%**

---

### 3. Disk Scheduling (SSTF)

**No fixed formula** — Use **Shortest Seek Time First** algorithm.

**Calculation Steps**:
1. Current head position.
2. Compute absolute distance |Current – Request| for all pending requests.
3. Service the **minimum distance** request.
4. Update head position and repeat.

**Use**: To find **order of service** or **how many requests serviced before a particular one**.

---

### 4. Deadlock – 4 Necessary Conditions (All must be true)

| Condition          | Formula / Rule                          | Prevention Method                     |
|--------------------|-----------------------------------------|---------------------------------------|
| Mutual Exclusion   | Resource used by only one process       | —                                     |
| Hold and Wait      | Holding + requesting more resources     | Request all at once                   |
| No Preemption      | Resource released only voluntarily      | Allow preemption                      |
| **Circular Wait**  | Circular chain of waiting               | **Linear Ordering** of resources      |

**Circular Wait Prevention Formula**:  
Processes must request resources in **strictly increasing (or decreasing) order** of resource numbers.

---

### 5. Thrashing

**No formula**, but key condition:

**Thrashing occurs when**:  
CPU time spent on **page faults** > CPU time spent on **process execution**

**Prevention**:  
Keep **working set** of pages in main memory.

---

### 6. Round Robin Scheduling

**Time Quantum (q)**: Fixed time slice given to each process.

**Important Relations**:
- Small q → High context switching, **better response time**
- Large q → Behaves like **FCFS**
- Does **not** require prior knowledge of burst time

**Advantage over SJF**: Better **Average Response Time**

---

### 7. Starvation

**Starvation**: Process waits **indefinitely** for CPU/resources.  
Common in: Priority Scheduling & Shortest Job First.

**Prevention**: **Aging** (gradually increase priority of waiting processes).

---

### Quick Memorization Summary Table

| Topic                    | Formula / Key Expression                          | Most Important Point                     |
|--------------------------|---------------------------------------------------|------------------------------------------|
| Internal Fragmentation   | Page Size – (Process % Page Size)                 | Last incomplete page waste               |
| Physical Memory          | 2^(PTE bits) × Frame Size                         | 2²⁸ in standard 4KB + 2B PTE question   |
| CPU Utilization          | (λ / μ) × 100%                                    | Must use same time unit                  |
| Deadlock                 | Mutual + Hold&Wait + No Preempt + Circular Wait   | All 4 required                           |
| Circular Wait Prevention | Linear Ordering of Resources                      | Best prevention technique                |
| Thrashing Prevention     | Working set pages in main memory                  | Avoid excessive multiprogramming         |
| Round Robin              | Fixed Time Quantum                                | Best for interactive systems             |

