### Assumptions and Setup
- **Instruction**: `ADD (R3), R1` (Add the value at memory address stored in R3 to R1, store result in R1).
- **Registers**:
  - PC (Program Counter): Holds the address of the next instruction.
  - IR (Instruction Register): Holds the fetched instruction.
  - MAR (Memory Address Register): Holds the memory address for read/write.
  - MDR (Memory Data Register): Holds data read from or written to memory.
  - R1, R3: General-purpose registers.
  - Y, Z: Temporary registers for ALU operations (Y for one input, Z for output).
- **Micro-Operations** (based on your format):
  - `PCout`: Output PC value to bus.
  - `MARin`: Load value from bus into MAR.
  - `Read`: Initiate memory read operation.
  - `Select4`: Select a constant (e.g., 4 or 1) for ALU input (used for PC increment).
  - `Add`: Perform ALU addition.
  - `Zin`: Store ALU output in Z.
  - `Zout`: Output Z to bus.
  - `PCin`: Load value from bus into PC.
  - `Yin`: Load value from bus into Y.
  - `WMFC`: Wait for Memory Function Complete (memory read/write completion).
  - `MDRout`: Output MDR to bus.
  - `IRin`: Load value from bus into IR.
  - `R3out`: Output R3 to bus.
  - `R1out`: Output R1 to bus.
  - `Select Y`: Select Y as one ALU input.
  - `R1in`: Load value from bus into R1.
  - `End`: Signal instruction completion.
- **Single Bus**: One bus for all transfers, so micro-operations in each step are limited by bus availability (sequential).
- **Three-Bus**: Three buses (Bus 1: ALU input A, Bus 2: ALU input B, Bus 3: ALU output), allowing more simultaneous micro-operations per step.

---

### Single Bus Architecture: Control Sequence for `ADD (R3), R1`

In a **single bus architecture**, only one data transfer can occur per step due to the single bus. Each step corresponds to a microprogrammed control word, with micro-operations executed sequentially.

#### Control Sequence
1. **PCout, MARin, Read, Select4, Add, Zin**  
   - Output PC to bus, load into MAR to fetch instruction. Initiate memory read. Select constant 4 (for PC increment), add to PC, store result in Z.  
   - *Purpose*: Start fetching instruction and increment PC.
2. **Zout, PCin, Yin, WMFC**  
   - Output Z (incremented PC) to bus, load into PC. Load memory data (instruction) into Y (temporary). Wait for memory read to complete.  
   - *Purpose*: Update PC and wait for instruction fetch.
3. **MDRout, IRin**  
   - Output fetched instruction from MDR to bus, load into IR.  
   - *Purpose*: Store instruction in IR for decoding.
4. **R3out, MARin, Read**  
   - Output R3 (memory address) to bus, load into MAR. Initiate memory read for data at [R3].  
   - *Purpose*: Start fetching memory operand.
5. **MDRout, Yin, WMFC**  
   - Output memory data from MDR to bus, load into Y. Wait for memory read to complete.  
   - *Purpose*: Store memory data in Y for ALU.
6. **R1out, Select Y, Add, Zin**  
   - Output R1 to bus (ALU input A). Select Y (memory data) as ALU input B. Perform addition, store result in Z.  
   - *Purpose*: Add R1 and memory data.
7. **Zout, R1in, End**  
   - Output Z (result) to bus, load into R1. Signal instruction completion.  
   - *Purpose*: Store result in R1 and end.

#### Total Steps: 7
- **Fetch**: Steps 1–3.
- **Execute**: Steps 4–7.
- **Note**: The sequence is longer because the single bus limits simultaneous operations (e.g., R1 and memory data can’t be sent to ALU together).

**Diagram**:
```
[PC] [IR] [MAR] [MDR] [R1] [R3] [Y] [Z] [ALU] [Memory]
    \_________________Single Bus_________________/
```
- Sequential transfers: PC → MAR, MDR → IR, R3 → MAR, etc.

---

### Three-Bus Architecture: Control Sequence for `ADD (R3), R1`

In a **three-bus architecture**, multiple transfers can occur simultaneously using Bus 1 (ALU input A), Bus 2 (ALU input B), and Bus 3 (ALU output). This reduces the number of steps by combining micro-operations.

#### Control Sequence
1. **PCout, MARin, Read, Select4, Add, Zin**  
   - Bus 1: Output PC to MAR for instruction fetch.  
   - Bus 2: Select constant 4 for PC increment.  
   - Bus 3: Add PC + 4, store in Z.  
   - Initiate memory read.  
   - *Purpose*: Fetch instruction and increment PC simultaneously.
2. **Zout, PCin, MDRout, IRin, WMFC**  
   - Bus 1: Output Z to PC (update PC).  
   - Bus 3: Output MDR (instruction) to IR.  
   - Wait for memory read to complete.  
   - *Purpose*: Store instruction in IR and update PC.
3. **R3out, MARin, Read, WMFC**  
   - Bus 1: Output R3 to MAR for memory data fetch.  
   - Initiate memory read and wait for completion.  
   - *Purpose*: Fetch data at [R3].
4. **R1out, MDRout, Select Y, Add, Zin, R1in, End**  
   - Bus 1: Output R1 to ALU input A.  
   - Bus 2: Output MDR (memory data) to Y, select Y as ALU input B.  
   - Bus 3: Add, store result in Z, then transfer Z to R1.  
   - Signal instruction completion.  
   - *Purpose*: Add R1 and memory data, store result in R1, and end.

#### Total Steps: 4
- **Fetch**: Steps 1–2.
- **Execute**: Steps 3–4.
- **Note**: Fewer steps due to parallel transfers (e.g., R1 and MDR to ALU inputs in one step).

**Diagram**:
```
[PC] [IR] [MAR] [MDR] [R1] [R3] [Y] [Z] [Memory]
   |      |      |      |      |      |      |
[Bus 1] [Bus 2] ----> [ALU] ----> [Bus 3]
```
- Parallel transfers: R1 → ALU A, MDR → ALU B, Z → R1.

---

### Similar Instructions in the Same Format

Using the same micro-operation format, let’s provide control sequences for the similar instructions you mentioned: `LOAD R1, (R2)`, `STORE R1, (R2)`, and `SUB R1, R2, R3`.

#### 1. `LOAD R1, (R2)` (Single Bus)
- **Operation**: `R1 ← Memory[R2]` (Load R1 with value at memory address in R2).
1. **PCout, MARin, Read, Select4, Add, Zin**  
   - Fetch instruction, increment PC.
2. **Zout, PCin, Yin, WMFC**  
   - Update PC, wait for instruction fetch.
3. **MDRout, IRin**  
   - Load instruction into IR.
4. **R2out, MARin, Read**  
   - Load R2 (address) into MAR, initiate memory read.
5. **MDRout, R1in, WMFC, End**  
   - Load memory data from MDR to R1, wait, end.
- **Total Steps**: 5.

#### `LOAD R1, (R2)` (Three-Bus)
1. **PCout, MARin, Read, Select4, Add, Zin**  
   - Fetch instruction, increment PC.
2. **Zout, PCin, MDRout, IRin, WMFC**  
   - Update PC, load instruction to IR.
3. **R2out, MARin, Read, WMFC**  
   - Load R2 to MAR, fetch memory data.
4. **MDRout, R1in, End**  
   - Load memory data to R1, end.
- **Total Steps**: 4.

---

#### 2. `STORE R1, (R2)` (Single Bus)
- **Operation**: `Memory[R2] ← R1` (Store R1’s value into memory address in R2).
1. **PCout, MARin, Read, Select4, Add, Zin**  
   - Fetch instruction, increment PC.
2. **Zout, PCin, Yin, WMFC**  
   - Update PC, wait for fetch.
3. **MDRout, IRin**  
   - Load instruction into IR.
4. **R2out, MARin**  
   - Load R2 (address) into MAR.
5. **R1out, MDRin**  
   - Load R1’s value into MDR.
6. **MDRout, Write, WMFC, End**  
   - Write MDR to memory, wait, end.
- **Total Steps**: 6.

#### `STORE R1, (R2)` (Three-Bus)
1. **PCout, MARin, Read, Select4, Add, Zin**  
   - Fetch instruction, increment PC.
2. **Zout, PCin, MDRout, IRin, WMFC**  
   - Update PC, load instruction to IR.
3. **R2out, MARin, R1out, MDRin**  
   - Load R2 to MAR, R1 to MDR.
4. **MDRout, Write, WMFC, End**  
   - Write MDR to memory, end.
- **Total Steps**: 4.

---

#### 3. `SUB R1, R2, R3` (Single Bus)
- **Operation**: `R1 ← R2 - R3` (Subtract R3 from R2, store in R1).
1. **PCout, MARin, Read, Select4, Add, Zin**  
   - Fetch instruction, increment PC.
2. **Zout, PCin, Yin, WMFC**  
   - Update PC, wait for fetch.
3. **MDRout, IRin**  
   - Load instruction into IR.
4. **R2out, Yin**  
   - Load R2 into Y (ALU input).
5. **R3out, Select Y, Sub, Zin**  
   - Load R3 to ALU, select Y, subtract, store in Z.
6. **Zout, R1in, End**  
   - Load Z to R1, end.
- **Total Steps**: 6.

#### `SUB R1, R2, R3` (Three-Bus)
1. **PCout, MARin, Read, Select4, Add, Zin**  
   - Fetch instruction, increment PC.
2. **Zout, PCin, MDRout, IRin, WMFC**  
   - Update PC, load instruction to IR.
3. **R2out, R3out, Select Y, Sub, Zin, R1in, End**  
   - Bus 1: R2 to ALU A. Bus 2: R3 to Y, select Y for ALU B. Bus 3: Subtract, store in Z, then to R1. End.
- **Total Steps**: 3.

---

### Comparison Table
| **Instruction**       | **Single Bus Steps** | **Three-Bus Steps** |
|-----------------------|----------------------|---------------------|
| `ADD (R3), R1`        | 7                    | 4                   |
| `LOAD R1, (R2)`       | 5                    | 4                   |
| `STORE R1, (R2)`      | 6                    | 4                   |
| `SUB R1, R2, R3`      | 6                    | 3                   |

- **Single Bus**: More steps due to sequential transfers (one bus bottleneck).
- **Three-Bus**: Fewer steps due to parallel transfers (multiple buses).
