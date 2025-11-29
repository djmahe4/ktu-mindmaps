An SR Flip-Flop is a basic digital memory circuit that stores a single bit of information. It's a fundamental component in digital electronics.

*SR Flip-Flop Truth Table:*

| S | R | Q(t) | Q(t+1) |
| --- | --- | --- | --- |
| 0 | 0 | Q(t) | Q(t)  |
| 0 | 1 | 0    | 0    |
| 1 | 0 | 1    | 1    |
| 1 | 1 | Invalid | Invalid |

*Working:*

1. *Set (S=1, R=0)*: Q(t+1) = 1, regardless of Q(t).
2. *Reset (S=0, R=1)*: Q(t+1) = 0, regardless of Q(t).
3. *Hold (S=0, R=0)*: Q(t+1) = Q(t), maintains previous state.
4. *Invalid (S=1, R=1)*: Q(t+1) is undefined.

*Logic Circuit:*

```
          +---------------+
          |               |
          |  S   R   Q   |
          +---------------+
                  |
                  |
                  v
+---------------+       +---------------+
|               |       |               |
|  NOR Gate    |       |  NOR Gate    |
|  (Q)         |       |  (Q')        |
+---------------+       +---------------+
          |               |
          |  Q'          |
          +---------------+
                  |
                  |
                  v
+---------------+       +---------------+
|               |       |               |
|  S           |       |  R           |
|  (Input)     |       |  (Input)     |
+---------------+       +---------------+
```

*How it works:*

1. When S=1 and R=0, the first NOR gate outputs 0, and the second NOR gate outputs 1.
2. When S=0 and R=1, the first NOR gate outputs 1, and the second NOR gate outputs 0.
3. When S=0 and R=0, the outputs remain the same as the previous state.

*Applications:*

1. Memory cells
2. Counters
3. Registers
4. Digital clocks
5. Sequential logic circuits

*Advantages:*

1. Simple implementation
2. Low power consumption
3. Fast switching times

*Disadvantages:*

1. Limited storage capacity
2. Sensitive to noise and glitches

*Variations:*

1. D Flip-Flop (Data Flip-Flop)
2. T Flip-Flop (Toggle Flip-Flop)
3. JK Flip-Flop

The SR Flip-Flop is a fundamental component in digital electronics, and its understanding is crucial for designing and analyzing digital circuits.
