A binary adder-subtractor is a digital circuit that performs both addition and subtraction operations on binary numbers.

*Binary Adder:*

A binary adder is a digital circuit that adds two binary numbers.

*Binary Subtractor:*

A binary subtractor is a digital circuit that subtracts one binary number from another.

*Binary Adder-Subtractor:*

A binary adder-subtractor is a combination of both adder and subtractor circuits.

*Working Principle:*

1. Addition: A and B are added using a binary adder.
2. Subtraction: B is inverted (using inverters) and added to A using the same binary adder.
3. End-around carry: To perform subtraction, the carry input (Cin) is set to 1.

*Circuit Diagram:*

```
          +---------------+
          |               |
          |  A (n bits)  |
          +---------------+
                  |
                  |
                  v
+---------------+       +---------------+
|               |       |               |
|  Inverter    |       |  Binary Adder  |
|  (for B)     |       |               |
+---------------+       +---------------+
          |               |
          |  B (n bits)  |
          +---------------+
                  |
                  |
                  v
+---------------+       +---------------+
|               |       |               |
|  Cin (1 bit)  |       |  Sum (n bits) |
|               |       |  Cout (1 bit) |
+---------------+       +---------------+
```

*Truth Table:*

| A   | B   | Cin | Mode | Sum  | Cout |
| :-- | :-- | :-- | :--- | :--- | :--- |
| 0   | 0   | 0   | Add  | 0    | 0    |
| 0   | 0   | 1   | Sub  | 1    | 0    |
| 0   | 1   | 0   | Add  | 1    | 0    |
| 0   | 1   | 1   | Sub  | 0    | 1    |
| 1   | 0   | 0   | Add  | 1    | 0    |
| 1   | 0   | 1   | Sub  | 0    | 1    |
| 1   | 1   | 0   | Add  | 0    | 1    |
| 1   | 1   | 1   | Sub  | 1    | 1    |

*VHDL Code:*

```
vhdl
entity binary_adder_subtractor is
    Port ( A : in  STD_LOGIC_VECTOR (n-1 downto 0);
           B : in  STD_LOGIC_VECTOR (n-1 downto 0);
           Cin : in  STD_LOGIC;
           Mode : in  STD_LOGIC;  -- 0 for addition, 1 for subtraction
           Sum : out  STD_LOGIC_VECTOR (n-1 downto 0);
           Cout : out  STD_LOGIC);
end binary_adder_subtractor;

architecture Behavioral of binary_adder_subtractor is
begin
    process(A, B, Cin, Mode)
        variable temp_B : STD_LOGIC_VECTOR (n-1 downto 0);
    begin
        if Mode = '1' then  -- subtraction
            temp_B := not B;
            Cin <= '1';
        else  -- addition
            temp_B := B;
            Cin <= '0';
        end if;
        
        Sum <= A + temp_B + Cin;
        Cout <= (A and temp_B) or (A and Cin) or (temp_B and Cin);
    end process;
end Behavioral;
```

*Applications:*

1. Arithmetic Logic Units (ALUs)
2. Digital computers
3. Microprocessors
4. Cryptographic hardware

*Advantages:*

1. Performs both addition and subtraction
2. Reduced hardware requirements
3. Improved performance

*Disadvantages:*

1. Increased complexity
2. Higher power consumption
