```
Bridge
|
+---> Filtering and Difference from Repeater
|     |
|     +---> Operates at data link layer (Layer 2)
|     +---> Examines incoming traffic
|     +---> Decides whether to filter or forward it
|
+---> Transparent Bridges
|     |
|     +---> Invisible to other devices on the network
|     +---> Does not reconfigure the network on addition or deletion of any station
|
+---> Learning
|     |
|     +---> Automatically maintains and updates a routing table
|     +---> Learns the location of nodes and associated ports
|
+---> Loop Problem
|     |
|     +---> Occurs when there is more than one Layer 2 path between two endpoints
|     +---> Solved by allowing physical loops but creating a loop-free logical topology
|
+---> Spanning Tree
|     |
|     +---> Network protocol that ensures a loop-free topology
|     +---> Creates a spanning tree by disabling all links that form a loop
|
+---> Dynamic Algorithm
|     |
|     +---> Used to find the best path for data to travel over a network
|     +---> Adapts to changing network conditions to optimize data transmission
|
+---> Source Routing Bridges
|     |
|     +---> Decide the route between two hosts
|     +---> The frame’s entire route is embedded with the data frames by the source station
|
+---> Bridges Connecting Different LANs
      |
      +---> Connect multiple LANs together with a larger Local Area Network (LAN)
      +---> Operate at the data link layer and transmit data as data frames
```
A **bridge** and a **repeater** are both network devices, but they function differently. 

- A **repeater** simply amplifies the network signal to extend its range.

- A **bridge**, on the other hand, has a more complex role. It can check the destination address of a data frame and decide whether to forward it or drop it. This is known as **filtering**. 

For example, consider two Local Area Networks (LANs) connected by a bridge. If a data frame arrives at the bridge destined for a certain station, the bridge checks its table to find out which port the frame should leave from. If the frame arrived at the same port it's supposed to leave from, the bridge drops the frame because there's no need to forward it. But if the frame arrives at a different port, the bridge forwards the frame to the correct port. 

In this way, a bridge can control traffic between different parts of a network, ensuring that data gets where it needs to go efficiently. And importantly, while doing all this, a bridge does not change the physical (MAC) addresses in the frame.
![image](https://github.com/djmahe4/ktu-mindmaps/assets/137691824/b3db63b6-edd0-4326-b079-8488575b32cb)

A **Transparent Bridge** is a type of bridge that operates in a way that is invisible to the rest of the network. The devices connected by the bridge don't need to know about the bridge's existence. Even if the bridge is added or removed, the devices don't need to be reconfigured.

A system with transparent bridges needs to meet three key criteria according to the IEEE 802.1d specification:

1. **Frame Forwarding**: The bridge must be able to forward data frames from one device to another.

2. **Automatic Learning**: The bridge automatically builds a forwarding table by observing the movement of frames in the network. This helps the bridge know where to forward the data.

3. **Loop Prevention**: The bridge must prevent data loops, which are situations where data keeps circulating in the network without reaching its intended destination.

In essence, a transparent bridge helps to extend a network by connecting devices, learning the network structure, forwarding data correctly, and preventing data loops, all while being invisible to the devices it connects.

**Learning**
* The earliest bridges had forwarding tables that were static. 
* The systems administrator would manually enter each table entry during bridge setup. 
* Although the process was simple, it was not practical. If a station was added or deleted, the table had to
be modified manually. 
* The same was true if a station's MAC address changed, which is not a rare event. 
* For example, putting in a new network card means a new MAC address.
* A better solution to the static table is a dynamic table that maps addresses to ports automatically.
* To make a table dynamic, we need a bridge that gradually learns from the frame movements. 
* To do this, the bridge inspects both the destination and the source addresses. 
* The destination address is used for the forwarding decision (table lookup); the source address is used for adding entries to the table and for updating purposes
```
1. A -> D
   Bridge: No entry for A or D
   Action: Floods network, learns A is on port 1
   Table: A - port 1

2. E -> A
   Bridge: Has entry for A
   Action: Forwards frame to port 1, learns E is on port 2
   Table: A - port 1, E - port 2

3. B -> C
   Bridge: No entry for B or C
   Action: Floods network, learns B is on port 3
   Table: A - port 1, E - port 2, B - port 3

4. Continues learning as it forwards frames
```
![image](https://github.com/djmahe4/ktu-mindmaps/assets/137691824/203b15fd-59d5-43b7-acf5-b5c98ec20367)

**Loop Problem** 
Transparent bridges work fine as long as there are no redundant
bridges in the system. Systems administrators, however, like to have redundant bridges
(more than one bridge between a pair of LANs) to make the system more reliable. If a
bridge fails, another bridge takes over until the failed one is repaired or replaced.
Redundancy can create loops in the system, which is very undesirable.
```
LAN 1 <----> Bridge 1 <----> LAN 2
  ^            ^  ^            ^
  |            |  |            |
  |            |  |            |
  v            v  v            v
Station A   Frame A->D    Station D
```

1. **Station A sends a frame to Station D**. Both bridges have empty tables. They forward the frame and update their tables with source address A.

```
Bridge 1 Table: A - LAN 1
Bridge 2 Table: A - LAN 1
```

2. **Two copies of the frame are now on LAN 2**. Bridge 1's copy is received by Bridge 2, and Bridge 2's copy is received by Bridge 1. Both bridges flood the network as they don't have information about destination D. Their tables are updated, but still no information for D.

```
Bridge 1 Table: A - LAN 1, D - LAN 2
Bridge 2 Table: A - LAN 1, D - LAN 2
```

3. **Two copies of the frame are now back on LAN 1**. Step 2 is repeated, and both copies flood the network again.

4. **The process continues indefinitely**. Each bridge regenerates fresh copies of the frames in each iteration.

To solve this looping problem, the IEEE specification requires that bridges use the Spanning Tree Algorithm to create a loopless topology. This algorithm ensures that there is only one active path between any two network nodes, which prevents loops in the network.

![image](https://github.com/djmahe4/ktu-mindmaps/assets/137691824/ec873f8d-849e-49bc-b3cf-5b7da9b2f4d2)

**Spanning Tree** 
1. **What is a Spanning Tree?**
   A spanning tree is a subset of a graph, which is a tree that includes all the vertices (or nodes) of the graph. In other words, it's a simplified version of the original network, where you can reach any point from any other point, but only along one unique path. This means there are no loops in a spanning tree.

2. **Why do we need a Spanning Tree?**
   In a Local Area Network (LAN), we often have redundant paths for reliability. However, these can create loops, causing broadcast storms and other issues. A spanning tree allows us to keep the network connected while avoiding these loops.

3. **How is a Spanning Tree created?**
   - Mentioned Below - 

4. **What is a Minimum Spanning Tree (MST)?**
   An MST is a spanning tree where the total weight (or cost) of all the edges is as small as possible. This is particularly useful when the edges have different weights or costs associated with them.

5. **Real-World Applications**
   Spanning trees are used in various real-world applications, such as computer network routing protocols, telecommunication networks, and more.

![image](https://github.com/djmahe4/ktu-mindmaps/assets/137691824/1e1a9954-45f5-4b2a-b26b-2dfac3043abd)
In the graph representation, both LANs and bridges are represented as nodes. The connecting arcs show the connection of a LAN to a bridge and vice versa. Each arc has a cost assigned to it, which could represent the path with minimum hops (nodes), the path with minimum delay, or the path with maximum bandwidth.

The process to find the spanning tree involves three steps:
1. Every bridge has a built-in ID (normally the serial number, which is unique). Each bridge broadcasts this ID so that all bridges know which one has the smallest ID. The bridge with the smallest ID is selected as the root bridge (root of the tree). We assume that bridge B1 has the smallest ID. It is, therefore, selected as the root bridge.
2. The algorithm tries to find the shortest path (a path with the shortest cost) from the root bridge to every other bridge or LAN. The shortest path can be found by examining the total cost from the root bridge to the destination.
3. The combination of the shortest paths creates the shortest tree. Based on the spanning tree, we mark the ports that are part of the spanning tree, the forwarding ports, which forward a frame that the bridge receives. We also mark those ports that are not part of the spanning tree, the blocking ports, which block the frames received by the bridge.

In the spanning tree system, there is only one single path from any LAN to any other LAN. This means there is only one single path from one LAN to any other LAN. No loops are created. This is the basic concept of a spanning tree in a bridged LAN.

**Dynamic algorithm** 
```
Dynamic Algorithm
|
|-- Spanning Tree Algorithm
|   |
|   |-- Not Manual: Each bridge is equipped with a software package
|   |
|   |-- Dynamic Process: The bridges send special messages (BPDUs) to each other
|   |
|   |-- Updates: The spanning tree is updated when there is a change in the system
|       |
|       |-- Failure of a Bridge
|       |
|       |-- Addition or Deletion of Bridges
```

In this context, the dynamic algorithm refers to the spanning tree algorithm used in network bridges. This algorithm doesn't require manual entries. Instead, each bridge is equipped with a software package that carries out this process dynamically. The bridges communicate with each other by sending special messages known as Bridge Protocol Data Units (BPDUs). These messages are used to update the spanning tree, which is the optimal path selection in the network. The spanning tree is updated whenever there is a change in the system, such as a failure of a bridge or an addition or deletion of bridges. This ensures that the network remains efficient and loop-free even when changes occur. 

![image](https://github.com/djmahe4/ktu-mindmaps/assets/137691824/29d29a87-9e9e-405b-be2a-dd095b47d86a)

**Source Routing Bridges** 
```
Source Routing Bridges
|
|-- Prevent Loops: Used in a system with redundant bridges
|   |
|   |-- Transparent Bridge Duties: Filtering frames, forwarding, and blocking
|       |
|       |-- Performed By: Source station and, to some extent, the destination station
|
|-- Source Routing: A sending station defines the bridges that the frame must visit
|   |
|   |-- Frame Contents: Source and destination addresses, and addresses of all bridges to be visited
|   |
|   |-- Bridge Addresses: Obtained through the exchange of special frames with the destination prior to sending the data frame
|
|-- Design: By IEEE for use with Token Ring LANs (not very common today)
```

In this context, Source Routing Bridges are used to prevent loops in a system with redundant bridges. The duties of a transparent bridge, which include filtering frames, forwarding, and blocking, are performed by the source station and, to some extent, the destination station. In source routing, a sending station defines the bridges that the frame must visit. The addresses of these bridges are included in the frame, which means the frame contains not only the source and destination addresses, but also the addresses of all bridges to be visited. The source gets these bridge addresses through the exchange of special frames with the destination prior to sending the data frame. Source routing bridges were designed by IEEE to be used with Token Ring LANs, which are not very common today.

**Bridges Connecting Different LANs** 
```
Ethernet LAN <---- BRIDGE ----> Wireless LAN
```

The bridge connects two LANs that may use different protocols at the data link layer. However, there are several issues to consider:

1. **Frame format**: Each LAN type has its own frame format. For example, an Ethernet frame is different from a wireless LAN frame.

2. **Maximum data size**: If an incoming frame's size is too large for the destination LAN, the data must be fragmented into several frames. The data then needs to be reassembled at the destination. However, no protocol at the data link layer allows the fragmentation and reassembly of frames. This is allowed in the network layer. The bridge must therefore discard any frames too large for its system.

3. **Data rate**: Each LAN type has its own data rate. For example, compare the 10-Mbps data rate of an Ethernet with the 1-Mbps data rate of a wireless LAN. The bridge must buffer the frame to compensate for this difference.

4. **Bit order**: Each LAN type has its own strategy in the sending of bits. Some send the most significant bit in a byte first; others send the least significant bit first.

5. **Security**: Some LANs, such as wireless LANs, implement security measures in the data link layer. Other LANs, such as Ethernet, do not. Security often involves encryption. When a bridge receives a frame from a wireless LAN, it needs to decrypt the message before forwarding it to an Ethernet LAN.

6. **Multimedia support**: Some LANs support multimedia and the quality of services needed for this type of communication; others do not. 
