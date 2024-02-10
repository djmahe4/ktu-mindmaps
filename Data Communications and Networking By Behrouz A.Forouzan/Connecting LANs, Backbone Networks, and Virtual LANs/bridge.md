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

Sure, let's break it down:

A **Transparent Bridge** is a type of bridge that operates in a way that is invisible to the rest of the network. The devices connected by the bridge don't need to know about the bridge's existence. Even if the bridge is added or removed, the devices don't need to be reconfigured.

A system with transparent bridges needs to meet three key criteria according to the IEEE 802.1d specification:

1. **Frame Forwarding**: The bridge must be able to forward data frames from one device to another.

2. **Automatic Learning**: The bridge automatically builds a forwarding table by observing the movement of frames in the network. This helps the bridge know where to forward the data.

3. **Loop Prevention**: The bridge must prevent data loops, which are situations where data keeps circulating in the network without reaching its intended destination.

In essence, a transparent bridge helps to extend a network by connecting devices, learning the network structure, forwarding data correctly, and preventing data loops, all while being invisible to the devices it connects.


