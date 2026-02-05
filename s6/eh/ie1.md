## **Part 1: 3-Mark Questions (Short & Precise)**

**1. CIA (Confidentiality, Integrity, Availability)**
The CIA triad is the standard model for information security:
*   **Confidentiality:** Ensures only authorized people can access data (e.g., encryption, classification).
*   **Integrity:** Ensures data is not modified without authorization; it remains whole and uncorrupted.
*   **Availability:** Ensures assets and systems are available to authorized users whenever needed (e.g., preventing power outages or hardware failures).

**2. Nmap & Traceroute**
*   **Nmap (Network Mapper):** A port scanner used to find open ports, discover assets, detect host services, and configure firewalls.
*   **Traceroute:** A tool that reveals the path IP packets travel between systems. It works by sending UDP packets with increasing **TTL (Time to Live)** values; each router decrements the TTL and sends back a "TTL exceeded" message.

**3. Ethical Hacking Process (5 Steps)**
Ethical hackers follow a 5-step methodology to secure an organization:
1.  **Assessment:** Performing hacking and penetration tests.
2.  **Policy Development:** Creating security policies based on critical assets.
3.  **Implementation:** Building technical and managerial controls.
4.  **Training:** Educating employees on security policies and tools.
5.  **Audit:** Periodic reviews of security controls (e.g., HIPAA compliance).

---

### **Part 2: 7-Mark Questions (Detailed & Structured)**

**1. Attacker’s Process (The 6 Phases)**
Attackers use a systematic 6-phase approach to gain unauthorized access:
1.  **Performing Reconnaissance:** Gathering preliminary intelligence on the target (Footprinting).
2.  **Scanning and Enumeration:** Using technical tools (Nmap, vulnerability scanners) to find open ports and user account info.
3.  **Gaining Access:** Exploiting vulnerabilities to gain control of the OS, applications, or network.
4.  **Escalation of Privilege:** Leveraging bugs to gain higher-level access (e.g., admin rights) than intended.
5.  **Maintaining Access:** Using Rootkits or backdoors to stay in the system stealthily.
6.  **Covering Tracks:** Deleting logs and evidence of the intrusion to avoid detection.

**2. Reconnaissance – Active & Passive**
Reconnaissance is the first pre-attack phase used to gather information.
*   **Passive Reconnaissance:** Acquiring information without directly interacting with the target. Examples: Searching public records, news releases, or social media.
*   **Active Reconnaissance:** Involves direct interaction with the target system. Examples: Making telephone calls to the help desk (Social Engineering) or using tools that touch the target network.

**3. Security Testing – Focus Areas, Advantages, and Goals**
*   **Goals:** Identify threats, measure potential vulnerabilities, detect security risks, and help developers fix code.
*   **Focus Areas:** System Software Security, Authentication/Authorization, Network/Infrastructure, Database Security, and Application Security.
*   **Advantages:** Identifies vulnerabilities before attackers do, ensures compliance with standards (HIPAA, PCI-DSS), reduces risk by fixing issues before deployment, and improves incident response.

**4. Penetration Testing – 6 Phases (Attacker's methodology applied)**
(See **Question 1** above. For a 7-mark answer, emphasize that this is a *simulated* attack by a malicious hacker to find weaknesses.)

**5. Footprinting**
Footprinting is creating a blueprint of an organization's network and systems using non-intrusive methods.
*   **Information Gathered:** Domain names, Network blocks, IP addresses, System architecture, IDS, and Contact addresses/Phone numbers.
*   **Tools Used:** Whois (domain registration info), Nslookup (querying DNS), and Google (OSINT gathering).
*   **Advantages:** Allows hackers to see network routes and data flows to identify which attack is most "handy."

**6. Identification of Open Ports (Nmap & Tools)**
Finding open ports helps identify active services and entry points:
*   **Nmap:** The primary tool for engineers to find open ports and discover assets.
*   **Netstat:** A command-line program (e.g., `netstat -a`) that identifies open ports on your own local computer.
*   **Wireshark:** A network sniffing tool that detects malicious activity and open ports in live traffic.

**7. Ethical and Legality**
Ethical hacking must be conducted legally and professionally:
*   **Authorization:** Must have a signed contract and express permission before starting.
*   **NDA (Nondisclosure Agreement):** Must protect the client’s confidential information.
*   **Limits:** Stay within agreed-upon limits (e.g., don't run DoS attacks unless specifically authorized).
*   **"Do No Harm":** The goal is to protect the system, not cause loss of revenue or goodwill.

**8. Analyze Active Mode / Locate Network Range**
*   **Locating Network Range:** Determining the range of IP addresses and subnet masks. Sources include **ARIN** (American Registry of Internet Numbers) and **Traceroute**.
*   **Identifying Active Machines:** Once the range is known, identify active nodes using:
    *   **Ping:** Sends ICMP Echo Requests to see if a machine responds.
    *   **War Dialers:** Scanning telephone numbers for modems (legacy).
    *   **Port Scanning:** Part of the larger process to find "live" systems.
---

### **9. All 8 Legal/International Standards (For a 7-Mark Answer)**
To get full marks, you should list all eight from your PDF:
1.  **PCI-DSS:** For debit/credit card data security.
2.  **ISO/IEC 27001:2013:** For Information Security Management Systems.
3.  **HIPAA:** For protecting healthcare and patient information.
4.  **FISMA:** For securing federal (government) information resources.
5.  **Cyber Security Enhancement Act & SPY ACT:** Mandates life sentences for reckless endangerment; prohibits unauthorized remote control and keylogging.
6.  **Federal Managers Financial Integrity Act (FMFIA):** Ensures financial assets are protected against waste, loss, or misappropriation.
7.  **Freedom of Information Act (FOIA):** Makes organization info public; used for legal reconnaissance.
8.  **Privacy Act 1974:** Prevents government agencies from sharing personal info without consent.


### **10 The Ethical Hacker’s Process (Management & Security Framework)**

The ethical hacker plays a key role in the security process by moving beyond just "hacking" and into securing the infrastructure. This methodology is broken down into these five key steps:

**1. Assessment**
*   This is the initial phase where the actual technical work happens.
*   It includes performing **Ethical Hacking**, **Penetration Testing**, and other hands-on security tests to identify the organization's strengths and weaknesses.

**2. Policy Development**
*   Once the assessment is done, the focus shifts to management.
*   Security policies are developed based on the organization's specific goals and mission.
*   The primary focus is placed on protecting the organization’s **critical assets** identified during the assessment.

**3. Implementation**
*   In this phase, the actual "defenses" are built.
*   The ethical hacker helps in building **technical, operational, and managerial controls**.
*   This includes configuring hardware (like firewalls) and software to secure key assets and data.

**4. Training**
*   Since humans are often the weakest link, employees must be educated.
*   Staff are trained on how to follow the newly developed security policies.
*   They are also taught how to configure and interact with key security controls, such as **Intrusion Detection Systems (IDS)** and firewalls.

**5. Audit**
*   Security is not a one-time event; it requires periodic reviews.
*   Auditing involves checking the controls that were put in place to ensure they are providing good security.
*   Certain regulations (like **HIPAA**) specifically require that these audits be done **yearly**.

---

**Key Distinction for the Exam:**
*   **The Attacker's Process (Section 1.6):** The 6 technical steps (Recon, Scanning, Access, etc.).
*   **The Ethical Hacker's Process (Section 1.7):** The 5 management steps (Assessment, Policy, Implementation, Training, Audit) used to "do no harm" and actually protect the company.


### **Part 1: 3-Mark Questions**

| Topic | PDF Module | Page Number |
| :--- | :--- | :--- |
| **1. CIA (Confidentiality, Integrity, Availability)** | Module 1 | Page 1 |
| **2. Nmap (Network Mapper)** | Module 2 | Page 7 |
| **3. Traceroute (Technical process/TTL)** | Module 2 | Pages 3–4 |
| **4. Ethical Hacking Process (5 Steps)** | Module 1 | Page 16 |

---

### **Part 2: 7-Mark Questions**

| Topic | PDF Module | Page Number |
| :--- | :--- | :--- |
| **1. Attacker’s Process (The 6 Technical Phases)** | Module 1 | Pages 12–15 |
| **2. Reconnaissance (Active vs. Passive)** | Module 1 | Page 13 |
| **3. Security Testing (Goals, Focus Areas, Advantages)** | Module 1 | Pages 2–4 |
| **4. Penetration Testing (Definition and Phase 3)** | Module 1 | Page 3 |
| **5. Footprinting (Definition, Tools, Advantages)** | Module 2 | Pages 1–2 |
| **6. Identification of Open Ports (Nmap, Netstat, Wireshark)** | Module 2 | Page 7 |
| **7. Ethical and Legality (How to be ethical/Legal rules)** | Module 1 | Pages 9–10 |
| **8. Locate Network Range (ARIN & Traceroute)** | Module 2 | Page 3 |
| **9. Identify Active Machines (Ping, War Dialing, etc.)** | Module 2 | Page 5 |
| **10. International Standards & Laws (All 8 Laws)** | Module 1 | Pages 11–12 |
| **11. Ethical Hacker's Process (5 Management Steps)** | Module 1 | Page 16 |
