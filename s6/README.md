## 📝 Semester Syllabus To-Do List

**[CD](#cst-302-compiler-design)**<br><br>
**[IOT](#cgt-304-iot-and-smart-computing)**<br><br>
**[AAD](#cst-306-algorithm-analysis-and-design)**<br><br>
**[EH](#cgt-312-ethical-hacking)**<br><br>
**[IEFT](#hut-300-industrial-economics-and-foreign-trade)**<br><br>
**[CCW](#cgt-308-comprehensive-course-work)**<br><br>
---
### CST 302 Compiler Design

* **Module 1 (Introduction to Compilers and Lexical Analysis)**
    * [ ] Study analysis and synthesis phases of the source program.
    * [ ] Understand the phases of a compiler.
    * [ ] Review Compiler writing tools and Bootstrapping.
    * [ ] Master **Lexical analysis**: role, input buffering, specification, and recognition of tokens.
* **Module 2 (Introduction to Syntax Analysis)**
    * [ ] Understand the role of the syntax analyser and syntax error handling.
    * [ ] Review **context-free grammars**: derivation, parse trees, and ambiguity elimination.
    * [ ] Learn basic parsing approaches: eliminating left recursion and left factoring.
    * [ ] Study **Top-down parsing**: recursive descent, predictive parsing, and LL(1) grammars.
* **Module 3 (Bottom-Up Parsing)**
    * [ ] Study Handle pruning and Shift-reduce parsing.
    * [ ] Review Operator precedence parsing (concept only).
    * [ ] Master **LR parsing**: constructing SLR, LALR, and canonical LR parsing tables.
* **Module 4 (Syntax-Directed Translation and Intermediate Code Generation)**
    * [ ] Study **Syntax-directed translation**: S-attributed and L-attributed definitions, and bottom-up evaluation.
    * [ ] Analyze **Run-time environments**: source language issues, storage organization, and allocation strategies.
    * [ ] Understand **Intermediate code generation**: intermediate languages, graphical representations, three-address code, quadruples, and triples.
* **Module 5 (Code Optimization and Generation)**
    * [ ] Study **Code optimization**: principal sources, machine-dependent/independent, local/global optimizations.
    * [ ] Master **Code generation**: design issues, target language, and simple code generator.
* **Reading**
    * [ ] Read Aho, Sethi, & Ullman: *Compilers: Principles, Techniques, and Tools*.

---

### CGT 304 IOT and Smart Computing

* **Module 1 (Overview of Internet of Things)**
    * [ ] Define IoT, conceptual framework, and architectural view.
    * [ ] Study technology behind IoT, development boards, and the role of RFID, WSN, and M2M communication.
    * [ ] Understand the modified OSI model for IoT/M2M systems.
* **Module 2 (Communication Technologies)**
    * [ ] Study **Wireless communication**: NFC, RFID, Bluetooth (BR/EDR and BLE), ZigBee IP/SE 2.0, Wi-Fi, and GPRS/GSM cellular networks.
    * [ ] Study **Wired communication**: SPI, UART/USART, and I²C.
* **Module 3 (Hardware Components in IoT)**
    * [ ] Know pins and descriptions for **Arduino, Raspberry Pi, and NodeMCU**.
    * [ ] Learn working and pin details of common **IoT sensors** (temp, humidity, distance, light, sound, PIR, pressure, moisture).
    * [ ] Study **IoT actuators** (servo motors, DC motor, relay).
* **Module 4 (Data Acquiring, Organizing, Processing, and Analytics)**
    * [ ] Study IoT application layer terminologies.
    * [ ] Understand data acquiring, storage, and server management.
    * [ ] Learn organizing data in **distributed databases** and **transaction processing** (batch, streaming, interactive, real-time).
    * [ ] Master **Data analytics**: descriptive, predictive, and prescriptive.
* **Module 5 (Smart IoT Systems Case Study)**
    * [ ] Study case studies: smart farming, home automation, IoT in health, industrial automation, connected car, smart grid, wearables, and smart city street lighting.
* **Reading**
    * [ ] Read Kamal, R.: *Internet of Things: Architecture and Design Principles*.
    * [ ] Read Bahga, A., & Madisetti, V.: *Internet of Things: A Hands-on Approach*.

---

### CST 306 Algorithm Analysis and Design

* **Module 1 (Introduction to Algorithm Analysis)**
    * [ ] Understand criteria for analysing algorithms and **time/space complexity**.
    * [ ] Master **Asymptotic notations** ($O, \Omega, \Theta, o, \omega$) and classifying functions.
    * [ ] Learn analysis of **recursive algorithms**: recurrence equations, iteration, recursion tree, substitution, and **Master’s Theorem**.
* **Module 2 (Advanced Data Structures and Graph Algorithms)**
    * [ ] Study **AVL trees** (insertion/deletion with all rotations).
    * [ ] Study **Disjoint sets**: operations, union and find algorithms.
    * [ ] Master **Graph traversals**: DFS, BFS, strongly connected components, and topological sorting.
* **Module 3 (Divide & Conquer and Greedy Strategy)**
    * [ ] Study **Divide and Conquer**: control abstraction, 2-way merge sort, and **Strassen’s algorithm** for matrix multiplication (analysis).
    * [ ] Study **Greedy Strategy**: control abstraction, fractional knapsack.
    * [ ] Master **Minimum cost spanning tree** (Kruskal’s) and **Single-source shortest path** (Dijkstra’s) with analysis.
* **Module 4 (Dynamic Programming, Backtracking, and Branch & Bound)**
    * [ ] Master **Dynamic Programming**: optimality principle, **Matrix chain multiplication**, and **Floyd-Warshall algorithm** (analysis).
    * [ ] Study **Backtracking**: control abstraction and **N-Queens problem**.
    * [ ] Study **Branch and bound** for travelling salesman problem.
* **Module 5 (Introduction to Complexity Theory)**
    * [ ] Understand tractable/intractable problems.
    * [ ] Study **Complexity classes**: P, NP, **NP-hard, and NP-complete**.
    * [ ] Learn NP-completeness proof of **clique problem** and **vertex cover problem**.
    * [ ] Review **Approximation algorithms** (bin packing, graph colouring).
    * [ ] Understand **Randomized algorithms** (Monte Carlo, Las Vegas, randomized quicksort with analysis).
* **Reading**
    * [ ] Read Cormen et al.: *Introduction to Algorithms*.
    * [ ] Read Horowitz, Sahni, & Rajasekaran: *Fundamentals of Computer Algorithms*.

---

### CGT 312 Ethical Hacking

* **Module 1 (Security Fundamentals)**
    * [ ] Review Security fundamentals, testing, and hacker/cracker descriptions.
    * [ ] Study test plans, ethics, legality, and the attacker/ethical hacker process.
    * [ ] Understand security and the stack.
* **Module 2 (Footprinting and Scanning)**
    * [ ] Practice **Information gathering** and network range determination.
    * [ ] Learn active machine identification, open ports/access points, **OS fingerprinting**, services, and network mapping.
    * [ ] Define attack surface.
* **Module 3 (Hacking Windows and Various Attacks)**
    * [ ] Study techniques for **Hacking Windows**, network, web, and password hacking.
    * [ ] Analyze various **attacks**: input validation, SQL injection, buffer overflow, and privacy attacks.
* **Module 4 (Web Services and Intrusion Detection)**
    * [ ] Study Web services architecture and strategies for fraud prevention/website protection.
    * [ ] Master **Intrusion detection systems** (NIDS, HIDS).
    * [ ] Review penetration testing process and web services risk reduction.
* **Module 5 (Forensics)**
    * [ ] Study **Computer forensics**, journaling, standardized logging criteria, and the journal risk and control matrix.
    * [ ] Learn neural networks, misuse detection, and novelty detection.
* **Reading**
    * [ ] Read Gregg, M.: *Certified Ethical Hacker, Version 9*.
    * [ ] Read Grimes, R.: *Hacking the Hacker*.

---

### HUT 300 Industrial Economics and Foreign Trade

* **Module 1 (Basic Concepts and Demand and Supply Analysis)**
    * [ ] Understand Scarcity, choice, basic economic problems, PPC, and types of firms.
    * [ ] Master **Demand and its determinants**, law of demand, **elasticity of demand** (measurement and applications).
    * [ ] Study Supply, law of supply, equilibrium, consumer/producer surplus, taxation, and deadweight loss.
* **Module 2 (Production and Cost)**
    * [ ] Study **Production function**, law of variable proportion, and economies of scale.
    * [ ] Understand **Isoquants, isocost line**, and producer’s equilibrium.
    * [ ] Review **Cobb-Douglas production function**.
    * [ ] Master **Cost concepts** (social, private, external, explicit, implicit, sunk) and **Short-run/Long-run cost curves**.
    * [ ] Define revenue, shutdown point, and break-even point.
* **Module 3 (Market Structure)**
    * [ ] Study **Perfect and imperfect competition** (monopoly, monopolistic competition, oligopoly).
    * [ ] Analyze **Oligopoly** (kinked demand curve, collusive oligopoly).
    * [ ] Review **Product pricing** strategies: cost-plus, target return, penetration, predatory, going rate, and price skimming.
* **Module 4 (Macroeconomic Concepts)**
    * [ ] Understand **Circular flow of economic activities** and stock/flow concepts.
    * [ ] Master **National income** (GDP and measurement methods).
    * [ ] Study **Inflation**: causes, effects, and control measures (monetary and fiscal policies).
    * [ ] Review **Business financing**: bonds, shares, money market, capital market, stock market, SENSEX, and NIFTY.
* **Module 5 (International Trade)**
    * [ ] Understand advantages and disadvantages of international trade.
    * [ ] Study **Trade theories**: absolute and comparative advantage, Heckscher-Ohlin theory.
    * [ ] Master **Balance of payments** (components, deficit, devaluation).
    * [ ] Review **Trade policy**: free trade vs. protection, tariff, and non-tariff barriers.

---

### CGT 308 Comprehensive Course Work

* [ ] **Review Full Syllabus** of the following core courses:
    * [ ] Data Structures (CST201)
    * [ ] Operating Systems (CST206)
    * [ ] Database Management Systems (CST204)
    * [ ] Computer Networks (CST303)
    * [ ] Foundations of Cryptography (CGT307)
* [ ] **Refer to Textbooks** of the respective core courses.
