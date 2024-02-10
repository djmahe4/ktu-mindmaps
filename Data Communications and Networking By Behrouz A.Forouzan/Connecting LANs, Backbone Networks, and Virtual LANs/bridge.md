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
