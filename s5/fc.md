# FC
[Mod1](#module-1)<br><br>
[Mod2](#module-2)<br><br>
[Mod3](#module-3)<br><br>
[Mod4](#module-4)<br><br>
[Mod5](#module-5)<br><br>
## Module 1
### Fermat’s Little Theorem & Euler’s Theorem – Complete Mastery Notes  
(With Mindmap, Mnemonics, Proofs & 15 Solved Problems)

#### 1. Prerequisites Recap (You Already Know This!)
- gcd(a, n) = 1 ⇒ a & n are **coprime** (relatively prime)  
- φ(n) = number of integers from 1 to n that are coprime to n  
- φ(p) = p−1 when p is prime  
- φ is multiplicative: if gcd(m,n)=1 then φ(mn) = φ(m)φ(n)

#### 2. FERMAT’S LITTLE THEOREM (FLT) – The “Prime” Version
**Statement**  
If **p is prime** and **p does not divide a** (i.e. gcd(a,p)=1), then  
**a^{p−1} ≡ 1 (mod p)**  
or equivalently  
**a^p ≡ a (mod p)** (this version works even if p divides a!)

**Mnemonic** → “**F**ermat says: for **P**rime modulus, a^{**P−1**} = **1** mod P”  
Think: “The (p−1) powers come back home to 1.”

**Quick Proof Idea (using group of units)**  
The numbers 1,2,…,p−1 are all coprime to p → there are φ(p) = p−1 of them.  
Multiplying each by a just permutes the list → product is same → a^{p−1} × (1·2·…·(p−1)) ≡ 1·2·…·(p−1) (mod p)  
⇒ a^{p−1} ≡ 1 (mod p)

#### 3. EULER’S THEOREM – The General Version
**Statement**  
If gcd(a, n) = 1, then  
**a^{φ(n)} ≡ 1 (mod n)**

**Mnemonic** → “**E**uler says: exponent = **φ(n)** brings you back to **1** when coprime.”

**Why it generalises FLT?**  
When n = p (prime), φ(p) = p−1 → Euler becomes Fermat!

#### Mindmap (Draw this on one page!)

```
              Fermat vs Euler
                       │
       ┌───────────────┴───────────────┐
       ▼                               ▼
If n = PRIME p                   If any n (gcd(a,n)=1)
   a^{p-1} ≡ 1 (mod p)    ─────►   a^{φ(n)} ≡ 1 (mod n)
   a^p ≡ a (mod p)                φ(p) = p-1 → same as FLT
       ▲                               ▲
       └───────────Special case───────┘
```

#### 4. 15 Solved Problems (Increasing Difficulty)

**Level 1 – Direct Application**
1. Compute 3¹⁰ mod 7  
   φ(7)=6, 10 ÷ 6 = 1 remainder 4 → 3¹⁰ = 3^{6+4} = (3⁶)¹·3⁴ ≡ 1¹·3⁴ ≡ 81 ≡ 4 mod 7  
   Ans: 4

2. Compute 2³⁰ mod 31 (31 is prime)  
   FLT: 2³⁰ ≡ 1 mod 31 (because 2^{30} = 2^{31−1})  
   Ans: 1

**Level 2 – Reduce exponent**
3. 5¹⁰⁰ mod 11  
   φ(11)=10 → 5¹⁰⁰ = (5¹⁰)¹⁰ ≡ 1¹⁰ ≡ 1 mod 11  
   Ans: 1

4. 7²⁰²⁵ mod 12  
   gcd(7,12)=1, φ(12)=φ(4·3)=12·(1−1/2)·(1−1/3)=4  
   7⁴ ≡ 1 mod 12 → 2025 ÷ 4 = 506 remainder 1 → 7²⁰²⁵ = (7⁴)⁵⁰⁶ ·7¹ ≡ 1·7 ≡ 7 mod 12  
   Ans: 7

**Level 3 – Last digits / Power cycles**
5. Last two digits of 3¹⁰⁰ (i.e. 3¹⁰⁰ mod 100)  
   φ(100)=40, gcd(3,100)=1 → 3⁴⁰ ≡ 1 mod 100  
   100 = 40·2 + 20 → 3¹⁰⁰ = (3⁴⁰)² · 3²⁰ ≡ 1² · 3²⁰ mod 100  
   3⁵=243≡43, 3¹⁰=(3⁵)²≡49, 3²⁰=(3¹⁰)²≡01 mod 100  
   So 01 → last two digits 01  
   Ans: 01

6. Find 2¹²³⁴⁵⁶ mod 13  
   13 prime → 2¹² ≡ 1 mod 13  
   123456 ÷ 12 = 10288 exactly → 2¹²³⁴⁵⁶ = (2¹²)¹⁰²⁸⁸ ≡ 1¹⁰²⁸⁸ ≡ 1 mod 13  
   Ans: 1

**Level 4 – Inverse using FLT/Euler**
7. Find multiplicative inverse of 3 mod 11  
   By FLT: 3¹⁰ ≡ 1 mod 11 → inverse is 3⁹  
   3³=27≡5, 3⁶=(3³)²≡3, 3⁹=3⁶·3³≡3·5=15≡4 mod 11  
   Check: 3·4=12≡1 yes!  
   Ans: 4

8. Solve 7x ≡ 4 (mod 17)  
   Inverse of 7 mod 17: 7^{15} ≡ 1 → need 7^{15}·4 = x  
   Or use extended Euclid, but fast way: 7·5=35≡1 mod 17 → inv=5  
   x ≡ 4·5 ≡ 20 ≡ 3 mod 17  
   Ans: x ≡ 3

**Level 5 – Hard ones**
9. Compute 2025¹⁰⁰⁰ mod 17  
   2025 ÷ 17: 17·119=2023 → 2025≡2 mod 17  
   So 2¹⁰⁰⁰ mod 17  
   φ(17)=16, 1000 ÷ 16 = 62·16 + 8 → 2¹⁰⁰⁰ ≡ 2⁸ ≡ 256 ≡ 1 mod 17  
   Ans: 1

10. Order of 2 modulo 31 (smallest k such that 2ᵏ≡1 mod 31)  
    31−1=30, divisors: 1,2,3,5,6,10,15,30  
    Check 2¹⁵=32768≡−1 ≢1, so order is 30 (primitive root)  
    Ans: 30

11. 11¹¹ mod 12  
    φ(12)=4, 11≡−1, (−1)¹¹=−1≡11 mod 12  
    Ans: 11

12. Without calculator: 7⁵⁰⁰ mod 561 (561=3·11·17, Carmichael number!)  
    Note: 561 is pseudoprime to many bases, but Euler still works because gcd(7,561)=1  
    λ(561)=lcm(2,10,16)=80 → actually use Carmichael function λ(n)  
    7⁸⁰ ≡1 mod 561 → 500=6·80 + 20 → 7⁵⁰⁰=(7⁸⁰)⁶ ·7²⁰ ≡7²⁰ mod 561  
    (Still tedious, but concept is important)

13–15. Quick-fire
13. 5⁹⁹ mod 7 → 5¹ ≡5, 99 odd → 5⁹⁹ ≡5 mod 7  
14. 2¹⁰⁰ mod 101 (101 prime) → 2¹⁰⁰ ≡ 2^{100} ≡1 mod 101 by FLT  
15. Inverse of 13 mod 100 → φ(100)=40 → 13⁴⁰≡1 → need 13³⁹  
    Or extended Euclid → 13·77=1001=10·100+1 → inv=77 mod 100  
    Ans: 77

#### One-Page Cheat Sheet to Memorise Forever

| Theorem          | Condition                  | Result                     | Mnemonic                     |
|------------------|----------------------------|----------------------------|------------------------------|
| Fermat’s Little  | p prime, p∤a               | a^{p−1} ≡1 (mod p)         | “Prime → p−1 power =1”       |
| Fermat (alt)     | p prime (any a)            | a^p ≡ a (mod p)            | “a^p looks like a”           |
| Euler’s          | gcd(a,n)=1                 | a^{φ(n)} ≡1 (mod n)        | “Coprime → φ(n) power =1”    |

## Module 2
### 1. OSI Security Architecture – The 3 Pillars (Mnemonic: ASM)
- **A**ttacks → What the enemy does
- **S**ervices → What protection we want
- **M**echanisms → How we actually protect

### 2. Security Attacks – 2 Types (Mnemonic: PA vs AA)
| Type          | Passive Attack (Silent Thief)                         | Active Attack (Aggressive Hacker)                     |
|---------------|-------------------------------------------------------|-------------------------------------------------------|
| Goal          | Steal info without being noticed                      | Change/disrupt the system                             |
| Effect        | No change in data or system                           | Data changed or service stopped                       |
| Detection     | Very hard                                             | Easier to detect                                      |
| Examples      | 1. Release of message content (eavesdrop call/email)<br>2. Traffic analysis (guess from pattern) | 1. Masquerade (pretend to be someone)<br>2. Replay (resend old message)<br>3. Modification (alter message)<br>4. Denial of Service (DoS) |

**Mnemonic for 4 Active Attacks: MR. MD**  
M – Masquerade  
R – Replay  
M – Modification  
D – Denial of Service

### 3. Security Services – 5 Types (X.800) – Mnemonic: AACID-N
1. **A**uthentication → Are you really you?
2. **A**ccess Control → Allowed or not?
3. **C**onfidentiality → No one else reads
4. **I**ntegrity → Message not changed
5. **N**on-Repudiation → Cannot deny sending/receiving  
   → **AACIN** (pronounced “Aacin” – like “Acid with N”)

### 4. Security Mechanisms – 2 Categories
- **Specific** (layer-specific): Encipherment, Digital Signature, Access Control, Data Integrity, Authentication Exchange, Traffic Padding, Routing Control, Notarization
- **Pervasive** (general): Trusted Functionality, Security Label, Event Detection, Audit Trail, Recovery

### 5. Cryptography Basic Terms – Mnemonic: P-C-E-D
- **P**laintext → Original message
- **C**iphertext → Scrambled message
- **E**ncryption → Plain → Cipher
- **D**ecryption → Cipher → Plain

Cryptography = Science of hiding (legal)  
Cryptanalysis = Science of breaking (attacker)  
Cryptology = Both together

### 6. Symmetric Cipher Model – 5 Ingredients (Mnemonic: PESCD)
1. **P**laintext
2. **E**ncryption Algorithm
3. **S**ecret Key (same for encrypt & decrypt)
4. **C**iphertext
5. **D**ecryption Algorithm

**Only 2 requirements for security:**
1. Strong algorithm
2. Key kept secret & shared securely

### 7. Cryptographic Systems – 3 Dimensions
| Dimension                  | Options                                      |
|----------------------------|----------------------------------------------|
| 1. Operation               | Substitution / Transposition                 |
| 2. Number of keys          | Symmetric (same key) / Asymmetric (two keys)|
| 3. Processing of plaintext | Block cipher / Stream cipher                 |

### 8. Cryptanalytic Attacks – Difficulty Order (Easiest → Hardest)
1. Ciphertext only
2. Known plaintext
3. Chosen plaintext (strongest for attacker)
4. Chosen ciphertext
5. Chosen text (both chosen plain + cipher)

### 9. Classical Encryption Techniques – 2 Big Families
#### A. Substitution Ciphers (Replace letters)
| Type              | Monoalphabetic                          | Polyalphabetic                             |
|-------------------|-----------------------------------------|--------------------------------------------|
| Meaning           | One letter → always same substitute     | One letter → many possible substitutes     |
| Examples          | Caesar, Playfair, Hill, Affine          | Vigenère                                   |
| Weakness          | Frequency analysis works                | Hides frequency → stronger                 |

**Caesar Cipher (Shift by 3)**
- Formula: C = (P + k) mod 26   → k = 3 usually
- Decryption: P = (C − k) mod 26
- Only 26 possible keys → brute-force in seconds
- Mnemonic: “Julius Caesar shifted 3”

**Playfair Cipher (5×5 matrix, digraphs)**
- Keyword → fill matrix → I/J together
- Rectangle rule for digraphs: selected letter row and other letter column
- Rules (Mnemonic: RRCD)
  1. Repeat letter → insert X
  2. Same Row → right (wrap)
  3. Same Column → down (wrap)
  4. Different → rectangle rule

**Vigenère Cipher (Polyalphabetic king)**
- Use repeating keyword
- Cᵢ = (Pᵢ + Kᵢ) mod 26
- Dᵢ = (Cᵢ − Kᵢ) mod 26
- Stronger than monoalphabetic because same letter can become different

**Hill Cipher (Matrix multiplication)**
- Uses m×m key matrix
- C = K × P (mod 26)
- Decryption uses K⁻¹
- Hides single-letter frequency completely
**Affine Cipher (Mathematical substitution)**
- C = (aX + b) mod 26
- D = a⁻¹(C − b) mod 26

#### B. Transposition Ciphers (Rearrange letters)
- No substitution, just permutation
- Types:
  - Keyless (Rail Fence)
    - Rail Fence (zig-zag)
        - Write message in zig-zag pattern across rows
        - example: "HELLO WORLD" with 3 rails<br>
          H   L   O  O  L<br>
           E L W R D<br>
        - Read row-wise: "HLOOL ELWRD"
    - Columnar (fixed columns)
      - Write message in rows of fixed length, read columns
      - example: "HELLO WORLD" with 3 rails<br>
          H   O   R<br>
          E   L   W<br>
          L   D   L<br>
          O<br>
        - Read row-wise: "HOR ELWLD LO"
  - Keyed (columnar)
    - Use keyword to determine column order (write indexes and then follow the key order)
    - example: Keyword "ZEBRA" (order 5,2,3,4,1)<br>
          Z E B R A<br>
          H E L L O<br>
          W O R L D<br>
        - Read columns in keyword order: "OHLWELRLD"
  - Double transposition (very strong classical)
    - example: First transpose with keyword1, then with keyword2
        - Keyword1: "CIPHER"<br>
          C I P H E R<br>
          H E L L O W<br>
          O R L D X X<br>
        - Then transpose again with Keyword2: "KEYWORD"<br>
          K E Y W O R D<br>
          H L L O W H E<br>
          O R L D X X<br>
        - Final ciphertext after both transpositions is: "HLLOWHEORL DXX"

### Full Mind-Map Summary (Visualise this)

```
                OSI Security Architecture
                          ↓
            ┌─────────────┴─────────────┐
         Attacks       Services      Mechanisms
            ↓              ↓              ↓
      Passive | Active   AACIN       Specific | Pervasive
                  ↓
               MR. MD (4 active)

                ↓↓↓
           Cryptography Basics
                ↓↓↓
        Symmetric Model (PESCD)
                ↓↓↓
     Classical Ciphers
          ┌────────┴────────┐
     Substitution       Transposition
          ↓                    ↓
  Caesar → Monoalphabetic → Polyalphabetic (Vigenère)
  Playfair → Hill → Affine
```

### Quick Revision Table (One-page cheat sheet)

| Concept                | Mnemonic / Key Phrase             | Strength / Weakness                     |
|-------------------------|-----------------------------------|-----------------------------------------|
| Passive Attack          | Silent thief                      | Hard to detect                          |
| Active Attack           | MR. MD                            | Easy to detect                          |
| Security Services       | AACIN                             | Remember 5 services                     |
| Symmetric Cipher        | PESCD (5 parts)                   | Same key, fast                          |
| Caesar                  | Shift by 3                        | 26 keys → very weak                     |
| Monoalphabetic          | Fixed mapping                     | Frequency attack                        |
| Polyalphabetic          | Vigenère                          | Hides frequency                         |
| Playfair                | 5×5, digraphs, RRCD rules         | Better than Caesar                      |
| Hill                    | Matrix cipher                     | Strong against ciphertext-only         |
| Transposition           | Rearrange positions               | Keyed/Double = strong classical        |
