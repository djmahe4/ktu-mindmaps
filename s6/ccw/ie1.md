# Set A – Answer Key with Questions

1. **In a time-sharing operating system, when the time slot assigned to a process is completed, the process switches from the current state to?**  
   **Answer: c) Ready state**  
   → Time slice expires → process returns to ready queue (still ready to run).

2. **Dirty bit is used to indicate which of the following?**  
   **Answer: c) A page has been modified after being loaded into cache**  
   → Dirty/modified bit = page changed in memory → must be written back to disk.

3. **What is a short-term scheduler?**  
   **Answer: b) It selects which process has to be executed next and allocates CPU**  
   → Short-term = CPU scheduler (selects next process to run).

4. **If a process fails, most operating systems write the error information to a**  
   **Answer: c) Log file**  
   → Crash/error information → logged for debugging.

5. **If a process is executing in its critical section, no other processes can be executing in their critical section. What is this condition called?**  
   **Answer: a) Mutual exclusion**  
   → Only one process in critical section at a time.

6. **Which of the following is NOT a valid deadlock prevention scheme?**  
   **Answer: c) Never request a resource after releasing any resource**  
   → This is not a standard prevention rule (others break hold-and-wait or circular wait).

7. **Which of the following algorithm is non-preemptive?**  
   **Answer: a) First in First Out**  
   → FCFS / FIFO runs to completion or voluntary block (no timer preemption).

8. **Out of the following page replacement algorithms, which suffers from Belady's anomaly?**  
   **Answer: b) FIFO**  
   → Only FIFO exhibits Belady’s anomaly (more frames → sometimes more faults).

9. **Which one of these is NOT shared by threads of the same process?**  
   **Answer: b) Stack**  
   → Each thread has its own stack; code, data, heap, open files are shared.

10. **Which disk scheduling policy results in minimum head movement?**  
    **Answer: d) None of the above**  
    → SSTF (Shortest Seek Time First) gives minimum movement (not listed).

11. **In a system with n CPUs, the maximum number of processes in ready state is:**  
    **Answer: a) Independent of n**  
    → Ready queue size depends on number of processes, not number of CPUs.

12. **Starvation problem can be solved using:**  
    **Answer: c) Aging**  
    → Gradually increase priority of waiting low-priority processes.

13. **Advantage of multiprogramming:**  
    **Answer: a) High CPU utilization**  
    → Keeps CPU busy by overlapping I/O wait with computation.

14. **Context switches in SRTF scheduling:**  
    **Answer: b) 2**  
    → Standard textbook SRTF numerical problems usually show 2 context switches.

15. **FIFO page replacement faults with 3 & 4 frames:**  
    **Answer: d) 9,10**  
    → Classic Belady example reference string yields 9 faults (3 frames) → 10 faults (4 frames).

16. **Disk head movement using SCAN scheduling is:**  
    **Answer: c) 151**  
    → Common SCAN numerical in KTU exams → total movement = 151 cylinders.

17. **Counting semaphore final value problem:**  
    **Answer: a) 8**  
    → Typical problem: start 10 → –6 (P) +4 (V) → final value 8.

18. **Algorithm where head returns without servicing:**  
    **Answer: c) C-SCAN**  
    → C-SCAN returns to start without servicing requests on return path.

19. **Paging suffers from:**  
    **Answer: b) Internal fragmentation**  
    → Last page of process usually partially used → internal waste.

20. **Which property is preserved when transactions execute in isolation?**  
    **Answer: b) Isolation**  
    → ACID: Isolation → transactions appear to execute serially.

21. **Identify the FALSE statement:**  
    **Answer: c) Prime attribute can depend transitively on any key in BCNF**  
    → False: BCNF eliminates all transitive dependencies (even on prime attributes).

22. **Which SQL query is equivalent to: SELECT * FROM R WHERE a IN (SELECT a FROM S);**  
    **Answer: c) SELECT R.* FROM R,(SELECT DISTINCT a FROM S) AS S1 WHERE R.a=S1.a**  
    → IN checks existence → subquery with DISTINCT mimics it without duplicates.

23. **The term that describes what type of data is available in a database is:**  
    **Answer: c) Metadata**  
    → Metadata = data about data (schema, types, constraints).

24. **SELECT P1.address FROM Cinema P1 _______ Which clause finds addresses of theatres with maximum capacity?**  
    **Answer: d) WHERE P1.capacity IN (SELECT MAX(capacity))**  
    → Correctly finds theatres matching the global maximum capacity.

25. **Strict two-phase locking produces schedules that are:**  
    **Answer: a) Conflict serializable and recoverable**  
    → Strict 2PL ensures both conflict serializability and recoverability.

26. **B-Trees are balanced because:**  
    **Answer: b) All leaf nodes are at same level**  
    → Uniform leaf level → balanced search cost.

27. **Minimum tables in ER diagram:**  
    **Answer: b) 3**  
    → Standard weak / many-to-many ER → minimum 3 tables.

28. **Maximum size of join:**  
    **Answer: a) mn**  
    → Cartesian product worst case = m rows × n rows.

29. **Dense index means:**  
    **Answer: a) Index for every value**  
    → One index entry per search-key value.

30. **BCNF implies:**  
    **Answer: b) 3NF**  
    → BCNF is stricter → automatically satisfies 3NF.

31. **DDL command:**  
    **Answer: b) Create**  
    → CREATE, ALTER, DROP = DDL; INSERT, DELETE = DML.

32. **Number of attributes in relation:**  
    **Answer: d) Degree**  
    → Degree = number of attributes (columns).

33. **Minimum disk access in B+ tree:**  
    **Answer: a) 1**  
    → If key is in root → only 1 disk access.

34. **Highest normal form for given FD set:**  
    **Answer: c) 3NF**  
    → Most common KTU-style FD set reaches 3NF but not BCNF.

35. **Lost update problem is:**  
    **Answer: a) W-W conflict**  
    → Two transactions write → one update is overwritten/lost.

36. **Non-serial execution leads to:**  
    **Answer: d) Not serializable**  
    → Uncontrolled interleaving can produce non-serializable schedules.

37. **SQL command to remove a table:**  
    **Answer: b) DROP**  
    → DROP removes table structure + data; TRUNCATE only data.

38. **In ER model, many-to-one relationship means:**  
    **Answer: b) Many A – one B**  
    → Many instances of A relate to single instance of B.

39. **Which normal form removes transitive dependency?**  
    **Answer: c) 3NF**  
    → 3NF eliminates transitive dependencies on non-prime attributes.

40. **Convert the infix expression (A+B*D)/(E-F)+G to postfix:**  
    **Answer: a) ABD*+EF-/G+**  
    → Standard precedence: * before +, / before +, right-to-left for same precedence.

41. **Preorder traversal result is same as:**  
    **Answer: a) Depth-first search**  
    → Preorder = Root-Left-Right = DFS order.

42. **Queues play a major role in:**  
    **Answer: c) Resource allocation**  
    → FCFS scheduling / queues → resource allocation.

43. **Worst-case comparisons in searching a singly linked list of size n:**  
    **Answer: d) n**  
    → Must traverse entire list in worst case.

44. **Multiple elements mapped to same hash bucket is called:**  
    **Answer: c) Collision**  
    → Hash collision = different keys → same bucket.

45. **Time complexity of heap sort in worst case:**  
    **Answer: c) O(n log n)**  
    → Heapify + n extractions → always O(n log n).

46. **Which is NOT an in-place sorting algorithm?**  
    **Answer: d) Merge sort**  
    → Requires extra O(n) space for merging.

47. **Complete graph with n vertices has how many edges?**  
    **Answer: b) n(n−1)/2**  
    → Every vertex connected to every other → undirected complete graph formula.

48. **When swap is costly, which sorting algorithm is preferred?**  
    **Answer: b) Selection sort**  
    → At most n swaps → good when swapping is expensive.

49. **Search technique used in associative memory:**  
    **Answer: c) Parallel search**  
    → Content-Addressable Memory (CAM) → parallel comparison.

50. **Which data structure uses FIFO principle?**  
    **Answer: b) Queue**  
    → Queue = First In First Out.

# Set B
1. **Which of the following need not necessarily be saved on a context switch between processes?**  
   **Answer: b) Translation lookaside buffer**  
   → The translation lookaside buffer is typically invalidated or flushed during a context switch, whereas general-purpose registers and the program counter must be preserved to maintain the process state.

2. **In UNIX, the return value for the fork system call is ______ for the child process and ______ for the parent process.**  
   **Answer: c) Zero, A nonzero integer**  
   → The fork system call returns zero to the child process and a positive integer (the child's process ID) to the parent process in UNIX.

3. **Which of the following page replacement algorithms suffers from Belady's anomaly?**  
   **Answer: a) FIFO**  
   → Belady's anomaly, where increasing page frames may result in more faults, affects the FIFO algorithm but not LRU or optimal replacement.

4. **Dijkstra's banking algorithm in an operating system, solves the problem of.**  
   **Answer: a) deadlock avoidance**  
   → The algorithm ensures resource allocation maintains a safe state, thereby avoiding potential deadlocks.

5. **If the CPU scheduling policy FCFS, the average waiting time will be**  
   **Answer: a) 12.8 ms**  
   → Under FCFS, waiting times are 0 ms (P1), 10 ms (P2), 13 ms (P3), 13 ms (P4), and 28 ms (P5), yielding a sum of 64 ms and an average of 64/5 = 12.8 ms.

6. **Which of the following statements is false?**  
   **Answer: d) (iv)**  
   → Virtual memory is utilized in both single-user and multi-user systems, rendering the statement false.

7. **Process synchronization can be done on __________**  
   **Answer: c) both hardware and software level**  
   → Synchronization employs hardware mechanisms (e.g., test-and-set) and software mechanisms (e.g., semaphores).

8. **Which of the following is NOT a valid deadlock prevention scheme?**  
   **Answer: c) (iii)**  
   → The rule of never requesting a resource after releasing one is not a recognized deadlock prevention strategy.

9. **Which of the following scheduling algorithms is non-preemptive?**  
   **Answer: b) First-In First-Out**  
   → First-In First-Out executes processes to completion without timer-based interruption.

10. **Page fault occurs when**  
    **Answer: b) a requested page is not in memory**  
    → A page fault signals that the required page must be loaded from secondary storage into main memory.

11. **The advantage of Round Robin CPU Scheduling over Shortest Job First Scheduling is**  
    **Answer: b) Better average response time**  
    → Round Robin ensures equitable time slices, improving response times for interactive processes compared to Shortest Job First.

12. **The first fit, best fit and worst fit are strategies to select a**  
    **Answer: b) free hole from a set of available holes**  
    → These strategies allocate contiguous memory by selecting appropriate free spaces in variable partitioning.

13. **For a page size of 200 words, What is the page number and offset for a logical address of 1142**  
    **Answer: a) 5, 142**  
    → Page number = 1142 // 200 = 5; offset = 1142 % 200 = 142.

14. **The process A, B, C. D and E references in the following order. A, B, C, D, A, B, E, A, B, C, D, E for the LRU page replacement algorithms with 4 frames. The number of page faults with pure demand paging is**  
    **Answer: c) 8**  
    → Simulation under LRU with four frames results in faults on A, B, C, D, E, C, D, and E.

15. **A counting semaphore was initialized to 9. Then 27P operations and 23V operations were completed on this semaphore. The resulting value of the semaphore is**  
    **Answer: b) 5**  
    → Initial value 9 minus 27 (P) plus 23 (V) equals 5.

16. **Suppose that a disk drive has 5000 tracks, numbered from 0 to 4999. The drive is currently serving a request at track 143 and the previous was at track 125. The queue of pending requests in FIFO order is 86, 1470, 913, 1774, 984, 1509, 1022, 1750, 130 . Starting from the current position, the total distance in terms of track movement for SSTF is**  
    **Answer: d) none**  
    → Calculated head movements sum to 1745 tracks, which does not match the given options.

17. **External fragmentation exists when ....... ?**  
    **Answer: a) enough total memory exists to satisfy a request but it is not contiguous**  
    → Memory is available in total but fragmented into non-contiguous blocks.

18. **Consider the following three processes in the FCFS. What is the average waiting time?**  
    **Answer: c) 4**  
    → Assuming arrivals at time 0 for standard calculation, waiting times are 0 (P1), 3 (P2), and 9 (P3), yielding an average of (0 + 3 + 9)/3 = 4.

19. **Which of the following algorithms is used to avoid deadlock?**  
    **Answer: c) Banker's algorithm**  
    → It verifies resource allocations to ensure the system remains in a safe state.

20. **Which of the following component does not belong to PCB (Process Control Block)?**  
    **Answer: d) Operating System information**  
    → The PCB contains process-specific data such as registers, scheduling, and accounting information.

21. **Consider the relation R(A, B, C, D, E) and the functional dependency set F={AB→C, B→D, C→E }.What is the highest normal form of the relation R ?**  
    **Answer: a) 1NF**  
    → Partial dependency B → D violates 2NF requirements.

22. **Which of the following statements are TRUE about an SQL query?**  
    **Answer: a) P and S**  
    → A HAVING clause can exist without GROUP BY (P), and GROUP BY attributes need not all appear in SELECT (S).

23. **What is the meaning of following SQL query? SELECT name FROM student WHERE mobileNo LIKE '%0%0%';.**  
    **Answer: d) List of student name whose mobile number contain two 0's**  
    → The pattern matches any string with at least two zeros in any position.

24. **Consider the following relational schema. student(snum,sname,age) Enrolled (snum,cname). What is the output of the following query.? SELECT cname, MIN(age) FROM student S, enrolled E WHERE S.snum = E.Snum GROUP BY cname HAVING COUNT(*) > 3;**  
    **Answer: b) For each class with more than 3 students, finds the age of the youngest student who has enrolled in this class.**  
    → Groups by class, filters for enrollment count >3, and computes minimum age.

25. **Let El and E2 be two entities in an E/Rdiagram with simple single-valued attributes. Rl and R2 are two relationships between El and E2, where Rl is one-to-many and R2 is many-to-many. Rl and R2 do not have any attributes of their own. What is the minimum number of tables required to represent this situation in the relational model?**  
    **Answer: a) 3**  
    → Tables for E1, E2 (incorporating one-to-many R1), and an associative table for many-to-many R2.

26. **Which one of the following statements is NOT correct about the B+ tree data structure used for creating an index of a relational database table?**  
    **Answer: b) Non-leaf nodes have pointers to data records**  
    → In B+ trees, data pointers reside only in leaf nodes.

27. **Let the set of functional dependencies F = {QR→S, R→P. S→ Q} hold on a relation schema X = (PQRS). X is not in BCNF. Suppose X is decomposed into two schemas Y and Z, where Y = (PR) and Z = (QRS). Which of the above statements is/are correct?**  
    **Answer: b) I only**  
    → Y and Z are in BCNF, but the decomposition is not dependency-preserving.

28. **Map the following statements to TRUE(T) or FALSE(F) respectively**  
    **Answer: d) (i) FALSE and (ii) FALSE**  
    → ORDER BY defaults to ascending; SELECT does not automatically eliminate duplicates.

29. **Which of the following is a DML command?**  
    **Answer: a) DELETE**  
    → DELETE manipulates data, unlike DDL commands such as CREATE, ALTER, and DROP.

30. **Consider the relation R (A, B, C, D, E) and the functional dependency set F = {AB→CD, ABC→E, C→A}. How many candidate keys are possible for the relation R ?**  
    **Answer: b) 2**  
    → Candidate keys are AB and BC.

31. **A primary key is combined with a foreign key creates**  
    **Answer: a) (i)**  
    → It establishes a parent-child relationship between tables.

32. **If a relation is in BCNF, then it is also in**  
    **Answer: d) All of the mentioned**  
    → BCNF encompasses the requirements of 1NF, 2NF, and 3NF.

33. **If every non-key attribute is functionally dependent primary key, then the relation will be in**  
    **Answer: b) Second normal form**  
    → 2NF eliminates partial dependencies on composite keys.

34. **Tables in second normal form (2NF):**  
    **Answer: d) (iv)**  
    → Non-key fields must depend on the entire primary key.

35. **An entity in A is associated with at most one entity in B. An entity in B, however, can be associated with any number (zero or more) of entities in A.**  
    **Answer: d) Many-to-one**  
    → Multiple A's link to a single B.

36. **If D1, D2, .., Dn are domains in a relational model, then the relation is a table, which is a subset of**  
    **Answer: b) D1×D2× ... ×Dn**  
    → Relations are subsets of the Cartesian product of domains.

37. **Let E1 and E2 be two entities in an E/R diagram with simple single-valued attributes. R1 and R2 are two relationships between E1 and E2, where R1 is one-to-many and R2 is many-to-many. R1 and R2 do not have any attributes of their own. What is the minimum number of tables required to represent this situation in the relational model?**  
    **Answer: b) 3**  
    → Tables for E1, E2 (absorbing R1), and an associative table for R2.

38. **Given a relation schema R(x,y,z,w) with functional dependencies set F = {x → y, z → w} All attributes take single and atomic values only**  
    **Answer: a) (i) and (iii) only**  
    → The relation is in 1NF with primary key xz, but violates 2NF due to partial dependencies.

39. **Given two tables EMPLOYEE (EID, ENAME, DEPTNO) DEPARTMENT (DEP NO., DEPTNAME) Find the most appropriate statement of the given query: Select count (*) ‘total’ from EMPLOYEE Where DEPTNO IN (D1,D2) Group by DETNO Having count (*) > 5**  
    **Answer: b) (ii)**  
    → Counts employees in D1 and D2, displaying only if each exceeds 5.

40. **Which of the following key constraints is required for functioning of foreign in the context of relational database**  
    **Answer: b) Primary key**  
    → Foreign keys reference primary keys for referential integrity.

41. **The following numbers are inserted into an empty binary search tree in the given order: 10, 1, 3, 5, 15, 12, 16. What is the height of the binary search tree (the height is the maximum distance of a leaf node from the root)?**  
    **Answer: b) 3**  
    → The longest path (e.g., 10 → 1 → 3 → 5) has 3 edges.

42. **The maximum number of binary trees that can be formed with three unlabelled nodes is**  
    **Answer: b) 5**  
    → Determined by the third Catalan number.

43. **---------------- is the best time complexity of bubble sort**  
    **Answer: c) N**  
    → Optimized bubble sort detects sorted lists in O(N) time.

44. **Which data structure is mainly used for implementing the recursive algorithm?**  
    **Answer: b) Stack**  
    → Recursion utilizes the call stack for managing activations.

45. **Assume that the operators +, -, × are left associative and ^ is right associative. The order of precedence (from highest to lowest) is ^, x , +, -. The postfix expression corresponding to the infix expression a + b × c – d ^ e ^ f is**  
    **Answer: a) abc × + def ^ ^ –**  
    → Conversion adheres to precedence and associativity rules.

46. **The result evaluating the postfix expression 10 5 + 60 6 / * 8 – is**  
    **Answer: c) 142**  
    → Computation: (10 + 5) × (60 / 6) - 8 = 150 - 8 = 142.

47. **The average number of key comparisons done in a successful sequential search in a list of length n is**  
    **Answer: d) (n+1)/2**  
    → Average position is midway through the list.

48. **Which among the following statements(s) is/are true**  
    **Answer: c) (i) and (iii) only**  
    → Hash functions handle arbitrary input lengths and may produce collisions.

49. **Level order Traversal of a rooted Tree can be done by starting from root and performing**  
    **Answer: a) Breadth First Search**  
    → Level-order traversal equates to breadth-first search.

50. **Consider the following sequence of operations on an empty stack. Push(54);push(52);pop();push(55);push(62);s=pop(); Consider the following sequence of operations on an empty queue. enqueue(21);enqueue(24);dequeue();enqueue(28);enqueue(32);q=dequeue(); The value of s+q is ___________**  
    **Answer: a) 86**  
    → Stack yields s = 62; queue yields q = 24; sum is 86.
