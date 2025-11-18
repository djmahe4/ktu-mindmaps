**SNS**<br>
[Mod1](#module-1)<br><br>
[Mod2](#module-2)<br><br>
[Mod3](#module-3)<br><br>
[Mod4](#module-4)<br><br>
[Mod5](#module-5)<br><br>

# Module 2
[Notes](https://drive.google.com/file/d/1GNo3bUxvDeV99IoI3Dp7w7vGRCX75fVm/view?usp=drive_link)
- **Linux Security Advantage**:	Why Linux is considered a less attractive target for security attacks?	Highest recurring 6-mark question. Secures 6 marks regardless of which question (Q13 or Q14) you attempt.
- **Workstation Prep Steps**:	Describe the steps to be followed before putting a workstation on any network?	Highly common 6-mark question, crucial procedure.
- **General/System Hardening**:	Describe the general process of Linux Hardening / Explain the different types of system hardening techniques.	Covers the core 8-mark component for Q13 and often overlaps with Q14(a).
- **Windows Safe Operations**:	How can you ensure the safe operations of a Windows workstation?	Key 8-mark component for Q14.



# Module 3
[Notes](https://drive.google.com/file/d/1l170U_HYZHeohgADOaMU6ZnXxKU5Yv8x/view?usp=drive_link)
- The question "How does HTTP work?" appears in Q15a (2023) and Q16a (2022), demonstrating its importance and flexibility in question slotting.
- The question "Client-Server Model" appears across Q5 (Part A) and Q15b (Part B), making it a high-yield topic.
- The question "DNS Misconfiguration" is a recurring 6-mark topic in Q15b.
## How a Web Browser Works – Simple, Thorough Explanation (Reverse Engineered from Notes)

#### 1. Big Picture First (Simple Overview)
- A web browser is a **client** that talks to a **web server** using HTTP/HTTPS.
- You type a URL → Browser finds the server → Gets HTML/CSS/JS → Converts it into a beautiful webpage you see.
- It does this in **less than a second** using 7 main components working together.

#### 2. 7 Main Components of a Web Browser (Mindmap Style)

**Mnemonic to remember all 7 components**:  
**U B R N J U D** → "**U**ncle **B**ob **R**eally **N**eeds **J**uice **U**p **D**aily"  
1. **U**ser Interface  
2. **B**rowser Engine  
3. **R**endering Engine  
4. **N**etworking  
5. **J**avaScript Interpreter  
6. **U**I Backend  
7. **D**ata Storage

#### 3. Step-by-Step Flow When You Type a URL (Real Working)

1. **You type URL** (e.g., https://google.com)
   - User Interface captures it → sends to Browser Engine

2. **DNS Lookup** (Browser → DNS Resolver)
   - Converts "google.com" → IP address (e.g., 142.250.190.78)
   - Handled by **Networking** component

3. **Send HTTP Request**
   - Networking component sends:
     ```
     GET / HTTP/1.1
     Host: google.com
     ```

4. **Server Responds**
   - Server sends HTML in 8KB chunks (not all at once!)

5. **Rendering Engine Starts Working Immediately** (does NOT wait for full HTML!)
   - Step 5.1: Parse HTML → Build **DOM Tree** (Content Tree)
   - Step 5.2: Parse CSS → Build **CSSOM**
   - Step 5.3: Combine DOM + CSSOM → **Render Tree** (only visible elements)
   - Step 5.4: **Layout / Reflow** → Calculate exact position & size of every element
   - Step 5.5: **Painting** → Draw pixels on screen using UI Backend

6. **JavaScript Execution**
   - If there's JS → JavaScript Interpreter (V8, etc.) runs it
   - JS can change DOM → triggers **reflow + repaint** again!

7. **Page Appears Progressively**
   - You see content appearing as it downloads (better UX)

**Mnemonic for Rendering Steps**: **P-R-L-P** → "**P**arse → **R**ender Tree → **L**ayout → **P**aint"  
(or think "**P**anda **R**uns **L**ate **P**arty")

#### 4. Rendering Engine Deep Dive (Most Important Part)

| Stage              | What Happens                              | Tree Created       | Example Output                     |
|--------------------|-------------------------------------------|---------------------|------------------------------------|
| 1. Parse HTML      | Tokenize → Create nodes                   | DOM Tree           | <div><p>Hello</p></div>           |
| 2. Parse CSS       | Build style rules                         | CSSOM              | p { color: red }                   |
| 3. Render Tree     | Combine DOM + CSSOM (skip display:none)   | Render Tree        | Only visible elements              |
| 4. Layout (Reflow) | Calculate position & size (x,y,width,height) | Coordinates      | div at (10,20), width 300px       |
| 5. Paint           | Draw pixels using UI backend              | Screen             | You see the actual page!           |

**Key Point**: Browser is **incremental** – it shows content as soon as it gets 8KB chunks → fast perceived loading.
#### 5. Summary Mindmap (One-Page Recall)

```
You → URL
      ↓
[User Interface] → [Browser Engine]
      ↓
[Networking → DNS → HTTP Request]
      ↓
Server sends HTML/CSS/JS in 8KB chunks
      ↓
[Rendering Engine]
   ├── Parse HTML → DOM Tree
   ├── Parse CSS  → CSSOM
   ├── Render Tree (DOM + CSSOM)
   ├── Layout → position & size
   └── Paint → draw on screen
      ↓ (if JS changes DOM → repeat Layout+Paint)
[JavaScript Interpreter] runs JS
[Data Storage] saves cookies, cache
```
## Web Browser Attacks – Complete Summary from Module-3  
(Reverse Engineered + Easy to Memorize + Mindmap + Mnemonics)

#### 1. Why Browsers Are the #1 Target (Quick Recall)
- Browsers hold **cookies, passwords, payment data, session tokens**
- Users visit **untrusted sites daily**
- JavaScript runs with **full page access**
- Extensions run with **high privileges**
- Always connected → perfect for **botnets & crypto mining**

**Mnemonic**: Browsers = **“CASH”** machine for attackers  
**C**ookies → **A**PI keys → **S**essions → **H**istory/passwords

#### 2. Top 10 Common Browser Attack Types (From Your Notes)

| No | Attack Name                  | Simple Meaning                                                                 | Real Example / Impact                          | Mnemonic Word |
|----|------------------------------|---------------------------------------------------------------------------------|-------------------------------------------------|---------------|
| 1  | Cross-Site Scripting (XSS)   | Inject malicious JS into a legit website → steals cookies/sessions            | `<script>stealCookies()</script>`             | **X**SS = e**X**ecute Script Silently |
| 2  | Malicious Browser Plug-ins   | Fake extension (PDF reader, adblocker) that reads all your data                | Fake “Video Downloader” extension              | **M**alicious = **M**alware in disguise |
| 3  | Clickjacking                 | Invisible iframe over a button → you click “Like” but actually click “Transfer $500” | Facebook Like-jacking                          | **C**lick = tricked **C**lick |
| 4  | Adware                       | Floods ads, redirects searches, injects affiliate links                       | Browser full of pop-ups                        | **A**dware = **A**nnoying ads |
| 5  | Session Hijacking            | Steal your login cookie → attacker uses your active session                    | Firesheep tool (old but classic)               | **S**ession = **S**tolen identity |
| 6  | Drive-by Downloads           | Just visiting a site → malware auto-downloads (zero-click)                    | Compromised legitimate sites                   | **D**rive-by = **D**ownload without consent |
| 7  | Man-in-the-Browser (MitB)    | Trojan inside browser (Zeus, Carberp) → modifies pages/transactions in real time| You see $100 → bank, attacker changes to $10,000| **M**itB = **M**anipulates in the middle |
| 8  | DNS Poisoning                | Fake DNS reply → example.com → attacker’s server                               | User thinks they are on bank.com               | **D**NS = **D**eceived Navigation |
| 9  | Browser-based Crypto Mining  | Website uses your CPU to mine Monero without consent                          | Coinhive (2017–2019)                           | **C**rypto = **C**PU thief |
|10  | Broken Authentication        | Weak login forms → easy brute-force or credential stuffing                     | No rate limiting on login                      | **B**roken = **B**ypass login |

**Best Mnemonic for all 10**: **“X-M-C-A-S-D-M-D-C-B”**  
→ **“X**mas **C**ame, **A**dware **S**ang, **D**rive-by **M**ade **D**ance **C**razy **B**oy”**


#### 3. Defence in Depth for Browser Attacks (Directly from Your Notes)

| Layer                          | Solution from Module-3                                   | Stops Which Attacks?                           |
|--------------------------------|-----------------------------------------------------------|------------------------------------------------|
| 1. Isolate Execution           | **Browser Isolation** (remote container)                | All malware, MitB, drive-by                    |
| 2. Client-Side Protection      | Block outdated plugins, DOM monitoring, anti-skimming    | XSS, formjacking, malicious extensions        |
| 3. Bot & Behaviour Detection   | Advanced Bot Management (fingerprinting, AI, etc.)       | Automated attacks, crypto mining               |
| 4. Script Monitoring           | Continuously analyze all JS on your site                | Magecart, injected XSS                         |
| 5. Perimeter + App Layer       | Multi-layered Next-Gen WAF + SSL inspection              | XSS payloads, malicious requests               |

**Mnemonic for 5 defences**: **I-C-B-S-P** → “**I**solate → **C**lient protect → **B**ot block → **S**cript scan → **P**erimeter WAF”

#### 4. One-Page Mindmap You Can Draw Right Now

```
               WEB BROWSER ATTACKS
                       │
       ┌───────┴────────┬────────┴────────┐
  Why they happen     Top Attacks         Defence Layers
       │                 │                   │
   - APIs heavy      1. XSS             1. Browser Isolation
   - Users unaware   2. Malicious Ext   2. Client-Side Protection
   - Old browsers    3. Clickjacking    3. Bot Management
   - No script check 4. MitB            4. Script Analysis
                     5. Crypto mining   5. Next-Gen WAF
                     6. Drive-by
                     7. Session Hijack
```
# HTTP – Complete, Simple, Exam-Ready Explanation  
(100% from Module-3 pages 9–15 + extra mnemonics & mindmaps)

### 1. What is HTTP in One Line?
**HTTP = HyperText Transfer Protocol**  
The language that browsers (clients) and web servers use to talk to each other and exchange web pages, images, videos, APIs, etc.

- Application-layer protocol  
- Stateless (each request is independent)  
- Mostly runs over TCP port 80 (HTTP) or 443 (HTTPS)

### 2. The Famous 5-Step Process (Exact Flow from Your Notes)

| Step | Name                         | What Actually Happens                                                                      | Mnemonic |
|-----|------------------------------|-----------------------------------------------------------------------------------------------------|----------|
| 1   | Direct browser to URL        | You type or click → https://www.example.com/index.html                                      | **U**RL |
| 2   | Browser looks up IP          | DNS resolves www.example.com → 93.184.216.34                                                | **D**NS |
| 3   | Browser sends HTTP request   | Browser → Server: GET /index.html HTTP/1.1 + headers                                        | **R**equest |
| 4   | Host sends back HTTP response| Server → Browser: HTTP/1.1 200 OK + headers + actual HTML                                   | **R**esponse |
| 5   | Browser renders the response | Rendering engine paints the page on your screen                                             | **P**aint |

**Super Mnemonic for 5 steps**: **U-D-R-R-P** → “**U**ncle **D**ave **R**eally **R**eally **P**aints”

### 3. Real Example of HTTP Request & Response (Copy-Paste Ready)

**Request (sent by browser)**
```
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0 ...
Accept: text/html
Connection: keep-alive
```

**Response (sent by server)**
```
HTTP/1.1 200 OK
Date: Tue, 18 Nov 2025 ...
Content-Type: text/html; charset=UTF-8
Content-Length: 208

<html><head><title>Welcome</title></head>
<body><h1>Hello World!</h1></body></html>
```


### 4. One-Page Mindmap You Can Draw in 30 Seconds

```
You type URL
      ↓
   1. DNS → IP address
      ↓
   2. HTTP Request
      ├─ Method: GET/POST
      ├─ Path: /index.html
      ├─ Headers: Host, Cookie...
      ↓
   3. HTTP Response
      ├─ Status: 200 OK
      ├─ Headers: Content-Type...
      └─ Body: <html>...</html>
      ↓
   4. Browser paints page
```

### 5. Quick Revision Table (Exam Special)

| Question                              | Answer from Module-3                                      |
|---------------------------------------|-----------------------------------------------------------|
| Full form of HTTP?                    | HyperText Transfer Protocol                               |
| Which layer?                          | Application layer                                         |
| Default port?                         | 80 (HTTP), 443 (HTTPS)                                    |
| Most common method?                   | GET                                                       |
| Most famous success code?             | 200 OK                                                    |
| Most famous error code?               | 404 Not Found                                             |
| Does HTTP remember previous requests? | No → stateless                                            |
| Where is the actual webpage sent?     | In the response body                                      |
| Who starts the conversation?          | Always the client (browser)                               |
## Client-Server Model – Complete, Simple & Exam-Ready (100% from Module-3 Pages 15–18)

#### 1. One-Line Definition (Never Forget)
**Client-Server = “Asker” (Client) talks to “Giver” (Server)**  
- Client **requests** resources/services  
- Server **waits & provides** resources/services  
- Communication over network (LAN/WAN/Internet)

**Mnemonic**: **C**lient **C**alls → **S**erver **S**erves → **C**lient **S**atisfied

#### 2. Roles Perfectly Explained (Mindmap Style)

```
            Client (Requester)                Server (Provider)
                │                                   │
   - Browser, App, Phone                    - Web server, DB server
   - Initiates communication                - Always listening (daemon)
   - Usually DOES NOT share resources      - Shares files, CPU, DB, apps
   - Can be thick/thin/hybrid               - Runs one or more server programs
   - Examples: Your laptop, mobile          - Examples: google.com server, email server
```

#### 3. Types of Clients (From Your Notes)

| Type      | Nickname      | Processing Power                     | Depends on Server? | Example                     |
|-----------|---------------|--------------------------------------|--------------------|-----------------------------|
| Thick     | Fat Client    | Does most work locally               | Very little        | Desktop Java app            |
| Thin      | Lightweight   | Almost zero processing               | Heavily            | Web browser, old terminals  |
| Hybrid    | Best of both  | Stores data on server, processes locally | Medium         | Gmail offline + online mode |

**Mnemonic**: **T**hick = **T**ons of power, **T**hin = **T**otally dependent, **H**ybrid = **H**alf-half

#### 4. Four Architectures/Tiers (Most Important for Exams)

| Tier        | Where UI?      | Where Logic?      | Where Data?       | Pros/Cons                                 | Mnemonic |
|-------------|----------------|-------------------|-------------------|-------------------------------------------|----------|
| 1-Tier      | Same machine   | Same              | Same              | Simple, no network                        | **1** = **One** PC |
| 2-Tier      | Client         | Server            | Server            | Classic (browser + web server)           | **2** = Client + Server |
| 3-Tier      | Presentation (Client) | Application (Middle) | Database (Back) | Most common today (Web + App + DB)     | **3** = UI + Logic + DB |
| N-Tier      | Many layers    | Distributed       | Distributed       | Microservices, scalable but complex      | **N** = **N**umber of layers |

**Best Mnemonic for tiers**: **1-2-3-N** → “**1** PC, **2** talk, **3** layers, **N** flexible”

#### 5. Benefits of Client-Server Model (Direct from Notes – 5 Points)

| # | Benefit                                   | Simple Meaning                                    |
|---|-------------------------------------------|----------------------------------------------------|
| 1 | Centralised data & management             | Easy backup, authentication, updates              |
| 2 | Easy to scale                             | Add more servers/clients without downtime         |
| 3 | Access from anywhere                      | Not tied to physical location                     |
| 4 | Nodes are independent                     | Upgrade one PC without affecting others           |
| 5 | Platform-agnostic data transfer           | Windows client ↔ Linux server = no problem        |

**Mnemonic for 5 benefits**: **C-E-A-I-P** → “**C**entral **E**asy **A**nywhere **I**ndependent **P**latform-free”


#### 6. Quick Exam Table (Copy-Paste Answers)

| Question                                      | Answer from Module-3                                      |
|-----------------------------------------------|------------------------------------------------------------|
| Who initiates communication?                  | Always the Client                                          |
| Who shares resources?                         | Only the Server                                            |
| Most common real example?                     | Web browser (client) + Web server                  |
| Best architecture for modern web apps?        | 3-Tier or N-Tier                                           |
| Advantage of central management?              | Easy protection, authentication, backups           |
| Can client and server be on same machine?    | Yes (but rare)                                             |
## Email Protocols – Complete Module-3 Style Summary  
(Everything you need for exams + mnemonics + mindmaps)

#### 1. The 3 Main Email Protocols (Never Mix Them Up Again)

| Protocol | Full Name                   | Job (Simple Meaning)                              | Direction                     | Port (Plain) | Port (SSL/TLS) | Mnemonic Phrase                  |
|----------|-----------------------------|----------------------------------------------------|-------------------------------|--------------|----------------|----------------------------------|
| SMTP     | Simple Mail Transfer Protocol| **SENDS** email (outgoing)                        | Client → Server OR Server → Server | 25 (or 587)  | 465            | **S**MTP = **S**end Mail To People |
| POP3     | Post Office Protocol v3     | **DOWNLOADS** email & usually deletes from server | Server → Client               | 110          | 995            | **P**OP = **P**ull Old Post        |
| IMAP     | Internet Message Access Protocol| **SYNC** email across all devices (keeps on server)| Server ↔ Client               | 143          | 993            | **I**MAP = **I**nternet Mail Always Present |

**Best Mnemonic to remember all 3 in order**:  
**S-P-I** → “**S**end with **P**OP, but **I** prefer **IMAP**”  
OR  
**SMTP → POP3 → IMAP** → “**S**ally **P**osted **I**MAP”

#### 2. Real-Life Flow When You Click “Send” (Step-by-Step)

1. Your mail client (Outlook, Gmail app) → uses **SMTP** → sends to YOUR mail server (e.g., smtp.gmail.com)  
2. Your mail server → uses **SMTP again** → delivers to recipient’s mail server  
3. Recipient opens their mail client → uses **IMAP** or **POP3** → fetches the message

**Mindmap (draw this in 10 seconds)**

```
You click SEND
      │
   SMTP (587/465)
      │
Your Mail Server ──SMTP──► Recipient Mail Server
                                 │
                            IMAP (993) or POP3 (995)
                                 │
                          Recipient’s Phone/PC
```

#### 3. POP3 vs IMAP – Exam Table (Most Asked Question)

| Feature                       | POP3                                 | IMAP (Winner for modern use)          |
|--------------------------------|--------------------------------------|----------------------------------------|
| Where emails stay             | Downloaded → deleted from server     | Always stay on server                  |
| Access from multiple devices  | Only on one device                   | Perfect sync everywhere                |
| Works offline                 | Yes (after download)                 | Limited (needs sync first)             |
| Storage usage on server       | Saves server space                  | Uses server space                      |
| Folder support                | Only Inbox                           | Full folders, labels, flags            |
| Today’s usage                 | Almost dead (banks, old systems)     | Gmail, Outlook, iPhone, everything    |

**Mnemonic**:  
POP3 = **P**ull **O**nce **P**ermanently  
IMAP = **I**nternet **M**ail **A**lways **P**resent

#### 4. Quick Revision Table (Copy-Paste for Exam)

| Question                               | Answer                                   |
|----------------------------------------|------------------------------------------|
| Which protocol is used to send email?  | SMTP                                     |
| Which protocol keeps email on server?  | IMAP                                     |
| Which protocol downloads & deletes?    | POP3                                     |
| Can SMTP transfer between two servers? | Yes (server-to-server)                   |
| Most modern choice for mobile + PC?    | IMAP + SMTPS                             |

#### 5. One-Page Mindmap You Can Draw Now

```
                EMAIL PROTOCOLS
                       │
        ┌──────┴───────┬──────┴───────┐
      SEND             RECEIVE        RECEIVE + SYNC
        │                 │               │
      SMTP             POP3             IMAP
   (25/587/465)       (110/995)        (143/993)
   “Push”             “Pull once”      “Always live”
```
## DOMAIN NAME SYSTEM (DNS) SECURITY

DNS is a critical application layer protocol that translates human-readable domain names (e.g., example.com) into machine-readable Internet Protocol (IP) addresses (e.g., 93.184.216.34).

---

### I. DNS BASICS & COMPONENTS (For Part A & Diagrams)

| Component | Function |
| :--- | :--- |
| **DNS Resolution** | The process of translation and lookup of a domain name to an IP address. |
| **DNS Server / Resolver** | The server that handles the query (e.g., ISP server, or a corporate DNS server). It provides the answer or refers to other servers. |
| **Root Name Server** | The first point of contact in the DNS hierarchy; maintains an index of all TLD servers. |
| **TLD Server** | Handles Top-Level Domains (.com, .org, .edu). Directs the query to the correct Authoritative Server. |
| **Authoritative Name Server** | The final server for a domain; contains the actual resource records (e.g., the 'A' record with the IP address). |
| **DNS Caching** | Storing previous query answers (IPs) closer to the client (on the browser, OS, or recursive resolver) to speed up future lookups. |
| **Reverse Lookup** (Q6 - Model) | Translating an IP address back to a domain name (used for verification, often by mail servers). |

---

### II. DNS QUERY TYPES (For Part B - Explaining Working)

| Query Type | Description | Where it Happens |
| :--- | :--- | :--- |
| **Recursive Query** | A request from the **client** to the **recursive resolver** asking for the *full name resolution* (an answer or an error). | Client $\leftrightarrow$ Recursive Resolver |
| **Iterative Query** | Requests between DNS servers where the responding server does **not** give the full answer but a *referral* (the address of the next server to ask). | Recursive Resolver $\leftrightarrow$ Root/TLD/Authoritative Servers |
| **Nonrecursive Query** | A query where the resolver already **knows the answer** (e.g., it is cached) and can return it immediately. | Resolver (from its cache) $\rightarrow$ Client |

---

### III. SECURITY ISSUES & ATTACKS (For Q15 b) - 6 Marks)

The security issues with DNS are primarily focused on **integrity** and **redirection**.

| Security Issue / Attack | Description | Impact |
| :--- | :--- | :--- |
| **DNS Misconfiguration** (Q15b - Frequent) | Incorrectly configured DNS servers, records, or zone files. | Causes failed lookups, service downtime, or unintentional traffic redirection. |
| **DNS Cache Poisoning** | Injecting false information/records into a DNS resolver's cache. | Redirects legitimate application requests from a valid IP address to a malicious host network. |
| **DNS Server Hijacking / Redirection** | An attack that tricks the end-user into thinking they are communicating with a legitimate domain when they are communicating with an attacker's IP/domain. | Used to direct users to phishing sites or malware distribution points. |
| **Domain Name Character Substitution** | Replacing a character in a domain name with a similar-looking character (e.g., '1' with 'l') to fool a user. | Exploited heavily in Phishing attacks. |

---

### IV. DEFENSE (Tips and Tricks)

*   **DNS Security Extensions (DNSSEC):** The primary defense mechanism. It supports **cryptographically signed responses** to ensure the integrity and authenticity of the DNS data.
*   **Secure Configuration:** Properly securing and configuring DNS servers to prevent unauthorized changes and Zone Transfer attacks.
*   **Monitoring:** Checking DNS logs for anomalous query behavior (e.g., high volume of unexpected queries).
*   **Manage TTL (Time-To-Live):** Properly setting TTL to control how long records are cached, limiting the duration of a cache poisoning attack.
# Module 4
[Notes](https://drive.google.com/file/d/1i3f6TXVt48WO2N3zFso5NCRlhz2P0_Fx/view?usp=drive_link)
## ✍️ Principles of Cryptography (8 Marks)

**Principles of Cryptography are the guidelines for designing secure systems using cryptographic primitives.** The following points summarize them:

1. **Building Blocks:**  
   Cryptographic primitives are the basic building blocks of security systems (e.g., hash functions, encryption).

2. **Reliability:**  
   They must be highly reliable and perform exactly as specified. If broken with fewer operations than claimed, the primitive fails.

3. **Avoid New Designs:**  
   It is essentially never sensible or secure to design new primitives casually, since they are complex, error‑prone, and require years of testing.

4. **Community Scrutiny:**  
   Even if a primitive looks good, it must withstand peer review by the cryptographic community before being trusted.

5. **Limited Scope:**  
   A primitive alone cannot provide complete security. For example, encryption alone does not ensure integrity or authentication.

6. **Combination in Protocols:**  
   Primitives must be combined in protocols (e.g., AES + SHA‑256) to achieve multiple security requirements like confidentiality and integrity.

7. **Protocol Design Matters:**  
   Most vulnerabilities arise not from weak primitives but from poor protocol design or buggy implementation.

8. **Analogy Principle:**  
   Just as programmers use established languages instead of inventing new ones, cryptographers should rely on proven primitives.

## Cryptographic Primitives (8 Marks)
Cryptographic Primitives includes:
1. **Hash Functions:**  
   - Maps data of arbitrary size to fixed-size output (hash).  
   - Properties: Deterministic, fast, pre-image resistance, collision resistance.
   - Examples: SHA-256, MD5.
   - Use Cases: Data integrity, digital signatures.
   - Challenges: Vulnerable to collision attacks (e.g., MD5).
2. **Symmetric Key Encryption:**
    - Same key for encryption and decryption.
    - Fast, suitable for large data.
    - Examples: AES, DES.
    - Use Cases: Secure communication, data storage.
    - Challenges: Key distribution, scalability.
3. **Asymmetric Key Encryption:**
    - Uses public/private key pair.
    - Slower, suitable for small data.
    - Examples: RSA, ECC.
    - Use Cases: Key exchange, digital signatures.
    - Challenges: Computational overhead.
4. **Digital Signatures:**
    - Provides authenticity, integrity, non-repudiation.
    - Uses asymmetric encryption.
    - Examples: RSA signatures, ECDSA.
    - Use Cases: Document signing, software distribution.
    - Challenges: Key management.
5. **Random Number Generators (RNGs):**
    - Generate random numbers for cryptographic use.
    - Types: True RNGs (hardware-based), Pseudo RNGs (algorithm-based).
    - Use Cases: Key generation, nonce creation.
    - Challenges: Ensuring randomness quality.

# Module 5
[Notes](https://drive.google.com/file/d/1puF4SGOPXTveZbyFvIqPXiPRHCC__Nm2/view?usp=sharing)
- Firewalls: Types (4-5 categories) and the difference between Stateful and Proxy. (Easy to write 8M).
- Penetration Testing: Definition, 5 Stages (P. 10), and the different testing types (Blind, Grey, White). (Easy to write 6M/8M).
- IDS/Auditing: Types of IDS, and the importance and steps of Security Auditing. (Easy to write 6M/8M).
## **1. FIREWALL BASICS** (Pages 2-3)
  - **Def**: Barrier between **private internal net** & **public internet**. Monitors traffic → Allows good, blocks bad (based on org policies).
  - **Purpose**: Let non-threat traffic **IN**, keep danger **OUT**.
  - **Types** (Hardware vs Software):
    - **Hardware**: Physical box (e.g., broadband router/appliance).
    - **Software**: Program on PC (e.g., host firewall). *Best: Both together*.
  - **Key Technique**: **Packet Filtering** – Checks packets using rules on protocols, IP, ports.
  - **Mnemonic**: **F**irewall = **F**ilter **I**n/**O**ut (FIO).

---

### **2. PACKET FILTERING FIREWALL** (Pages 3-4)
  - **How it works**:
    - Packets = Small data chunks (fault-tolerant).
    - Reordered at destination → Increases speed/channel use.
    - Contains: Source/Dest IP, Protocol (TCP/UDP/ICMP), Ports, Flags, Payload.
  - **Allow/Deny Criteria** (6 checks – **SIP-PPF**):
    1. **S**ource IP
    2. **D**est IP (wait, mnemonic has S for source, but dest is implied)
    3. **P**rotocol
    4. **P**orts (src/dest)
    5. **F**lags (e.g., SYN for connect)
    6. Interface (NIC in/out)
  - **4 Sub-Types** (Mindmap branch: **Dyna-Sta-less-ful**):
    - **Dynamic**: Changes rules on-fly.
    - **Static**: Fixed rules.
    - **Stateless**: No connection memory.
    - **Stateful**: Tracks connection state (best for TCP).
  - **Mnemonic**: **Packet = SIPP-FI** (Source IP, Protocol, Ports, Flags, Interface).

---

### **3. CIRCUIT-LEVEL GATEWAYS** (Pages 4-6)
  - **Purpose**: Filters at **session layer** (OSI). Hides internal host. Blocks unauthorized via virtual circuits.
  - **Working** (2 TCP connections):
    1. Inner host ↔ Gateway.
    2. Gateway ↔ Outer host.
    - Maintains **circuit table** → Validates packets.
  - **Features**:
    - Works session layer (TCP/IP).
    - Hides private network.
    - Example: **SOCKS** proxy.
  - **Adv** (Mindmap: **PHACE**):
    - **P**roxy hide.
    - **H**ides packets.
    - **A**ddress schemes easy.
    - **C**heap.
    - **E**very app no separate proxy.
  - **Disadv**:
    - No packet inspect.
    - Needs frequent updates.
    - No data-leak protect.
    - Vendor-modified TCP/IP.
  - **Mnemonic**: Circuit = **C**onnect **I**nner-**R**outer-**C**onnect **U**ser **I**nside **T**able (CIRCUIT).

---

### **4. OTHER FIREWALL TYPES** (Page 7)
  - **Application-Level Gateways (ALG)**: App-specific (e.g., VOIP). Translates addresses. Acts as proxy.
  - **Cloud Firewalls (FWaaS)**: Software in cloud. For modern online apps/business.
  - **Unified Threat Management (UTM)**: All-in-one box (firewall + antivirus + etc.).
  - **Next-Gen Firewall (NGFW)**: Detects/block app-level attacks. Enforces policy at app/port/protocol.
  - **Mnemonic**: Types = **A-C-U-N-P** (App, Cloud, UTM, Next-gen, Personal).

---

### **5. PERSONAL FIREWALL & RULES** (Page 8)
  - **Personal**: On single PC. Controls traffic to/from it. Diff from conventional (policy per computer, not network).
  - **Firewall Rules**: Block/allow packets. Create via: New → XML import → Edit → Duplicate.
  - **Mnemonic**: Rules = **C-R-E-A-T-E** (Create, Read, Edit, Assign, Test, Enforce).

---

### **6. INTRUSION DETECTION/RESPONSE** (Page 9)
  - **IDS**: Monitors malicious activity/policy violation. Reports to central system.
    - **Methods**: 
      1. **Signature**: Known patterns.
      2. **Anomaly**: Unusual behavior.
  - **IRS**: Auto-mitigates attacks. Static/dynamic. Often with **ASMF** system.
  - **Mnemonic**: IDS = **S**ignature or **A**nomaly (SA).

---

### **7. PENETRATION TESTING (PEN TEST)** (Pages 10-12)
  - **Def**: Authorized fake attack → Find weaknesses.
  - **5 Stages** (Cycle Mindmap – **PR-SGM-A**):
    1. **Planning/Recon**: Goals, intel (domains, mail servers).
    2. **Scanning**: Tools → Static (code inspect) vs Dynamic (running app).
    3. **Gaining Access**: Exploit (SQLi, XSS, privilege escalate).
    4. **Maintaining Access**: Backdoors, APT imitation.
    5. **Analysis**: Report vulnerabilities, data accessed, time undetected.
  - **Types**:
    - **External**: Public assets (web, DNS).
    - **Internal**: Behind firewall (rogue employee sim).
    - **Blind**: Only company name given.
    - **Double-Blind**: Security unaware.
    - **Targeted**: Tester + security collaborate.
  - **Mnemonic**: Stages = **P**lan **R**econ **S**can **G**ain **M**aintain **A**nalyze (PRSGMA).

---

### **8. SECURITY AUDITING** (Page 13)
  - **Def**: Full check of info system vs standards/regulations.
  - **Audits**:
    - Physical components.
    - Apps/software/patches.
    - Network vuln (in/out).
  - **Mnemonic**: Audit = **P-A-N** (Physical, Apps, Network).
- **WAP ARCHITECTURE - CONCISE REVERSE-ENGINEERED NOTES** (Pages 17-25)
  - *Goal*: Grasp in 5 min → Memorize via **L-A-Y-E-R-S** mnemonic (Layers: App-Session-Trans-Sec-Transport-Datagram). Draw mindmap. Link: WAP = Mobile WWW bridge.

---

## **1. WAP** (Page 17-18)
  - **Def**: **W**ireless **A**pplication **P**rotocol – For micro-browsers. Access internet on mobiles via **WML** (XML-based, not HTML).
  - **History**: 1998 WAP Forum (Nokia/Ericsson/etc.) → 2002 merged into **OMA**.
  - **Model Flow** (Client-Server + Gateway):
    1. Mobile: Open micro-browser → Select URL.
    2. Sends WAP-encoded request → **WAP Gateway**.
    3. Gateway: Translate WAP → HTTP → Web Server.
    4. Server response → WML file → Gateway → Mobile (visible in micro-browser).
  - **Mnemonic**: Flow = **M-G-W-S-M** (Mobile-Gateway-WebServer-Gateway-Mobile).

---

### **2. WAP PROTOCOL STACK** (Pages 19-20) – **6 Layers** (Mindmap: Stack like OSI but optimized for wireless/low-bandwidth)
  - **Top to Bottom** (Mnemonic: **A-S-T-S-T-D** → "A Smart Tiger Swims To Dive"):
    1. **Application (WAE)**: Device specs + WML/WMLScript. Content dev languages.
    2. **Session (WSP)**: Fast suspend/resume connections. Binary HTTP.
    3. **Transaction (WTP)**: Lightweight, on UDP. Transaction support (acks, retransmit). Classes 0-2.
    4. **Security (WTLS)**: Integrity/privacy/auth. Like TLS but optimized (datagram, handshake).
    5. **Transport (WDP)**: Consistent format to upper layers. Port addressing, segmentation.
    6. **Datagram (Bearer)**: Adapts to carriers (SMS, CSD, GPRS, USSD).
  - **Key**: Layers accessible via interfaces. External apps can bypass to session/trans/sec/transport.

---

### **3. WAP ARCHITECTURE FEATURES** (Page 22)
  - **Scalable/Extensible**: Layered (OSI-like) for mobile app dev.
  - **Interoperability**: Operators build apps for varied wireless platforms.
  - **Addressing**: URL/URI.
  - **WAE Details**: WWW + mobile telephony combo. WML for content, WMLScript for input validation.
  - **WTA (Wireless Telephony App)**: Telephony services via **WTAI** (call from WML/Script). Repository for offline services (event-based: call answer/disconnect). Service indication (notifications).

---

### **4. PROTOCOL DEEP DIVE** (Pages 23-24)
  - **WSP**: Reliable content exchange. Supports HTTP 1.1 methods. Suspend idle sessions. Async requests.
  - **WTP**: Thin-client friendly. Unique IDs, acks, no security/setup phases.
  - **WTLS**: TLS-based. Goals: Integrity, privacy, auth, DoS protect. Features: Datagram, optimized handshake, key refresh.
  - **WDP**: Port nums for apps. Segmentation/reassembly. Bearer adaptation (e.g., GSM SMS).
  - **Bearers**: SMS, CSD, GPRS, USSD.

---

### **5. WAP GATEWAY** (Page 25)
  - **Role**: Proxy between WAP devices & WWW. Translates WAP → HTTP/WML.
  - **Model**: Adds intermediary to client-server. Micro-browser request → HTTP URL → Server.


## **WAP PROTOCOL STACK ELEMENTS - ONE BY ONE** (Pages 19-24)
  - *Goal*: Layer-by-layer breakdown → Memorize via **A-S-T-S-T-D** mnemonic ("**A** Smart **T**iger **S**wims **T**o **D**ive"). Link to OSI (WAP = slim wireless version). Repeat stack order 3x.

---

### **1. WAE - Wireless Application Environment** (Top Layer, Page 20/22)
  - **What**: General-purpose app environment. Combo of **WWW + mobile telephony**.
  - **Key Role**: Interoperable apps for operators/providers across wireless platforms.
  - **Components**:
    - Device specs.
    - Content langs: **WML** (markup), **WMLScript** (validation/scripting).
  - **Addressing**: URL/URI.
  - **Mnemonic**: WAE = **W**eb **A**pp **E**nvironment (for mobiles).

---

### **2. WTA - Wireless Telephony Application** (Part of WAE, Page 22)
  - **What**: Extension for **telephony services** in WAP (not full layer, but key framework).
  - **Key Role**: Build call-related apps (e.g., answer/disconnect triggers).
  - **Components**:
    - **WTAI**: Interface to call from WML/WMLScript.
    - **Repository**: Store services offline in device → Access on events (no network needed).
    - **Service Indication**: Push notifications → Trigger WTA services.
  - **Mnemonic**: WTA = **W**ireless **T**elephony **A**pps (call events).

---

### **3. WSP - Wireless Session Protocol** (Session Layer, Page 20/23)
  - **What**: Reliable content exchange client-server. Binary version of **HTTP**.
  - **Key Role**: Organized sessions over unreliable wireless.
  - **Features**:
    - All **HTTP 1.1 methods**.
    - **Suspend/resume** idle sessions (frees resources).
    - **Asynchronous requests** (multi-req → Better airtime use).
  - **Mnemonic**: WSP = **W**ireless **S**ession **P**rotocol (HTTP binary + suspend).

---

### **4. WTP - Wireless Transaction Protocol** (Transaction Layer, Page 20/23)
  - **What**: Lightweight, transaction-oriented. Runs on **UDP** (part of TCP/IP).
  - **Key Role**: Efficient for thin clients (mobiles).
  - **Features**:
    - Unique IDs, acks, duplicate removal, retransmit.
    - **Classes**: 0 (no ack), 1-2 (confirm every msg).
    - No security, no setup/teardown phases.
  - **Mnemonic**: WTP = **W**ireless **T**ransaction **P**rotocol (UDP + acks).

---

### **5. WTLS - Wireless Transport Layer Security** (Security Layer, Page 20/24)
  - **What**: Based on **TLS** (industry std). Between WAP client & gateway/proxy.
  - **Key Role**: Secure comms in low-bandwidth.
  - **Goals** (4): Data **integrity, privacy, authentication, DoS protection**.
  - **Features**:
    - Datagram support.
    - Optimized handshake.
    - Dynamic key refreshing.
  - **Mnemonic**: WTLS = **W**ireless **T**LS (secure + optimized).

---

### **6. WDP - Wireless Datagram Protocol** (Transport Layer, Page 20/24)
  - **What**: Presents consistent data format to upper layers.
  - **Key Role**: Abstraction over varied bearers.
  - **Features**:
    - **Port numbers** for app addressing.
    - Segmentation/reassembly.
    - Optional error detection.
    - Multi comms over one bearer.
    - **Adaptation** to bearer specifics (e.g., GSM SMS).
  - **Mnemonic**: WDP = **W**ireless **D**atagram **P**rotocol (ports + adapt).

---

### **7. Bearer Layer** (Bottom, Not a Protocol - Page 24)
  - **What**: Underlying services WDP adapts to.
  - **Examples**: SMS, CSD, GPRS, USSD.
  - **Key Role**: Actual wireless transport (WAP operates over these).
  - **Mnemonic**: Bearer = **B**ottom **E**ntry **A**dapted **R**adio (BEAR).

---

### **MINDMAP SKETCH** (Draw vertical stack → Label each)
```
WAE (Apps + WTA telephony)
   |
WSP (Sessions)
   |
WTP (Transactions)
   |
WTLS (Security)
   |
WDP (Datagram/Ports)
   |
Bearer (SMS/GPRS...)
```
## **IP SECURITY (IPSec) - CONCISE REVERSE-ENGINEERED NOTES** (Pages 25-27)
  - *Goal*: Grasp in 5 min → Memorize via **U-C-W-S-A** mnemonic ("**U**ses **C**omponents **W**ork **S**A **A**uth"). Link: IPSec = Secure IP tunnel (VPN-like). Repeat components 3x.

---

### **1. IPSec OVERVIEW** (Page 25)
  - **Def**: IETF std suite of protocols (2 points across IP net). Provides **auth, integrity, confidentiality**.
  - **Key**: Encrypts/decrypts/auth packets. Defines key exchange/management.
  - **Mnemonic**: IPSec = **I**P **Sec**ure (auth + encrypt).

---

### **2. USES OF IP SECURITY** (Page 25) – **4 Main** (Mindmap: **E-R-A-P**)
  1. **E**ncrypt app-layer data.
  2. **R**outer security (routing data over public net).
  3. **A**uth without encrypt (verify sender).
  4. **P**rotect via **tunneling** (encrypt all between endpoints → VPN).
  - **Mnemonic**: Uses = **ERAP** (Encrypt, Router, Auth, Protect-tunnel).

---

### **3. COMPONENTS OF IP SECURITY** (Page 26) – **5 Key** (Mnemonic: **E-A-I-S-K** → "Encrypt Auth IKE SA Key")
  1. **ESP (Encapsulating Security Payload)**: Integrity + **encryption** + auth + anti-replay. Auth for payload.
  2. **AH (Authentication Header)**: Integrity + auth + anti-replay. **No encryption**. Protects vs unauthorized packets.
  3. **IKE (Internet Key Exchange)**: Dynamic key exchange + SA negotiation (2 devices).
  4. **SA (Security Association)**: Shared security attributes (2 entities for secure comm).
  5. **ISAKMP (Internet Security Association & Key Management Protocol)**: Framework for auth + key exchange. Sets up SAs + direct host connects.
     - IKE adds: Msg protection + std algos (SHA/MD5). Unique ID per packet → Discard bad.
  - **Mnemonic**: Components = **ESP-AH-IKE-SA-ISAKMP** (Encrypt Secure Payload, Auth Header, Key Exchange, Secure Assoc, Key Mgmt).

---

### **4. WORKING OF IP SECURITY** (Page 27) – **7 Steps** (Flow Mindmap: **C-P-I-P-N-E-T**)
  1. **C**heck policy: Transmit via IPSec? Apply encryption.
  2. **P**acket check: Incoming encrypted properly?
  3. **I**KE Phase 1: Auth hosts → Secure channel. Modes: **Main** (secure) / **Aggressive** (fast).
  4. **P**hase 1 channel → Negotiate encryption.
  5. **N**egotiate IKE Phase 2: Crypto algos + secret keys (over secure channel).
  6. **E**xchange data: Encrypt/decrypt via IPSec SAs in tunnel.
  7. **T**erminate: Session end/timeout → Discard keys.
  - **Mnemonic**: Working = **CPIPNET** (Check Policy, Packet, IKE1, Phase-negotiate, Negotiate2, Exchange, Terminate).

---

### **5. KEY CONCEPTS**
  - **Anti-Replay**: Unique ID → Detect duplicates/unauth.
  - **Tunnel Mode**: Full packet encrypt (VPN).
  - **Transport Mode**: Payload only.

---

### **MINDMAP SKETCH** (Draw: Central **IPSec** → Branches)
```
          Uses (ERAP)
             |
Components --+  ESP (encrypt)
             |  AH (auth)
             |  IKE/SA/ISAKMP
             |
         Working (7-step flow)
```
## **GSM SECURITY - CONCISE REVERSE-ENGINEERED NOTES** (Pages 28-29)
  - *Goal*: Grasp in 5 min → Memorize via **E-A-P-T** mnemonic ("**E**nd-to-end **A**nonymity **P**rivacy **T**emp IDs"). Link: GSM = Secure calls + user hide. Repeat process 3x.

---

### **1. GSM SECURITY OVERVIEW** (Page 28)
  - **Def**: Most secure cellular system. **End-to-end security**: Call confidentiality + **subscriber anonymity**.
  - **Methods**:
    - **Temp IDs**: Assigned to hide real subscriber number.
    - **Encryption algos** + **frequency hopping** (digital/signaling).
  - **Mnemonic**: GSM Sec = **G**uaranteed **S**afe **M**obile (temp + encrypt).

---

### **2. MOBILE STATION AUTHENTICATION** (Page 28-29) – **Challenge-Response** (Mindmap: Flow cycle)
  - **Process** (6 Steps – **R-S-C-M-V-F**):
    1. **R**AND (128-bit random) sent to **MS** (Mobile Station).
    2. **S**RES (32-bit) computed by MS: Encrypt RAND with **A3 algo** + **Ki** (individual key).
    3. **C**ompare: Network repeats calc → Verify SRES match.
    4. **M**atch → Auth success → Continue.
    5. **V**iolate → Fail → Terminate + alert MS.
    6. **F**inal: Processed in **SIM** (no IMSI/Ki over air).
  - **Key Storage**: **Ki** in SIM + AUC/HLR/VLR (never radio).
  - **Mnemonic**: Auth = **RAND → A3+Ki → SRES** (Random Algo Key Signed Response).

---

### **3. KEY FEATURES** (Implied from process)
  - **Privacy**: Real ID hidden post-auth.
  - **Integrity**: Encrypted comms.
  - **No Air Leak**: Sensitive data stays in SIM.
  - **Standardized**: A3 algo across GSM.

---

### **4. RELATED: WTLS (Page 29) - Bonus Link to WAP**
  - **Role**: Privacy + integrity + auth for WAP apps.
  - **Base**: Like **TLS** but optimized (low BW mobiles).
  - **3 Diff from TLS** (Mnemonic: **C-C-P**):
    1. **C**ompressed structures (bit-fields, truncate crypto).
    2. **C**ompressed certs (smaller X.509).
    3. **P**acket-based (not stream) → Works with SMS.
  - **Mnemonic**: WTLS = **W**ireless **T**LS **S**lim (Compressed + Packet).

---

### **MINDMAP SKETCH** (Draw: Central **GSM Auth** → Cycle)
```
         Temp ID (Hide)
            |
RAND --> MS (SIM: A3+Ki) --> SRES
            |
       Network Compare --> Match/Fail
            |
       Encrypt + Hop (Privacy)
```
## **SSL / SECURE SOCKETS LAYER - CONCISE REVERSE-ENGINEERED NOTES** (Pages 32-34)
  - *Goal*: Grasp in 5 min → Memorize via **H-E-A-D** mnemonic ("**H**andshake **E**ncrypt **A**uthenticate **D**igital-cert"). Link: SSL = Padlock in browser (now TLS). Repeat process 3x.

---

### **1. SSL OVERVIEW** (Page 32)
  - **Def**: Standard for **secure document transmission** over network (created by Netscape).
  - **Full Name**: **Secure Sockets Layer** → Now evolved into **TLS** (1999 onwards).
  - **Core Job**: Creates **encrypted link** between **web server ↔ browser**.
  - **Layer**: Sits **on top of TCP** (transport layer) → Encrypts above it.
  - **Mnemonic**: SSL = **S**ecure **S**ocket **L**ink (padlock).

---

### **2. HOW SSL WORKS** (Page 32-33) – **3 Main Things**
  1. **Encryption**:
     - Turns data into jumbled mess → Only recipient decrypts.
  2. **Handshake** (Authentication):
     - Browser & server say “Who are you?” → Verify identity.
  3. **Digital Signature** (Integrity):
     - Ensures data not tampered → Receiver trusts it’s original.
  - **Mnemonic**: Works = **H-E-A-D** → **H**andshake, **E**ncrypt, **A**uthenticate, **D**igital sign.

---

### **3. SSL HANDSHAKE & CRYPTO PROCESS** (Page 33)
  - **Asymmetric Crypto** (Public + Private Key):
    - Browser generates **public key** + **private key** (private never leaves browser/server).
    - **CSR** (Certificate Signing Request): Contains public key + domain + org info.
    - Server sends **SSL Certificate** (signed by trusted CA) containing public key.
  - **Flow** (Simplified):
    1. Client Hello → Server Hello.
    2. Server sends **certificate** (public key).
    3. Client verifies cert → Generates session key → Encrypts with server public key.
    4. Secure symmetric session starts (faster than asymmetric).
  - **Mnemonic**: Keys = **Pub-Priv Pair** → "Public to all, Private to me".

---

### **4. OBJECTIVES OF SSL** (Page 33) – **3 Big Goals**
  1. **Data Integrity**: No tampering (via Record, Handshake, ChangeCipherSpec, Alert protocols).
  2. **Client-Server Authentication**: Cryptographic proof of identity.
  3. **Confidentiality**: Encrypted data.
  - **Mnemonic**: Goals = **CIA** backwards → **A**uth **I**ntegrity **C**onfidentiality.

---

### **5. HOW TO GET SSL/TLS CERTIFICATE** (Page 34) – **4 Steps**
  1. Generate **public + private key pair** on server.
  2. Create **CSR** (public key + domain + org info).
  3. Send CSR to trusted **CA** (e.g., SSL.com, Let’s Encrypt).
  4. CA verifies → Issues signed **certificate** → Install on server.
  - **Types**: DV (Domain), OV (Organization), EV (Extended Validation – green bar).

---

### **6. SSL vs TLS**
  - SSL 1.0 → Never released.
  - SSL 2.0 → 1995 (weak).
  - SSL 3.0 → 1996 (last SSL).
  - **TLS 1.0** (1999) = SSL 3.1 → Stronger, modern.
  - **Today (2025)**: TLS 1.2 / 1.3 mandatory. SSL = outdated/deprecated.

---

### **MINDMAP SKETCH** (Draw: Central **SSL Padlock** → 3 Branches)
```
           Handshake
              |
Encryption --+  Asymmetric → Symmetric
              |
         Integrity + Auth
              |
         Get Cert (Key→CSR→CA→Install)
```
## **GPRS - GENERAL PACKET RADIO SERVICE - CONCISE REVERSE-ENGINEERED NOTES** (Module-5 Typical Notes)
  - *Goal*: Grasp in 5 min → Memorize via **G-P-R-S** mnemonic ("**G**SM **P**acket **R**adio **S**ervice"). Link: GPRS = Internet on 2G phones (1999–2000). Repeat architecture 3x.

---

### **1. GPRS OVERVIEW**
  - **Def**: **Packet-switched** extension over **circuit-switched GSM** → Brings “always-on” data to 2G mobiles.
  - **Nickname**: **2.5G** (bridge between 2G GSM & 3G UMTS).
  - **Key Idea**: Instead of dedicating a full voice channel, data is broken into **packets** → Shared radio channels → Much cheaper & faster than GSM data (9.6 kbps).
  - **Mnemonic**: GPRS = **G**SM + **P**ackets = Internet on phone.

---

### **2. WHY GPRS WAS NEEDED** (Advantages over GSM Data)
  - **Always-on** → No dial-up every time.
  - **Faster**: Theoretical 172 kbps (real ~30–80 kbps).
  - **Volume-based billing** (pay per MB, not per minute).
  - **Simultaneous voice + data** (with Class A/B phones).
  - **Mnemonic**: Benefits = **A-F-V-S** → Always-on, Faster, Volume-billing, Simultaneous.

---

### **3. GPRS NETWORK ARCHITECTURE** (New Elements Added to GSM)
  - **Core GSM elements remain**: MS, BTS, BSC, MSC, HLR/VLR.
  - **New GPRS-specific nodes** (Mnemonic: **SGSN-GGSN-PCU** → "S-G-P")
    1. **PCU** (Packet Control Unit) → Inside or near BSC → Converts packet data to radio blocks.
    2. **SGSN** (Serving GPRS Support Node)
       - Mobility management, authentication, session handling.
       - Tracks phone location (cell/routing area).
       - Like “VLR for packets”.
    3. **GGSN** (Gateway GPRS Support Node)
       - Gateway to external networks (Internet, corporate).
       - Assigns IP address to mobile (like home router).
       - Like “foreign agent + NAT”.
  - **Mnemonic**: SGSN = Local boss, GGSN = Internet gate.

---

### **4. GPRS INTERFACES** (Mindmap Connections)
  - **Gb**: BSC/PCU ↔ SGSN (packet over Frame Relay/ATM).
  - **Gn/Gp**: SGSN ↔ GGSN (GPRS Tunneling Protocol – GTP).
  - **Gi**: GGSN ↔ Internet/PDN.
  - **Gr**: SGSN ↔ HLR (for subscriber info).
  - **Gd**: SGSN ↔ SMS centers (SMS over GPRS).

---

### **5. GPRS PROTOCOL STACK** (Simplified)
  - **Air Interface (Um)**:
    - Application → IP/X.25
    - SNDCP (Subnetwork Dependent Convergence Protocol)
    - LLC (Logical Link Control) – Reliable link
    - RLC/MAC → Radio Link Control / Medium Access
    - Physical RF layer
  - **Key Protocol**: **GTP** (GPRS Tunneling Protocol) – Tunnels user packets between SGSN & GGSN.

---

### **6. PDP CONTEXT** (The “Session” in GPRS)
  - **Def**: Logical connection between MS and GGSN (like a virtual tunnel).
  - **Contains**:
    - IP address of mobile
    - APN (Access Point Name – e.g., “internet”, “mms.vodafone.in”)
    - QoS profile
  - **Activation Steps** (Mnemonic: **A-R-A**)
    1. MS sends **Activate PDP Context Request** (with APN).
    2. SGSN → DNS → Finds GGSN.
    3. GGSN assigns IP → **Accept** → Tunnel created.
  - **Mnemonic**: PDP = **P**acket **D**ata **P**rotocol Context (your internet login).

---

### **7. MOBILE CLASSES** (How many time-slots)
  - **Class A**: Voice + data simultaneously (rare).
  - **Class B**: Voice OR data (can monitor both, switch).
  - **Class C**: Data only.
  - **Coding Schemes** (Speed vs Reliability):
    - CS-1 (9.05 kbps) → Best coverage.
    - CS-4 (21.4 kbps) → Best speed, needs good signal.

---

### **MINDMAP SKETCH** (Draw this!)
```
          Internet
             ↑ Gi
           GGSN ←─────── APN + IP assign
             ↑ Gn/Gp (GTP tunnel)
           SGSN ←─────── Mobility + Auth
             ↑ Gb
    BSC/PCU ← BTS ← Mobile (PDP Context)
```
