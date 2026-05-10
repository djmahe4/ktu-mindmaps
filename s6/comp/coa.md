## Module 1: Basic Structure of Computers

This module introduces the fundamental building blocks of a computer system.

#### 1. Basic Structure of Computers: Functional Units and Basic Operational Concepts

*   **Functional Units:** A computer is typically organized into several functional units, each with a specific role. These usually include:
    *   **Input Unit:** To enter data and instructions into the computer.
    *   **Output Unit:** To display or present the results of computation.
    *   **Memory Unit:** To store data and programs.
    *   **Arithmetic Logic Unit (ALU):** To perform arithmetic and logical operations.
    *   **Control Unit (CU):** To manage and coordinate all the operations of the computer.
    *   The **ALU** is identified as the computational center of the CPU.
*   **Basic Operational Concepts:** These units work together in a coordinated manner to execute tasks. The CPU (Central Processing Unit) fetches instructions from memory, decodes them, executes them, and stores the results.

#### 2. Bus Structures

*   **Definition:** A bus is a communication pathway connecting two or more devices. It's a collection of wires through which data, addresses, and control signals are transmitted.
*   **Types of Buses:**
    *   **Address Bus:** Carries the memory address of the data or instruction that the CPU wants to access.
    *   **Data Bus:** Carries the actual data between the CPU, memory, and I/O devices.
    *   **Control Bus:** Carries control signals from the CPU to other devices to coordinate operations (e.g., read/write signals, interrupt requests).
*   **Single Bus vs. Multiple Bus Structures:**
    *   **Single Bus Structure:** All functional units are connected to a single common bus. This simplifies wiring and reduces cost but can become a bottleneck as only one transfer can happen at a time. The main advantage of a single bus structure is its cost-effective connectivity and ease of attaching peripheral devices.
    *   **Multiple Bus Structure:** Uses multiple buses to allow simultaneous transfers, improving performance. Your question bank implies that **multiple bus structures** allow two or more transfers at a time.
    *   A key difference between single bus and multiple bus structures is **Performance**.
    *   I/O devices are connected to the CPU via a **BUS**.
    *   The primary function of the BUS is to connect the various devices to the CPU, to provide a path for communication between the processor and other devices, and to facilitate data transfer between various devices. In essence, it performs **all of the mentioned** functions.
    *   The **SCSI Bus** is mentioned as a bus used to connect the monitor to the CPU.

#### 3. Memory Locations and Addresses, Memory Operations

*   **Memory Locations and Addresses:** Main memory is organized as a collection of individually addressable locations. Each location has a unique address.
    *   An address in main memory is called a **Physical address**.
*   **Memory Operations:** The CPU performs read and write operations on memory.
    *   **Read Operation:** Fetches data from a specified memory location.
    *   **Write Operation:** Stores data into a specified memory location.
    *   **RAM (Random Access Memory)** is volatile; its contents are lost when power is removed, making it unsuitable for permanent storage.
    *   **Static RAM (SRAM)** consists of circuits capable of retaining their state as long as power is applied.

#### 4. Instructions and Instruction Sequencing, Addressing Modes

*   **Instructions:** These are commands that the CPU understands and executes. An instruction typically consists of an opcode (operation code) and operands (data or addresses of data).
*   **Instruction Sequencing:** The order in which instructions are executed. The Program Counter (PC) holds the address of the next instruction to be fetched.
*   **Addressing Modes:** These define how the operand's effective address is calculated.
    *   **Immediate Addressing Mode:** The operand value is directly specified within the instruction. "SUB A, #10" is an example.
    *   **Index Addressing Mode:** Uses a base register plus an offset to calculate the memory address. The instruction "MOV 5(R1), LOC" has an effective address of **EA = 5 + R1**.
    *   **Relative Addressing Mode:** Uses the Program Counter (PC) instead of a general-purpose register to calculate the address, typically an offset from the current PC value.
    *   When using auto-increment or auto-decrement addressing modes, in auto-increment, the operand is retrieved first, and then the address is altered.
    *   In assembly language programming, a minimum of **zero** operands is required for an instruction.
    *   The decoded instruction is stored in the **Instruction Register (IR)**.
    *   The **Program Counter (PC)** keeps track of the instructions stored in memory.

#### 5. Basic Processing Unit: Instruction Cycle

*   **Instruction Cycle:** The fundamental process by which a computer executes instructions. It generally involves these phases:
    1.  **Fetch:** The CPU fetches the instruction from memory, whose address is pointed to by the Program Counter (PC).
    2.  **Decode:** The fetched instruction is decoded to determine what operation needs to be performed and what operands are involved.
    3.  **Execute:** The actual operation is performed (e.g., arithmetic calculation, data transfer).
    4.  **Write-back/Store:** The results of the execution are written back to memory or registers.
*   This cycle is critical for the execution of a complete instruction.

