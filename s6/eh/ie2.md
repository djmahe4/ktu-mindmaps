# IE 2

Here are the exact **3-mark answers** for the three topics you requested. These are concise, exam-ready responses optimized for full marks (typically 1 mark for definition/explanation + 1 mark for key details/examples + 1 mark for extra point like prevention or steps).
## 3 marks
### 1. Functions of IDS (3 marks)

**Answer**:  
An Intrusion Detection System (IDS) is a security tool that monitors network or host activity to detect malicious actions or policy violations.  
Its main functions are:  
- Monitor network/host activity for suspicious behavior.  
- Recognize attack patterns and anomalies.  
- Assess file/system integrity and audit configurations.  
- Perform statistical analysis and generate alerts.  
- Manage audit trails/logs for forensic analysis.  

(Write any 4–5 functions; examiners often expect monitoring, pattern recognition, integrity assessment, statistical analysis, and alerting/audit management.)

### 2. SQL Injection (3 marks)

**Answer**:  
SQL Injection (SQLi) is a code injection attack where an attacker inserts malicious SQL statements into input fields to manipulate or bypass the backend database query.  
Example: Entering `105 OR 1=1 --` in a login field changes the query to `SELECT * FROM users WHERE id=105 OR 1=1 --`, making it always true and dumping all records.  
Prevention: Use prepared statements/parameterized queries, input validation & sanitization, and enforce least privilege on database accounts.

### 3. Network Hacking (3 marks)

**Answer**:  
Network hacking is the unauthorized process of identifying and exploiting vulnerabilities in a computer network to gain access, steal data, or disrupt services.  
It typically follows 5 phases:  
1. Reconnaissance (gather information).  
2. Scanning (probe for open ports/services).  
3. Enumeration (extract accounts/shares).  
4. Exploitation (gain access).  
5. Post-exploitation (maintain access/cover tracks).  

## 7 marks

### 1. Malware Attacks & Types of Spoofing Attacks (7 marks)

**Definition & Overview**  
Malware (malicious software) is any program designed to harm, exploit, or gain unauthorized access to systems, data, or networks. Spoofing attacks involve impersonating a legitimate entity to deceive victims or systems.

**Detailed Types of Malware**  
1. **Virus** — Attaches to legitimate files/programs; spreads only when the infected file executes. Requires user interaction. Example: File infector viruses like CIH/Chernobyl.  
2. **Worm** — Self-replicates and spreads independently across networks without needing a host file or user action. Exploits vulnerabilities (e.g., EternalBlue in WannaCry).  
3. **Trojan** — Disguised as useful software; creates backdoors for remote control or data theft. Example: Zeus banking Trojan.  
4. **Ransomware** — Encrypts files/data and demands payment (usually cryptocurrency). Example: Locky, Ryuk.  
5. **Spyware/Adware** — Secretly monitors activity or displays unwanted ads (often bundled).

**Types of Spoofing Attacks** (Link to network-level deception)  
1. **ARP Spoofing** — Poisons ARP cache → attacker becomes MitM on local network.  
2. **DNS Spoofing** (Cache Poisoning) — Returns fake IP for domain → redirects to malicious site.  
3. **IP Spoofing** — Forges source IP → used in DoS (e.g., reflection attacks).  
4. **MAC Spoofing** — Alters MAC address → bypasses MAC-based access controls.  
5. **Email/Phone Spoofing** — Fakes sender ID → common in phishing.

**Impacts** — Data theft, financial loss, ransomware payments, lateral movement in networks.  

**Prevention**  
- Updated antivirus/EDR with behavior analysis.  
- Network segmentation & ARP/DNS monitoring (e.g., DHCP snooping, DNSSEC).  
- User awareness training, least privilege, patch management.

**Exam Tip**: Use bullet points for types; draw simple spoofing flow if time permits.

### 2. Network Hacking (7 marks – very high yield)

**Definition**  
Network hacking refers to unauthorized attempts to identify, exploit, and gain access to or disrupt network infrastructure, devices, protocols, and services.

**Phases/Methodology (Detailed 5 steps – expand each)**  
1. **Reconnaissance** (Passive/Active) — Gather intel (WHOIS, Google dorking, Shodan, social media). Passive avoids direct contact.  
2. **Scanning** — Probe for live hosts, open ports, services, OS versions (Nmap, Nessus).  
3. **Enumeration** — Extract usernames, shares, groups, policies (NetBIOS, SNMP, LDAP queries).  
4. **Exploitation / Gaining Access** — Exploit vulnerabilities (Metasploit, custom exploits) → gain shell/root.  
5. **Post-Exploitation** — Maintain access (backdoors, pivoting), escalate privileges, exfiltrate data, cover tracks (log deletion).

**Common Techniques**  
- Spoofing, DoS (SYN flood, Smurf), session hijacking, MitM.  
- Tools: Wireshark (sniffing), Ettercap (ARP poisoning).

**Impacts** — Unauthorized access, data breaches, ransomware deployment, service disruption.

**Prevention (Defense side – link to Module 4)**  
- Firewalls, IDS/IPS, network segmentation.  
- Disable unnecessary services, strong authentication (MFA).  
- Regular vulnerability scanning & patching.

**Exam Tip**: List the 5 steps numbered; explain each with 1–2 tools/examples.

### 3. Buffer Overflow Attack (7 marks)

**Definition & Mechanism**  
Buffer overflow occurs when a program writes more data to a fixed-size buffer than it can hold, overwriting adjacent memory (e.g., return addresses, function pointers).

**Types**  
- **Stack-based** (most common) — Overwrites return address → redirects execution to attacker code (shellcode).  
- **Heap-based** — Targets dynamic memory; harder but possible.  
- **Integer overflow** — Related; miscalculates buffer sizes.

**Exploitation Steps**  
1. Identify vulnerable function (e.g., strcpy, gets in C).  
2. Craft input exceeding buffer → overwrite return address with attacker-controlled address.  
3. Inject shellcode → gain shell.

**Impacts**  
- Denial of service (crash).  
- Arbitrary code execution → root shell, backdoor installation.

**Prevention Techniques**  
- Use safe functions (strncpy, fgets).  
- Compiler protections: Stack canaries, ASLR (randomizes addresses), DEP/NX bit (prevents code execution in data areas).  
- Modern languages (Rust, Go) with built-in bounds checking.  
- Input validation & fuzzing during development.

**Exam Tip**: Explain stack layout briefly (buffer → saved registers → return address).

### 4. Privacy Attacks (7 marks)

**Definition**  
Privacy attacks aim to compromise individuals’ or organizations’ private information through unauthorized collection, inference, or disclosure.

**Key Types & Examples**  
- **Data Exfiltration** — Direct theft (SQLi, XSS, malware).  
- **Inference Attacks** — Deduce sensitive info from non-sensitive data (e.g., Netflix prize dataset re-identification).  
- **Profiling** — Build detailed user profiles (tracking cookies, behavioral analysis).  
- **Specific Techniques** — Phishing, MitM, Shoulder surfing, Doxxing, Side-channel attacks.

**Impacts**  
- Identity theft, financial fraud, blackmail, targeted phishing, reputational damage.

**Prevention**  
- Encryption (TLS, data-at-rest).  
- Anonymization/pseudonymization.  
- Privacy-by-design, consent mechanisms (GDPR principles).  
- DLP tools, access controls.

### 5. Web Services – REST, WSDL, SAML (7 marks)

**Overview**  
Web services enable interoperable machine-to-machine communication.

**Detailed Components**  
- **WSDL (Web Services Description Language)** — XML document describing SOAP service: operations, messages, endpoints. Acts as contract/manual.  
- **REST (Representational State Transfer)** — Architectural style using HTTP methods (GET/POST/PUT/DELETE), stateless, resource-oriented (usually JSON/XML). Lightweight, scalable vs. SOAP.  
- **SAML (Security Assertion Markup Language)** — XML-based framework for authentication & authorization (SSO). Identity Provider (IdP) issues assertions → Service Provider trusts & grants access.

**Comparison SOAP vs REST**  
- SOAP: Structured, XML, built-in security (WS-Security), stateful possible.  
- REST: Simpler, faster, uses standard HTTP, no strict standard.

**Security Aspects** — SAML prevents session hijacking in SSO; REST often uses OAuth/JWT.

**Exam Tip**: Draw simple comparison table; explain SAML SSO flow.

### 6. Architectural Strategies for Computer Fraud Prevention (7 marks)

**Main Strategy** — **Multitier (N-tier) Architecture** (especially 3-tier).

**Explanation**  
- **Presentation Tier** (UI/web server) — Handles user input/output.  
- **Application/Business Logic Tier** — Processes requests, applies rules/validation.  
- **Data Tier** (Database) — Stores/retrieves data.

**How it Prevents Fraud**  
- Segregates layers → attacker compromising UI (e.g., via XSS/SQLi) cannot directly query/manipulate database.  
- Each tier has separate security controls: input sanitization (app tier), encryption (data tier), firewalls between tiers.  
- Least privilege: DB accounts have minimal rights.  
- Reduces attack surface; limits lateral movement.

**Additional Strategies**  
- Input validation & output encoding.  
- Logging & monitoring.  
- WAF, rate limiting.

**Exam Tip**: Draw 3-tier diagram + arrows showing data flow & controls at each layer.

### 7. NIDS and HIDS (7 marks – difference + strengths/weaknesses)

**NIDS (Network-based IDS)**  
- Monitors network traffic (raw packets).  
- Deployed on network segments/SPAN ports.  
- Detects: DoS, port scans, protocol anomalies.  
- **Weakness**: Blind to encrypted traffic; cannot see host-level changes.

**HIDS (Host-based IDS)**  
- Installed on individual hosts/servers.  
- Monitors logs, file integrity, system calls.  
- Detects: Rootkits, file changes, insider threats.  
- **Strength**: Sees decrypted data & host-specific events.

**Comparison Table** (write in exam)

| Aspect              | NIDS                          | HIDS                          |
|---------------------|-------------------------------|-------------------------------|
| Scope               | Entire network segment        | Single host                   |
| Data Source         | Packets                       | Logs, files, processes        |
| Encryption          | Cannot inspect                | Can (after decryption)        |
| Resource Usage      | Centralized                   | Per-host (higher overhead)    |
| Best For            | Broad attacks                 | Detailed, persistent threats  |

**Exam Tip**: Always include table + 2–3 examples each.

### 8. Pentesting Steps (Module 4 – 7 marks)

**5 Phases (Detailed)**  
1. **Reconnaissance** — Passive (OSINT) & active info gathering.  
2. **Scanning** — Port/service discovery (Nmap), vulnerability scanning (Nessus/OpenVAS).  
3. **Gaining Access / Enumeration & Exploitation** — Exploit found vulnerabilities (Metasploit).  
4. **Maintaining Access** — Install backdoors, create accounts.  
5. **Analysis & Reporting** — Document findings, risk ratings, remediation advice.

**Key Difference from Malicious Hacking** — Authorized, scoped, ends with report.

**Exam Tip**: Number phases; explain tools/examples for each.

### Quick Prioritization for 7-mark Questions

1. Network Hacking (5 steps detailed)  
2. Malware + Spoofing types  
3. Buffer Overflow (mechanism + prevention)  
4. Multitier fraud prevention (diagram + explanation)  
5. Pentesting steps  
6. NIDS vs HIDS  
7. Web services (WSDL/REST/SAML)
