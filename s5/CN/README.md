# Ethernet Frame
```mermaid
graph TD
    A[Ethernet Frame]
    A --> B[Preamble - 7 bytes]
    A --> C[Start Frame Delimiter - 1 byte]
    A --> D[Destination MAC Address - 6 bytes]
    A --> E[Source MAC Address - 6 bytes]
    A --> F[EtherType or Length - 2 bytes]
    A --> G[Payload or Data - 46 to 1500 bytes]
    A --> H[Frame Check Sequence - 4 bytes]
```
# Mod 3
```mermaid
mindmap
  root((Module 3: Network Layer))
    A(Routing Algorithms)
      A1[Link State Routing - LSR]
        A1.1(Dijkstra Algorithm Steps)
        A1.2(LSP Construction and Flooding)
      A2[Distance Vector Routing - DVR]
        A2.1(Count-to-Infinity Problem)
          A2.1.1(Split Horizon / Poisoned Reverse)
        A2.2(Bellman-Ford Equation - Numerical)
        A2.3(Optimality Principle - Sink Tree)
      A3[Classification]
        A3.1(Static vs Dynamic)
        A3.2(Adaptive vs Non-Adaptive)
    B(Congestion Control and QoS)
      B1[Congestion Control]
        B1.1(Open-Loop Prevention)
          B1.1.1(Leaky Bucket - Traffic Shaping)
          B1.1.2(Token Bucket)
          B1.1.3(Load Shedding)
        B1.2(Closed-Loop Feedback)
          B1.2.1(Backpressure)
          B1.2.2(Choke Packets)
          B1.2.3(Explicit Congestion Notification - ECN)
        B1.3(Flooding)
          B1.3.1(Applications)
          B1.3.2(Sequence Numbers / Hop Limit)
      B2[Quality of Service - QoS]
        B2.1(QoS Parameters)
          B2.1.1(Bandwidth, Delay, Jitter, Loss)
        B2.2(Techniques)
          B2.2.1(Scheduling - Fair Queuing / WFQ)
          B2.2.2(Traffic Shaping - Leaky or Token Bucket)
    C(Network Structure)
      C1[Subnet Types Comparison]
        C1.1(Datagram Subnet)
        C1.2(Virtual Circuit Subnet)
      C2[Other Routing - Low Priority]
        C2.1(Multicast Routing)
        C2.2(Mobile Host Routing)
```
## congestion control 
Here is the explanation of the Congestion Control concepts from the notes, presented in a clear, comparative table format.
🚦 Congestion Control Mechanisms
| Category | Mechanism | Goal / When Applied | Key Action |
|---|---|---|---|
| Open-Loop | Open-Loop Control | Prevent congestion before it happens. | Policies are set beforehand; no feedback used. |
| Open-Loop | Retransmission Policy | Handle lost or corrupted packets. | If a sender suspects a loss, the packet is sent again. |
| Open-Loop | Acknowledgement Policy | Confirm successful data receipt. | Receiver informs the sender which packets arrived (often delaying to send one ACK for multiple packets). |
| Open-Loop | Discarding Policy | Shed load during overload (used by intermediate routers). | Congested routers drop packets, forcing senders to slow down. |
| Open-Loop | Admission Policy | Ensure the network can handle new traffic. | A node must reserve resources before sending data. |
| Closed-Loop | Closed-Loop Control | Alleviate congestion after it has been detected. | Uses various signaling methods to fix current issues. |
| Closed-Loop | Backpressure | For very slow networks; local congestion relief. | Warning moves upstream from the congested node only to its immediate neighbor. |
| Closed-Loop | Choke Packet | Directly signal the source to slow down. | A packet is sent back to the original sender to inform them of congestion. |
| Closed-Loop | Implicit Signaling | Infer congestion based on poor performance. | Sender observes signs (e.g., long delays, dropped packets) and infers congestion. |
| Closed-Loop | Explicit Signaling | Directly signal congestion status. | A specific bit is marked in the data packet to notify the source or destination about congestion. |
Would you like a brief analogy for any of these specific mechanisms?
