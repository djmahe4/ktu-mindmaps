# FAQ: Foundations of Post-Quantum Cryptography

## Intro
Post-Quantum Cryptography (PQC) is a new generation of cryptographic algorithms designed to remain secure even against future quantum computers that can break today's RSA and ECC systems.

### RSA

1. Choose two large prime numbers.
2. Multiply them together.
3. Create a public key from the result.
4. Create a private key using the original primes.
5. **Shor's Algorithm:** Given the public key, a quantum computer can efficiently recover the original primes and break RSA.

---

### ECC

1. Choose a secret number.
2. Apply elliptic-curve multiplication.
3. Publish the resulting point as the public key.
4. Keep the secret number as the private key.
5. **Shor's Algorithm:** Given the public key, a quantum computer can efficiently recover the secret number and break ECC.

---

### AES

1. Generate a random secret key.
2. Use the key to encrypt data.
3. Share the same key with the receiver.
4. Use the same key to decrypt data.
5. **Grover's Algorithm:** A quantum computer can speed up key guessing, but cannot directly recover the key like Shor's does for RSA/ECC. AES-256 remains considered secure.


## Q1. Why do quantum computers threaten RSA and ECC but not AES to the same extent?

RSA and ECC depend on mathematical problems such as integer factorization and discrete logarithms.

A sufficiently capable quantum computer running Shor's Algorithm can solve these problems efficiently, rendering traditional public-key systems insecure.

AES behaves differently. The primary quantum attack is Grover's Algorithm, which provides only a square-root speedup. As a result:

* AES-128 offers roughly 64 bits of quantum security.
* AES-256 offers roughly 128 bits of quantum security.

This makes increasing symmetric key lengths a practical mitigation strategy.

---

## Q2. Why are lattice-based systems considered quantum-resistant?

Lattice-based cryptography relies on difficult geometric problems in high-dimensional vector spaces.

A prominent example is Learning With Errors (LWE), where small amounts of noise are deliberately introduced into mathematical structures.

Currently, no known quantum algorithm provides the dramatic advantage against lattice problems that Shor's Algorithm provides against factorization and discrete logarithms.

For this reason, ML-KEM (formerly Kyber) became a leading standard for post-quantum key establishment.

---

## Q3. What is a hybrid key exchange?

A hybrid key exchange combines a classical algorithm with a post-quantum algorithm.

Example:

Layer 1: X25519 (Classical Elliptic Curve)
Layer 2: ML-KEM (Post-Quantum Lattice)

The connection remains secure if either layer remains secure.

Benefits:

* Protection against future quantum attacks.
* Protection if a newly standardized PQC algorithm later reveals weaknesses.
* Reduced migration risk during the transition period.

---

## Q4. What deployment challenges emerged during large-scale PQC testing?

The most significant issue is size.

| Algorithm  | Public Key  | Ciphertext  | Characteristics          |
| ---------- | ----------- | ----------- | ------------------------ |
| X25519     | ~32 bytes   | ~32 bytes   | Minimal overhead         |
| ML-KEM-768 | ~1184 bytes | ~1088 bytes | Larger network footprint |

Consequences include:

* Increased bandwidth consumption.
* MTU fragmentation.
* Compatibility issues with older middleboxes and firewalls.
* Potential connection failures in legacy environments.

---

# Advanced FAQ: QS-BTrust and Edge Deployments

## Q5. What is QS-BTrust?

QS-BTrust is a quantum-safe, zero-trust architecture designed for intelligent transportation systems and vehicular networks.

Its objectives are:

1. Prevent quantum-enabled message forgery.
2. Protect driver privacy.
3. Maintain trust in real-time safety communications.

Examples include:

* Emergency braking notifications.
* Hazard alerts.
* Cooperative traffic coordination.

---

## Q6. Why does Google use ML-KEM while QS-BTrust uses Dilithium?

The answer lies in the cryptographic objective.

### Google Infrastructure

Goal:
Securely establish confidential communication channels.

Preferred primitive:
ML-KEM (Key Encapsulation Mechanism)

Function:
Encryption and key establishment.

### QS-BTrust

Goal:
Verify authenticity of public safety broadcasts.

Preferred primitive:
CRYSTALS-Dilithium

Function:
Digital signatures and message authentication.

Vehicles want messages to be visible to everyone nearby but verifiably authentic.

---

## Q7. How do PUFs strengthen PQC in QS-BTrust?

QS-BTrust integrates software-based cryptography with hardware-based trust.

Physical Unclonable Functions (PUFs) exploit microscopic manufacturing variations in semiconductor devices.

Process:

Silicon Variations
↓
Physical Unclonable Function
↓
Unique Hardware Fingerprint
↓
Dynamic Vehicle Identity
↓
Dilithium Signature
↓
Trusted Broadcast

Benefits:

* Resistant to key cloning.
* Resistant to hardware impersonation.
* Maintains trust even if software is copied.

---

## Q8. How does QS-BTrust balance privacy and accountability?

QS-BTrust implements conditional privacy.

For normal users:

* Vehicles use rotating pseudonymous identities.
* Broadcasts become difficult to correlate.
* Long-term tracking becomes impractical.

For authorized authorities:

* A trusted authority can resolve identities when necessary.
* Malicious actors can be identified and revoked.

Revocation is handled through lightweight state-management mechanisms rather than large certificate revocation lists, reducing latency and bandwidth requirements.

---

# Comparative Architecture Matrix

| Dimension           | Google-Scale Infrastructure | QS-BTrust Vehicular Infrastructure |
| ------------------- | --------------------------- | ---------------------------------- |
| Primary Goal        | Confidentiality             | Authentication & Trust             |
| PQC Primitive       | ML-KEM                      | CRYSTALS-Dilithium                 |
| Classical Companion | X25519                      | SHA-256-based mechanisms           |
| Main Threat         | Harvest-now-decrypt-later   | Message forgery & impersonation    |
| Key Constraint      | Packet fragmentation        | Verification latency               |
| Trust Root          | Certificate Authorities     | Physical Unclonable Functions      |
| Identity Model      | Long-term sessions          | Dynamic pseudonyms                 |
| Environment         | Cloud & Web                 | Edge & Transportation              |

---

# Key Presentation Takeaway

Post-Quantum Cryptography is not a single technology but a family of solutions tailored to different operational environments.

Google demonstrates how PQC protects global communications through hybrid key exchanges and internet-scale deployment strategies.

QS-BTrust demonstrates how PQC extends beyond the cloud into physical cyber-physical systems, combining lattice-based signatures with hardware fingerprints to secure future transportation networks.

Together, they illustrate a complete quantum-resilient ecosystem—from data centers and browsers to vehicles and roadside infrastructure.
