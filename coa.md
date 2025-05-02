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
