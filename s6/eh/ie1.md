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

**9. International Standards (Module 1)**
Organizations must follow specific security standards:
1.  **PCI-DSS:** For organizations handling credit/debit card information.
2.  **ISO/IEC 27001:** Requirements for an Information Security Management System (ISMS).
3.  **HIPAA:** Protects the privacy of health information.
4.  **FISMA:** Framework for securing federal (government) information and assets.
5.  **Cyber Security Enhancement Act:** Mandates life sentences for hackers who "recklessly" endanger lives.
6.  **SPY ACT:** Prohibits unauthorized remote control of computers and keystroke logging.
   
**10. Ethical Hacking Process (Managerial/Policy side)**

### **1. Performing Reconnaissance (Footprinting)**
This is the first pre-attack phase. It is a systematic attempt to locate, gather, and record information about the target.
*   **Goal:** To create a blueprint or map of an organization’s network and systems.
*   **Passive Reconnaissance:** Gathering information without direct interaction (e.g., searching public records, news releases, or social media).
*   **Active Reconnaissance:** Directly interacting with the target (e.g., making phone calls to the help desk or technical department).
*   **Information Gathered:** Domain names, IP addresses, network blocks, and system architecture.

### **2. Scanning and Enumeration**
In this phase, the hacker uses technical tools to gather more detailed intelligence on the target's systems and applications.
*   **Scanning:** The active step of attempting to connect to systems to elicit a response. Tools like **Nmap** are used to map open ports.
*   **Enumeration:** Gathering in-depth information such as open shares, user account information, and software versions (banner grabbing).
*   **Objective:** To identify the "live" systems and specific vulnerabilities that can be exploited.

### **3. Gaining Access**
This is one of the most important steps. The attacker moves from simply probing the network to actually attacking it.
*   **Levels of Access:** Access can be gained at the Operating System (OS) level, Application level, or Network level.
*   **Methods:** Finding vulnerabilities in web server software, exploiting open wireless access points, or using captured credentials.

### **4. Escalation of Privilege**
Once initial access is gained, the hacker tries to move from a standard user to a higher security context (Administrative or Root access).
*   **Goal:** To obtain complete control over the system.
*   **Techniques:** Leveraging bugs or vulnerabilities in applications or the OS to bypass protections.
*   **Examples:** Password cracking, buffer overflows, and session hijacking.

### **5. Maintaining Access**
The attacker tries to stay in the system as long as possible to gather information while remaining stealthy to avoid detection.
*   **Stealth:** The hacker must remain hidden from administrators.
*   **Tools:** Using **Rootkits**, which are sets of tools that mask the hacker's presence and activity.
*   **Activity:** Uploading, downloading, or manipulating data and using the owned system to launch further attacks on other networks.

### **6. Covering Tracks and Placing Backdoors**
The final phase involves hiding the malicious activity and ensuring future access.
*   **Covering Tracks:** Overwriting server, system, and application logs to remove evidence that might lead to prosecution. 
*   **Hiding Files:** Using techniques like hidden directories or Alternate Data Streams (ADS).
*   **Backdoors:** Creating hidden entry points that allow the hacker to re-enter the computer at will in the future.
