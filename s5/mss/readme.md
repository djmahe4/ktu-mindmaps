# MSS
[Mod1](#module-1)<br><br>
[Mod2](#module-2)<br><br>
[Mod3](#module-3)<br><br>
[Mod4](#module-4)<br><br>
[Mod5](#module-5)<br><br>
## Module 3

### I. Cluster 1: Software Verification Fundamentals (High Priority)

These are fundamental concepts necessary for answering both comparison questions (Part A) and detail questions (Part B).

#### 1. White Box vs. Black Box Testing

This is the most recurring comparison topic.

| Aspect | White Box Testing (Structural/Glass-box) | Black Box Testing (Functional/Behavioral) |
| :--- | :--- | :--- |
| **Focus** | Internal code logic, structure, paths, and flow. | External functionality, user requirements, inputs, and outputs. |
| **Knowledge** | Requires knowledge of the code structure and algorithms. | Requires no knowledge of internal code (treated as a black box). |
| **Who tests?** | Developers, programmers. | Testers, end-users, QA team. |
| **Goal** | Ensure all independent paths are executed and internal errors are found. | Verify the system meets the specifications/requirements. |
| **Techniques** | Basis Path Testing, Loop Testing, Data Flow Testing. | Equivalence Partitioning (EP), Boundary Value Analysis (BVA), Orthog. |

> ##### 💡 Mnemonic Tip:
> *   **W**hite Box sees the **W**orks (internal logic).
> *   **B**lack Box sees the **B**ehavior (user function).

#### 2. Black Box Techniques (EP and BVA)

These are commonly asked for definition and comparison in Q15 (Part B) or Part A.

*   **Equivalence Partitioning (EP):**
    *   **Definition:** Divides the input data into partitions (classes) where the system behavior is assumed to be similar. Only one test case is chosen from each partition.
    *   **Goal:** Reduce redundant test cases while ensuring coverage of all major input types (valid and invalid).
*   **Boundary Value Analysis (BVA):**
    *   **Definition:** Focuses on testing values exactly *at*, *just above*, and *just below* the edge (boundary) of equivalence partitions.
    *   **Goal:** Errors frequently cluster at the boundaries of input ranges. BVA is a high-yield method for finding these edge-case bugs.

> ##### 💡 Mnemonic Tip:
> **B**VA targets the **B**oundaries (edges).

#### 3. System Testing Variants

System testing verifies the complete, integrated system. (High Priority - Part A)

1.  **Functional Testing:** Checks if the system performs its specified requirements (what the user asked for).
2.  **Performance Testing:** Checks speed, stability, and responsiveness under various loads (includes Load and Stress testing).
3.  **Security Testing:** Checks protection mechanisms against unauthorized access, penetration, and malicious attacks.
4.  **Usability Testing:** Checks how easy and intuitive the system is for end-users (User Experience/UX).
5.  **Acceptance Testing (UAT/OAT):** Final testing done by the customer/client to ensure the system is ready for production.

---

### II. Cluster 2: Quality Reviews and Processes (High Priority for Q16)

These are key process-centric topics frequently asked in the detailed Part B questions.

#### 1. Formal Technical Review (FTR)

A structured software quality control activity performed by a team to uncover errors and ensure compliance with standards.

##### FTR Process Steps (Recurring Question)
The process is formal and sequential:

1.  **P**lanning (Set objectives, select team).
2.  **P**reparation (Reviewers study materials independently).
3.  **C**onducting the Review Meeting (Author presents; defects identified, **not solved**).
4.  **R**ecording Findings (Scribe documents all issues/defects).
5.  **R**eviewing Outcome (Decision on major/minor revisions; action items assigned).
6.  **F**ollow-up and Closure (Author fixes defects; verification ensures resolution).

> ##### 💡 Mnemonic Tip (The FTR Meeting Flow):
> **P**lease **P**repare **C**offee, **R**ecorder **R**eads **F**indings.

##### Objectives of FTR (Part A & B)
*   Uncover errors early (function, logic, implementation).
*   Verify compliance with requirements and standards.
*   Achieve uniform software development style.
*   Promote knowledge transfer and team training.

#### 2. Test Documentation

Essential for planning, tracking, resource management, and transparency. (Medium Priority)

| Document Type | Purpose |
| :--- | :--- |
| **Test Policy** | High-level organizational goal settings for testing. |
| **Test Plan** | Detailed document covering scope, approach, resources, and schedule for a specific project. |
| **Test Case** | Detailed steps, input values, and expected results for verifying a specific function. |
| **Traceability Matrix** | Links requirements to test cases (ensures all requirements are covered/tested). |
| **Defect Report** | Documenting any flaw that causes the system to fail its expected function. |

---

### III. Cluster 3: Evolution, Maintenance & Modern Practices (High Priority for Q16)

#### 1. Software Maintenance

Maintenance occurs after delivery to adapt or correct the software. (High Priority - Part A)

> ##### 💡 Mnemonic Tip (Types of Maintenance): **CAPP**

1.  **C**orrective Maintenance: Fixing defects, bugs, and errors found after deployment (e.g., fixing a crash).
2.  **A**daptive Maintenance: Modifying the software to cope with changes in the operating environment (OS, hardware, new libraries).
3.  **P**erfective Maintenance: Improving performance, functionality, or usability based on user feedback or optimization opportunities (adding a new feature).
4.  **P**reventive Maintenance: Proactive changes (like **Refactoring**) to improve reliability and maintainability, slowing down system degradation.

#### 2. Software Evolution Process

Describes how software adapts over time to meet changing needs. (Medium Priority)

**Stages (Cyclical Process):**
1.  **Change Identification:** System change proposals (fault reports, new requirements).
2.  **Impact Analysis:** Assessing the cost, risk, and benefit of implementing the change.
3.  **Release Planning:** Deciding which changes will be included in the next version/release.
4.  **Change Implementation:** Modifying the code and documentation (includes program understanding).
5.  **System Release:** Distributing the new version to customers.

#### 3. CI/CD/CD and DevOps

Automating the software pipeline to increase speed and reliability. (High Priority)

| Practice | Definition | Key Feature |
| :--- | :--- | :--- |
| **DevOps** | Integration of Development and Operations teams and processes, emphasizing automation and collaboration. | Principles: Automation, Measurement, Shared Responsibility. |
| **Continuous Integration (CI)** | Developers frequently merge code into a shared repository, triggering automated builds and tests immediately. | **Key Benefit:** Early detection of integration bugs ("Don't break the build"). |
| **Continuous Delivery (CD)** | Extends CI; code changes are validated, packaged, and kept in a *deployable state* at any time. | **Key Feature:** Ready for production, but **deployment requires manual approval**. |
| **Continuous Deployment (CD)** | Extends Continuous Delivery; every change that passes the automated pipeline is **automatically deployed to production.** | **Key Feature:** No manual approval step; fully automated release cycle. |

#### 4. Open Source Licensing

Defines the legal rights and restrictions for using, modifying, and distributing open-source code. (High Priority - Q15a or Part A)

> ##### 💡 Mnemonic Tip: Licensing Types

| License | Philosophy | Core Rule / Restriction |
| :--- | :--- | :--- |
| **GPL** (GNU General Public License) | **Strong Copyleft** | If you use GPL code, your entire derivative work (including your own additions) **must also be open-source (GPL licensed)**. |
| **LGPL** (Lesser GPL) | **Weak Copyleft** | Used mostly for libraries. Allows proprietary software to link to it **without forcing the proprietary code to be open-source**. |
| **BSD** (Berkeley License) | **Permissive** | Allows code to be used in proprietary products with **minimal restrictions** (often just attribution is required). Best for businesses who want to keep their source private. |

---

### 🗺️ Module 3 Mind Map for Memorization

Use this structure to connect concepts visually:

```mermaid
mindmap
  root((Module 3: Verification & Evolution))
    Testing Strategies
      Black Box (BB)
        Functional focus
        Techniques
          Equivalence Partitioning (EP)
          Boundary Value Analysis (BVA)
        BB vs WB (Comparison - H)
      White Box (WB)
        Internal Code focus
        Techniques
          Basis Path Testing (M)
          Loop Testing
        Basis Path Process (Steps)
      System Testing (H)
        Functional Testing
        Performance (Stress/Load)
        Security Testing
        Acceptance (UAT/OAT)
      Integration Testing (M)
        Top-Down (Uses Stubs)
        Bottom-Up (Uses Drivers)
    Quality Assurance & Review
      Formal Technical Review (FTR) (H)
        Process Steps (P-P-C-R-R-F)
        Objectives (Error detection, Compliance)
      Review Comparison (FTR vs Informal) (L)
      Test Documentation (M)
        Test Plan
        Traceability Matrix
        Purpose (Tracking/Transparency)
      Post Mortem Evaluation (PME)
    Evolution & Modern Practices
      Software Maintenance (H)
        Types
          Corrective (C)
          Adaptive (A)
          Perfective (P)
          Preventive (P)
        Evolution Process (Change Analysis/Implementation)
        Refactoring vs Re-engineering
      DevOps (H)
        Continuous Integration (CI)
        Continuous Delivery (CD - Manual Approval)
        Continuous Deployment (CD - Auto to Prod)
      Licensing (H)
        GPL (Strong Copyleft)
        LGPL (Weak Copyleft/Libraries)
        BSD (Permissive/Minimal Restriction)
```
## Module 4

### I. HIGH PRIORITY CORE TOPICS (PILLAR 2)

**Focus: SCM, Version Management, and Cost Estimation (Likely Q18/Q14)**

#### A. Software Configuration Management (SCM)

SCM is the discipline of controlling changes to software artifacts throughout the lifecycle to maintain integrity and consistency.

| Concept | Key Points to Remember | Mnemonics/Tips |
| :--- | :--- | :--- |
| **Definition (Part A/B)** | Set of policies, processes, and tools for managing changing software systems. Ensures that all versions are identified, tracked, and accessible. | SCM ensures **integrity, traceability, and accountability.** |
| **SCM Activities (Part B)** | Four fundamental activities required for managing a changing system: | **V S C R** (Very Secure Configuration Repository) |
| 1. **V**ersion Control | Tracks multiple versions of components; prevents different developers from overwriting each other's work. | *Key Feature:* Branching and Merging. |
| 2. **S**ystem Building | The process of assembling, compiling, and linking components (including external libraries and configuration files) to create an executable system. | Output is the executable system. |
| 3. **C**hange Management | Tracks and manages change requests (from customers/developers). Includes analyzing impact, costing, and deciding if/when changes are implemented. | Decision-making process. |
| 4. **R**elease Management | Preparing the software for external distribution to customers/users (System Release). Includes planning functionality and organizing software distribution. | Connects development to customer use. |

#### B. Cost Estimation Models (COCOMO)

| Concept | Key Study Points (Part B) | Mnemonics/Tips |
| :--- | :--- | :--- |
| **Techniques (Part A)** | 1. **Expert Judgment:** Relying on the experience/intuition of professionals. (Quick but subjective). 2. **Algorithmic Cost Modelling:** Using mathematical formulas (like COCOMO) based on size and complexity. (Systematic but relies on accurate inputs). | **E.J.** (Expert Judgment) is **Q.S.** (Quick/Subjective). |
| **COCOMO Model (Part B)** | **Constructive Cost Model.** Uses inputs like estimated size (KLOC) and cost drivers (M) to predict Effort (Person-Months) and time. | Formula Core: **$Effort = A \times (\text{Size})^B \times \prod(\text{EAF})$** (A, B are constants, EAF is Effort Adjustment Factor/M). |
| **Problems of Algorithmic Models (Q17/Q18 context)** | 1. **Inaccurate Input:** Hard to estimate size (KLOC) accurately early on. 2. **Subjective Multipliers (M):** Factors like complexity, reliability, and team experience are subjective. 3. **Lack of Adaptability:** Doesn't handle dynamic projects or frequently changing requirements well. | **S I M** (Size, Input, Multipliers are problems) |

#### C. Factors Affecting Software Pricing (Part A/B)

Pricing is determined by costs plus profit, but is heavily influenced by external factors.

| Factor | Explanation |
| :--- | :--- |
| **Contractual Terms** | If the developer retains source code ownership (for reuse), the price might be lower. |
| **Cost Estimate Uncertainty** | If estimates are uncertain (risky), the organization adds a contingency margin, increasing the price. |
| **Financial Health** | Companies in financial distress might lower the price (pricing to win) to ensure cash flow, accepting lower profit. |
| **Market Opportunity** | A company might quote a low price to enter a new market segment, hoping for higher profits later via experience/new products. |
| **Requirements Volatility** | If requirements are expected to change frequently, the initial price may be low, but high prices will be charged for later changes. |

***

### II. MEDIUM/HIGH PRIORITY TOPICS (PILLAR 1 & CROSS-MODULE)

**Focus: Part A (3 Marks) Definitions & Part B Plan-Driven Concepts (Likely Q17)**

#### A. Risk Management

| Concept | Key Study Points (Part A) | Mnemonics/Tips |
| :--- | :--- | :--- |
| **Risk Definition (Part A)** | An uncertainty (event or condition) that, if it occurs, has a negative effect on project objectives (scope, schedule, quality, cost). | Risk is **Uncertainty + Loss.** |
| **Types of Risk (Part A)** | 1. **P**roject Risk (Affects budget/schedule, e.g., scope creep, staff turnover). 2. **T**echnical Risk (Affects quality/delivery, e.g., design complexity, unreliable component). 3. **B**usiness Risk (Affects organizational viability, e.g., new competitor, market change). | **PTB** (Project, Technical, Business) |
| **Risk Management Process (Part B - Q17 Focus)** | The process involves four main steps: | **I A P M** (I Am Project Manager) |
| | 1. **I**dentification (Brainstorm potential risks). 2. **A**nalysis (Assess probability and impact/severity). 3. **P**lanning (Mitigation/Contingency strategies: Avoidance, Minimization, Contingency). 4. **M**onitoring (Tracking risks continuously). | Diagram: Cyclical flow is often required for 7M. |

#### B. Project Planning and Scheduling

| Concept | Key Study Points (Part A/B) | Mnemonics/Tips |
| :--- | :--- | :--- |
| **Fundamental Project Management Activities (Part A)** | Activities required to execute and control the project successfully: | **P P R M** (People Plan, Risk Manage) |
| | 1. **P**roject **P**lanning (Scheduling, estimation). 2. **P**eople **M**anagement (Team leadership, motivation). 3. **R**isk Management (Anticipating failures). 4. **R**eporting & **M**onitoring (Tracking progress and communication). | |
| **Critical Path (Part B - Q17 focus)** | The longest sequence of dependent activities in a project network that determines the earliest time the project can be completed. Tasks on the critical path have zero slack. | Delaying a Critical Path task delays the *entire project*. |
| **Plan-Driven Development (Part B)** | Process is planned in detail upfront (like Waterfall). Decisions are made early. High control, high documentation, but low flexibility to change. | Contrast this with Agile (high flexibility, incremental). |

#### C. Agile Management

| Concept | Key Study Points (Part A) | Mnemonics/Tips |
| :--- | :--- | :--- |
| **SCRUM Framework (Part A/B)** | An agile framework focusing on iterative development through fixed-length cycles (Sprints). | Define Roles (PO, SM, Team) and Artifacts (Backlogs). |
| **Role of Backlogs/Sprints (Part A)** | 1. **Product Backlog:** Prioritized list of all requirements/features. (The "What"). 2. **Sprint Backlog:** Subset of tasks chosen from the Product Backlog for the current Sprint. (The "How much in this cycle"). | Sprint = Time-boxed iteration (2-4 weeks). |
| **Kanban/Lean Approaches (Part B - Q17 focus)** | **Kanban:** Focuses on flow and limiting Work-In-Progress (WIP) using visual boards. **Lean:** Philosophy focused on maximizing customer value while minimizing waste. | Lean Principles: Eliminate waste, Amplify learning, Decide late, Deliver fast, Empower team, Build integrity, Optimize the whole. |

***

### 📊 Summary of Topic Frequency and Priority

| Topic | Primary Question Type | Frequency (QPs) | Priority for Exam Focus |
| :--- | :--- | :--- | :--- |
| **SCM Definition & Activities** | Part B (10M), Part A (3M) | 4/6 | **P1 (Master for Part B)** |
| **COCOMO / Algorithmic Models** | Part B (7M), Part A (3M) | 4/6 | **P1 (Master for Part B)** |
| **Risk Management Process** | Part B (7M/10M) | 3/6 | **P2 (Study basics for Q17, but skip if prioritizing Q18)** |
| **Risk Categories/Types** | Part A (3M) | 5/6 | **P1 (Must know for Part A)** |
| **Project Management Activities** | Part A (3M) | 5/6 | **P1 (Must know for Part A)** |
| **SCRUM (Backlogs/Sprints)** | Part A (3M) | 4/6 | **P1 (Must know for Part A)** |
| **Pricing Factors** | Part A (3M) | 3/6 | **P2 (Medium)** |
| **Critical Path / Scheduling** | Part B (7M) | 2/6 | P3 (Skippable for Part B strategy) |
## Module 5

### **I. High-Priority Core Concepts (Master First)**

This covers SQA, CMMI/ISO, and Microservices, which are highly likely to appear in both Part A (3M) and Part B (7M) questions.

#### **A. Software Quality Assurance (SQA) & Quality Models**

**1. Definition and Goal:**
*   SQA is the infrastructure (policies, processes, tools) established to manage software quality throughout the entire development lifecycle.
*   **Goal:** Ensure the software process and products conform to standards and requirements, leading to high-quality software that delivers value.
*   *Mnemonic: SQA provides the 4 I's:* **I**nfrastructure, **I**nsight, **I**nformation, and **I**mproved quality.

**2. Elements/Tasks of SQA (Checklist/Auditing Role):**
The SQA group (often independent) performs these tasks:
*   **Standards:** Ensure that organization and project standards (e.g., coding, documentation) are **followed**.
*   **Reviews/Audits:** Conduct technical reviews to uncover errors (quality control) and audits to ensure compliance with quality guidelines.
*   **Testing:** Ensure testing is properly **planned and executed** to maximize error detection.
*   **Error/Defect Analysis:** Collect data on errors to understand *how* they occur and determine the best elimination methods.
*   **Change Management:** Ensure that changes are properly managed and documented to prevent the introduction of new defects.
*   **Risk Management:** Ensure risk activities are properly conducted and contingency plans are in place.

| 3 Marks Tip: Elements of SQA | **S**tandards, **R**eviews/Audits, **T**esting, **E**rror Analysis, **C**hange Mgmt, **R**isk Mgmt. |
| :--- | :--- |

**3. Achieving Software Quality (Four Broad Activities):**
Software quality results from combining four pillars:
1.  **Software Engineering Methods:** Understanding the problem and using rigorous design/coding practices.
2.  **Project Management Techniques:** Using estimation, scheduling, and risk planning to avoid shortcuts.
3.  **Quality Control Actions:** Activities like **reviews, inspections, and testing** applied early and consistently.
4.  **Quality Assurance (SQA):** Providing the oversight and infrastructure to ensure the above three are effective.

#### **B. Capability Maturity Model Integration (CMMI)**

**1. CMMI Overview:**
*   CMMI is a **process meta-model** (framework) that guides organizations in improving the maturity and capability of their software development processes.
*   It uses a **staged representation** (5 levels) to measure organizational maturity.

**2. The Five Maturity Levels (Must Memorize):**
*   *Mnemonic: **I**nterested **M**anagers **D**efine **Q**uality **O**utcomes* (Initial, Managed, Defined, Quantitatively Managed, Optimizing).

| Level | Name | Characteristic | Focus / Process State |
| :--- | :--- | :--- | :--- |
| **1** | **Initial (Chaotic)** | Ad-hoc, unpredictable, reactive. | Success relies on individual heroes, not repeatable processes. |
| **2** | **Managed** | Processes are planned, performed, and controlled **at the project level**. | Work products are defined, monitored, and reviewed. (Project-specific policies). |
| **3** | **Defined** | Processes are **standardized across the organization**. | Standard processes are tailored for specific projects. Training and documentation are organizational assets. |
| **4** | **Quantitatively Managed** | Process performance is controlled using **statistical and quantitative techniques**. | Focus is on achieving measurable quantitative goals for quality and process performance. |
| **5** | **Optimizing** | Focuses on **continuous process improvement**. | Processes are adapted and optimized using statistical feedback and piloting innovative ideas. |

**3. ISO 9001:2000 vs. CMMI:**
*   **ISO 9001:** Generic QMS standard. Focuses on *if* you have a defined system (binary: compliant/not compliant). Applicable to *any* industry.
*   **CMMI:** Software-specific framework. Focuses on *how well* you manage your processes (5 levels of maturity).

#### **C. Microservices Architecture**

**1. Characteristics (3 Marks Tip):**
*   Small-scale services, each focused on a single business function.
*   **Self-contained:** Manage their own data and UI (no shared database).
*   **Implementation-independent (Polyglot):** Can use different languages/technologies.
*   **Independently Deployable:** Deployable using automated systems without affecting other services.
*   **Resilient (Fault Isolation):** Failure in one service does not crash the entire system.

**2. Key Design Principles (Why Microservices are Good):**
*   **Low Coupling:** Services rely minimally on each other, communicating via explicit messages/APIs. (Changes in one service don't break others).
*   **High Cohesion:** The internal elements of a service are strongly related and focused on one responsibility. (Easier to understand and maintain).

**3. Service Communications (Must Know):**
*   Microservices communicate by exchanging messages.
    *   **Synchronous:** (e.g., REST/HTTP). Client waits for a response. Simple, but higher risk of cascading failure.
    *   **Asynchronous (Choreography):** (e.g., Message Queues, Event-Driven). Services emit events, and other services react accordingly. Highly decoupled, improves resilience.

---

### **II. Medium-Priority Topics (Part B Q20 & Detailed Part A)**

These topics are often combined with the core topics to form the second Part B question (Q20) or appear as detailed Part A questions.

#### **D. Software Process Improvement (SPI)**

**1. SPI Process (Five Iterative Steps):**
SPI is a method to transform an "as-is" process into a "to-be" process.

| Step | Activity | Purpose |
| :--- | :--- | :--- |
| **1** | **Assessment & Gap Analysis** | Evaluate the **current process** (often using CMMI) to identify strengths and weaknesses ("gaps") compared to best practices. |
| **2** | **Education & Training** | Train practitioners and managers on the new process concepts and tools. |
| **3** | **Selection & Justification** | Choose the most suitable process model, methods, and tools for the organization. |
| **4** | **Installation & Migration** | Implement the chosen changes, often via a pilot project first. |
| **5** | **Evaluation & Tuning** | Assess the degree of adoption and the measurable business benefit (ROI). Tune the process for continual improvement. |

**2. Elements of an SPI Framework (3 Marks):**
1.  **Defined Process Characteristics:** What an effective process should look like (e.g., CMMI KPAs).
2.  **Assessment Method:** A procedure to evaluate the current process against these characteristics.
3.  **Mechanism for Summarizing Results:** Providing an indication of **process maturity**.
4.  **Strategy for Implementation:** Guidance on how to address missing or weak characteristics.

#### **E. Cloud-Based Software and Virtualization**

**1. Characteristics of Cloud Software (3 Marks):**
*   *Mnemonic: **RESUME** (Resilience, Elasticity, Scalability, Utility/Measured Service, Multi-tenancy/Resource Pooling, Ease of use/On-Demand).*
    *   **Scalability:** Cope with increasing load (scaling up/out).
    *   **Elasticity:** Scale **up and down dynamically** based on demand (pay only for what you need).
    *   **Resilience:** Architecture tolerates server failures (redundancy/fault isolation).

**2. Cloud Service Levels (Basic and Intermediate):**
*   **Basic/Foundational:** **IaaS (Infrastructure as a Service):** Provides VMs, storage, networking. **You manage:** OS, applications, data.
*   **Intermediate:** **PaaS (Platform as a Service):** Provides OS, databases, web servers, frameworks. **You manage:** Applications, data.
*   **Highest Level:** **SaaS (Software as a Service):** Provides the entire application (e.g., Gmail). **You manage:** User configuration.

**3. Virtualization vs. Containerization:**
*   **Virtualization (VMs):** Uses a **hypervisor**. Each VM has its own **Guest OS and kernel**. Provides strong isolation. Slower startup (minutes).
*   **Containerization (e.g., Docker):** Uses **OS-level virtualization**. Containers **share the host OS kernel**. Lightweight, fast deployment (seconds). Efficient for service-oriented architectures.

---

### **III. Memorization Tools (Mind Map)**

Use this simplified mind map to recall the relationships between the high-priority topics:

```mermaid
mindmap
  root((Module 5: Quality, Process, Arch.))
    Software Quality
        SQA (Oversight/Infrastructure)
            Elements (SRT-ECR)
            How Achieved (Methods, Mgmt, QC, SQA)
        Quality Models
            CMMI (Process Maturity)
                Levels (IMDQO)
            ISO Standards (QMS Certification)
                ISO 9001 (Compliance)
                ISO 9126 (Attributes: Functionality, Reliability, etc.)
    Process Improvement (SPI)
        SPI Process (5 Steps)
            1. Assessment (Find Gap)
            2. Education (Train)
            3. Selection (Choose Model)
            4. Installation (Implement)
            5. Evaluation (Measure ROI/Tune)
    Microservices Architecture
        Design Principles
            Low Coupling (Decouple for independent deployment)
            High Cohesion (Single Responsibility Focus)
        Characteristics
            Self-Contained (Own Data)
            Independently Deployable
            Polyglot (Implementation Independent)
        Communication
            Synchronous (REST)
            Asynchronous (Choreography/Events)
    Technology Trends (Deployment)
        Cloud Services (Features: Elasticity, Scalability)
            IaaS (VMs, You manage OS)
            PaaS (Platform, You manage App)
            SaaS (Software, Vendor manages all)
        Virtualization
            VMs (Heavy, Separate OS)
            Containers (Lightweight, Shared Kernel)
```

```
