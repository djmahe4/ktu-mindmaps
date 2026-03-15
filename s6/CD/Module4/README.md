# Module 4

# Static vs Heap alloc

**Static Allocation vs Heap Allocation**  
(Exam-friendly point-wise notes – short, clear, and easy to remember/revise)

### Static Allocation (Compile-time / Static Memory Allocation)
- Memory is allocated **at compile time** (or link time).
- Size of memory must be **known and fixed** at compile time.
- Memory is allocated in the **data segment** (or **bss segment** for uninitialized globals).
- Lifetime → Entire program execution (from start to end).
- Management → Fully **automatic** (no programmer intervention needed).
- Examples → Global variables, static local variables, fixed-size arrays declared globally/static.
- Allocation speed → Very **fast** (zero runtime cost).
- Memory reusability → **No** (memory stays allocated even if not used).
- Fragmentation → **No** fragmentation issue.
- Preferred for → Constants, fixed-size data, global counters, lookup tables.
- Disadvantages → Cannot change size at runtime, wastes memory if over-allocated, large static data bloats executable.
- Memory location → Usually **data segment** (not stack/heap).

### Heap Allocation (Dynamic / Runtime Memory Allocation)
- Memory is allocated **at runtime** (during program execution).
- Size can be **determined and variable** at runtime (e.g., based on user input).
- Memory is allocated from the **heap** (large pool managed by runtime/library).
- Lifetime → From allocation (e.g., `malloc`/`new`) until explicit deallocation ( `free`/`delete`) or garbage collection.
- Management → **Manual** in C/C++ (programmer must free memory) or **automatic** in Java/Python (GC).
- Examples → Dynamic arrays, linked lists, trees, vectors, objects with runtime size.
- Allocation speed → **Slower** (involves searching free blocks, bookkeeping).
- Memory reusability → **Yes** (can free memory and reuse it).
- Fragmentation → **Yes** possible (external fragmentation, internal in some cases).
- Preferred for → Data structures with unknown/variable size, large data, user-dependent structures.
- Disadvantages → Risk of **memory leaks**, dangling pointers, use-after-free, overhead of heap manager.
- Memory location → **Heap** segment.

### Quick Comparison Table (Exam Favorite Format)

| Point                          | Static Allocation                          | Heap Allocation (Dynamic)                  |
|--------------------------------|--------------------------------------------|--------------------------------------------|
| Allocation time                | Compile time                               | Runtime                                    |
| Size known                     | At compile time (fixed)                    | At runtime (variable)                      |
| Memory area                    | Data segment / BSS                         | Heap                                       |
| Lifetime                       | Whole program                              | Until freed / GC                           |
| Management                     | Automatic                                  | Manual (C/C++) or GC (Java etc.)           |
| Speed                          | Very fast                                  | Slower                                     |
| Memory reusability             | No                                         | Yes                                        |
| Fragmentation                  | No                                         | Possible                                   |
| Risk of errors                 | Low (no leaks)                             | High (leaks, dangling pointers)            |
| Best for                       | Fixed-size, globals, constants             | Dynamic data structures, variable size     |

### One-liner Summary for Exams
- **Static** → Compile-time, fixed, fast, automatic, no flexibility, no leaks.
- **Heap** → Runtime, flexible, manual control (or GC), reusable, but slower + error-prone.
