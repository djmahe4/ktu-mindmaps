## Module 5

| Mechanism           | CPU Involvement     | Speed     | Use Case                |
|---------------------|---------------------|-----------|-------------------------|
| Programmed I/O      | High (polling)      | Slow      | Small, slow devices     |
| Interrupt-Driven I/O| Medium (ISR)        | Moderate  | General I/O (e.g., disk)|
| DMA                 | Low (setup only)    | Fast      | Large transfers         |

### Table: Mechanisms for Accessing I/O Devices

| **Aspect**               | **Programmed I/O**                                                                 | **Interrupt-Driven I/O**                                                                 | **Direct Memory Access (DMA)**                                                                 |
|--------------------------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| **Description**          | The CPU actively controls I/O by polling the device’s status and transferring data manually. | The CPU initiates I/O but waits for an interrupt from the device to handle data transfer via an ISR. | A DMA Controller (DMAC) transfers large data blocks directly between I/O device and memory, with minimal CPU involvement. |
| **Process**              | 1. CPU sends command to device (e.g., “read keypress”).<br>2. CPU polls status register until device is ready.<br>3. CPU transfers data between device and memory.<br>4. Repeat until complete. | 1. CPU sends command to device (e.g., “read 4 KB from disk”).<br>2. CPU continues other tasks.<br>3. Device raises interrupt when ready.<br>4. CPU saves PC/PSW, executes ISR to transfer data, restores state.<br>5. Resume original task. | 1. CPU programs DMAC with source, destination, size.<br>2. DMAC requests bus, transfers data directly.<br>3. DMAC interrupts CPU upon completion.<br>4. ISR confirms transfer or handles errors.<br>5. CPU resumes tasks. |
| **Role of Interrupts**   | No interrupts used; CPU polls continuously, no asynchronous signaling.             | Central role: Device raises interrupt to signal data readiness. ISR handles transfer, checks errors, and clears interrupt. Priority and masking manage multiple devices. | Interrupts used only at completion: DMAC sends interrupt to CPU to signal transfer is done. ISR verifies or handles errors. |
| **Advantages**           | - Simple to implement.<br>- Suitable for slow devices with small data (e.g., keyboard). | - CPU free during I/O, improving efficiency.<br>- Supports multitasking with multiple devices.<br>- Handles asynchronous I/O effectively. | - Fastest for large transfers.<br>- Minimal CPU involvement, freeing it for other tasks.<br>- Efficient for bulk data (e.g., disk I/O). |
| **Disadvantages**        | - CPU busy polling, wasting cycles.<br>- Inefficient for large or slow transfers.   | - Interrupt overhead (context switching) for frequent small transfers.<br>- Less efficient for very large data blocks compared to DMA. | - Complex hardware (DMAC required).<br>- Bus contention if CPU needs bus during transfer. |
| **Use Case**             | Slow devices with small data, e.g., reading a keypress from a keyboard.            | General I/O operations, e.g., disk reads, network packets, where CPU multitasking is needed. | Large, high-speed transfers, e.g., transferring a 1 MB file from disk to RAM or video streaming. |
 | **Example**              | CPU polls keyboard status to detect a keypress and reads the character.            | CPU initiates disk read, continues tasks, handles interrupt to move 4 KB to memory.      | DMAC transfers 1 MB video file from disk to RAM, interrupts CPU when done. |

 ### Asynchronous Synchronous Dram

| **Feature**               | **Asynchronous DRAM**                              | **Synchronous DRAM (SDRAM)**                       |
|---------------------------|---------------------------------------------------|--------------------------------------------------|
| **Definition**            | DRAM where operations are not synchronized with a system clock, relying on internal timing. | DRAM where all operations are synchronized with the system clock for precise timing. |
| **Timing Mechanism**      | CPU sends address and control signals (Row Address Strobe (RAS), Column Address Strobe (CAS), Write Enable (WE)) independently. Memory responds after variable delays. | All signals (address, data, commands) are latched on clock edges, ensuring predictable timing. |
| **Performance**           | Slower due to asynchronous nature, causing synchronization overhead. Access time depends on DRAM’s internal delays (e.g., 70-100 ns). | Faster due to clock synchronization, enabling pipelined operations and burst transfers. Access time aligns with clock cycles (e.g., 5-10 ns for DDR4). |
| **Data Transfer**         | Sequential access, limited by RAS/CAS delays. Examples: Fast Page Mode (FPM) DRAM, Extended Data Out (EDO) DRAM. | Supports burst transfers and double data rate (e.g., DDR transfers data on both rising and falling clock edges). Examples: SDR SDRAM, DDR3, DDR4, DDR5. |
| **Bandwidth**             | Lower bandwidth due to single-cycle transfers and delays. Typical: 100-200 MB/s for EDO DRAM. | Higher bandwidth due to pipelining and DDR. Typical: 25-50 GB/s for DDR4. |
| **Interface Complexity**  | Simpler interface, fewer control signals, but requires CPU to handle timing variations. | More complex interface with clock signal and command inputs (CS, RAS, CAS, WE interpreted on clock edges). |
| **Applications**          | Used in older systems (1980s-1990s PCs) where cost was prioritized over speed. | Standard in modern systems (laptops, desktops, servers) requiring high-speed memory access. |

### Cache hit/miss

| Operation | Hit Condition | Miss Condition | Policy |
|-----------|---------------|----------------|--------|
| Read      | Read directly | Fetch block from memory, load to cache | - |
| Write     | Write to cache (and memory if write-through; dirty bit set if write-back) | Fetch to cache then write (write-allocate) or write to memory only (no-write-allocate) | Write-Through, Write-Back (hit); Write-Allocate, No-Write-Allocate (miss) |

### Mapping
| Mapping Type        | Mapping Rule                                      | Address Breakdown           | Pros                                | Cons                    | Example (Block 70)         |
|---------------------|---------------------------------------------------|------------------------------|--------------------------------------|--------------------------|-----------------------------|
| Direct              | One block to one line (Index = Block MOD Lines)   | Tag (6), Index (6), Offset (4) | Simple, fast, low cost               | High conflict misses     | Maps to line 6              |
| Fully Associative   | Any block to any line                             | Tag (12), Offset (4)          | Flexible, low conflict misses        | Complex, expensive, slow | Any line (e.g., 10)         |
| Set-Associative (2-way) | One block to any line in a set (Set = Block MOD Sets) | Tag (7), Set (5), Offset (4)   | Balanced flexibility, fewer conflicts | Moderate complexity      | Set 6 (line 12 or 13)       |

## Module 4
### Hardwired vs microprogramed control

| **Feature**               | **Hardwired Control**                              | **Microprogrammed Control**                       |
|---------------------------|---------------------------------------------------|--------------------------------------------------|
| **Speed**                 | Faster (direct logic, minimal delay).             | Slower (microcode fetching adds overhead).       |
| **Design Complexity**     | Complex, error-prone for large instruction sets.  | Simpler, software-like, easier to debug.         |
| **Flexibility**           | Inflexible, hard to modify instructions.          | Flexible, easy to update via microcode.          |
| **Chip Area**             | Smaller for simple instruction sets.              | Larger due to control memory.                    |
| **Cost of Changes**       | Expensive (requires hardware redesign).           | Low (update microcode in memory).                |
| **Use Case**              | RISC processors, embedded systems with fixed instructions. | CISC processors, systems needing frequent updates or emulation. |
---

### Table: Comparison of Control Unit Design Methods

| **Method**                     | **Definition**                                                                 | **Operation**                                                                                       | **Advantages**                                                                 | **Disadvantages**                                                                 |
|--------------------------------|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| **One Flip-Flop per State**    | A hardwired control method where each control state has a dedicated flip-flop to indicate the active state. | One flip-flop is set to 1 per state, others are 0. Combinational logic generates control signals based on the active flip-flop and inputs (e.g., opcode). | Simple for small state machines. Fast (direct hardware). Low latency for state transitions. | Inefficient for many states (requires many flip-flops). Complex logic for large systems. Not scalable. |
| **Sequence Register and Decoder** | A hardwired control method using a register to hold the current state and a decoder to generate control signals. | Sequence register stores state code. Decoder converts state code to a unique signal, fed to combinational logic for control signals. | Fewer flip-flops than one flip-flop per state. Scalable for moderate state counts. Structured design. | More complex than one flip-flop method. Decoder and logic design can be intricate for many states. |
| **PLA Control**                | A hardwired control method using a Programmable Logic Array (PLA) to generate control signals based on state and inputs. | PLA (AND-OR array) maps current state and inputs (e.g., opcode) to control signals. State transitions are encoded in PLA. | Compact for complex control logic. Flexible for small changes (reprogram PLA). Efficient for many signals. | Slower than pure hardwired (PLA access time). Limited by PLA size. Requires reprogramming for changes. |
| **Microprogram Control**       | A control method using microinstructions (control words) stored in control memory to generate control signals. | Microprogram counter fetches control word from memory. Each word’s fields (e.g., ALU, register select) produce signals. | Highly flexible (modify microcode). Easy to design/debug complex instructions. Supports emulation. | Slower (memory fetch overhead). Requires control memory (adds cost/area). Complex for simple systems. |

## Module 3

### Table: Hazard Resolution Techniques in Pipeline Processors

| **Hazard Type** | **Definition** | **Example** | **Resolution Techniques** |
|-----------------|----------------|-------------|---------------------------|
| **Structural Hazard** | Occurs when multiple instructions compete for the same hardware resource (e.g., memory, ALU) in the same cycle. | Two instructions in a 5-stage pipeline (IF, ID, EX, MEM, WB) both need the memory unit in the MEM stage simultaneously. | 1. **Resource Duplication**: Add more resources (e.g., separate instruction and data caches to avoid memory conflicts).<br>2. **Stalling**: Insert a stall (bubble) to delay one instruction, allowing the resource to free up.<br>3. **Resource Scheduling**: Design the pipeline to avoid conflicts (e.g., interleaved memory access). |
| **Data Hazard** | Occurs when an instruction depends on the result of a previous instruction that hasn’t completed, causing incorrect data access. | Instruction 1: `ADD R1, R2, R3` (writes R1 in WB). Instruction 2: `SUB R4, R1, R5` (needs R1 in EX), causing a read-after-write (RAW) dependency. | 1. **Forwarding (Bypassing)**: Pass the result directly from a later stage (e.g., EX or MEM) to the dependent stage (e.g., EX) without waiting for WB.<br>2. **Stalling**: Insert stalls to delay the dependent instruction until the data is available.<br>3. **Instruction Reordering**: Compiler reorders instructions to avoid dependencies.<br>4. **Register Renaming**: Use different physical registers to eliminate false dependencies (used in advanced CPUs). |
| **Control Hazard** | Occurs when a branch instruction disrupts the pipeline flow, as the next instruction to fetch is unknown until the branch is resolved. | A branch instruction `BRN Target` (branch if negative) in the EX stage, but the pipeline fetches the next instruction in IF, which may be incorrect. | 1. **Branch Prediction**: Predict branch outcome (e.g., taken/not taken) and fetch accordingly. If wrong, flush pipeline.<br>2. **Delayed Branching**: Execute instructions in the branch delay slot (fixed number of cycles) before branching.<br>3. **Stalling**: Stall the pipeline until the branch outcome is resolved.<br>4. **Speculative Execution**: Execute predicted path speculatively, rollback if incorrect (advanced CPUs). |

## Module 2

### Comparison of Single Cycle, Multiple Cycle, and Pipeline Processor Designs

**Overview**:
- **Single Cycle**: Executes each instruction in one clock cycle using dedicated hardware for all stages.
- **Multiple Cycle**: Breaks instruction execution into multiple steps, each taking one clock cycle, sharing hardware resources.
- **Pipeline**: Overlaps execution of multiple instructions by dividing them into stages, processing different instructions concurrently.

---

### Table: Comparison of Single Cycle, Multiple Cycle, and Pipeline Designs

| **Aspect**               | **Single Cycle**                                                                 | **Multiple Cycle**                                                               | **Pipeline**                                                                     |
|--------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| **Definition**           | Executes an entire instruction (fetch, decode, execute, memory, write-back) in one long clock cycle. | Divides instruction execution into multiple steps (e.g., fetch, decode, execute), each in a shorter clock cycle, reusing hardware. | Divides instruction execution into stages (e.g., IF, ID, EX, MEM, WB), processing multiple instructions concurrently in overlapping stages. |
| **Execution Process**    | All stages (e.g., IF, ID, EX, MEM, WB) are completed in one cycle using separate hardware for each stage. | Stages are executed sequentially over multiple cycles, with shared hardware (e.g., one ALU for execute and address calculation). | Each stage takes one cycle; multiple instructions progress through stages simultaneously (e.g., IF for Instr1, ID for Instr2). |
| **Clock Cycle Time**     | Long (must accommodate the slowest stage, e.g., memory access). Typically 1–2 ns for simple CPUs. | Short (based on the slowest individual step, e.g., ALU operation). Typically 0.2–0.5 ns per step. | Short (similar to multiple cycle, as each stage is balanced). Typically 0.2–0.5 ns per stage. |
| **Instruction Throughput** | Low (one instruction per long cycle, e.g., 0.5–1 MIPS). | Moderate (one instruction every 3–5 cycles, e.g., 2–5 MIPS). | High (one instruction per cycle after initial latency, e.g., 5–10 MIPS). |
| **Hardware Complexity**  | High (dedicated hardware for each stage, e.g., separate adders for PC increment and ALU). | Moderate (shared hardware, e.g., one ALU, but more complex control unit). | High (multiple stage registers, hazard detection logic, forwarding paths). |
| **Control Unit**         | Simple (fixed control signals for all stages in one cycle). Hardwired or microprogrammed. | Complex (state machine to sequence steps, e.g., fetch, decode). Microprogrammed or hardwired. | Complex (manages stage transitions, hazard resolution). Hardwired or microprogrammed. |
| **Performance Example**  | `ADD R1, R2, R3`: Takes 1 cycle (e.g., 2 ns), no overlap. 10 instructions = 20 ns. | `ADD R1, R2, R3`: Takes 4–5 cycles (e.g., 0.4 ns × 5 = 2 ns). 10 instructions ≈ 18–20 ns. | `ADD R1, R2, R3`: 5-stage pipeline, 1 cycle per instruction after 5-cycle latency. 10 instructions ≈ 14 ns (5 + 9 × 0.4 ns). |
| **Advantages**           | - Simple design and control.<br>- Predictable execution time.<br>- No hazards. | - Shorter cycle time.<br>- Efficient hardware reuse.<br>- Flexible for complex instructions. | - High throughput (overlaps instructions).<br>- Efficient for multiple instructions.<br>- Scalable with more stages. |
| **Disadvantages**        | - Long cycle time (slow for complex instructions).<br>- Wastes resources for simple instructions.<br>- Low throughput. | - Lower throughput than pipeline.<br>- Complex control unit.<br>- Variable instruction latency. | - Complex design (hazard detection, forwarding).<br>- Control hazards (branches).<br>- Initial latency for single instruction. |
| **Use Case**             | Simple CPUs, educational designs (e.g., basic RISC processors). | Embedded systems, CISC processors (e.g., older x86 designs). | Modern CPUs (e.g., ARM, x86), high-performance systems requiring high throughput. |
| **Hazards**              | None (single cycle, no overlap). | None (sequential execution, no overlap). | Structural (resource conflicts), Data (dependencies), Control (branches). Resolved via forwarding, stalling, prediction (from your hazard question). |

---

### Notes and Examples
- **Single Cycle Example**:  
  - Instruction: `ADD R1, R2, R3`.  
  - Execution: Fetch, decode, execute (ALU), write-back in one 2 ns cycle.  
  - **Scenario**: 5 instructions take 5 × 2 ns = 10 ns.  
  - **Hardware**: Separate memory for IF, ALU for EX, register file for WB.  
  - **Status Register**: Flags (N, Z, C, V) updated in one cycle (links to your status register question).

- **Multiple Cycle Example**:  
  - Instruction: `ADD R1, R2, R3`.  
  - Execution: 5 steps (IF, ID, EX, MEM, WB), each 0.4 ns, total 2 ns.  
  - **Scenario**: 5 instructions take ~10 ns (overlapping fetch of next instruction reduces total time slightly).  
  - **Hardware**: Shared ALU for EX and PC increment, single memory unit.  
  - **Control**: State machine sequences steps (e.g., `PCout, MARin` for IF).

- **Pipeline Example**:  
  - Instruction: `ADD R1, R2, R3`.  
  - Execution: 5-stage pipeline (IF, ID, EX, MEM, WB), each 0.4 ns. First instruction takes 5 × 0.4 = 2 ns; subsequent instructions complete every 0.4 ns.  
  - **Scenario**: 5 instructions take 5 × 0.4 + 4 × 0.4 = 3.6 ns.  
  - **Hardware**: Stage registers, hazard detection (e.g., forwarding for data hazards).  
  - **Conditional Branch**: `BRN Target` causes control hazard, resolved by prediction (links to your hazard and conditional control questions).
