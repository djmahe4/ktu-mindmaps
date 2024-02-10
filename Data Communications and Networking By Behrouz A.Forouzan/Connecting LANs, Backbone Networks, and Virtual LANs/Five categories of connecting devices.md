```
Five Categories of Connecting Devices
|
|-- 1. Operate below the physical layer
|   |-- Example: Passive Hub
|
|-- 2. Operate at the physical layer
|   |-- Example: Repeater
|   |-- Example: Active Hub
|
|-- 3. Operate at the physical and data link layers
|   |-- Example: Bridge
|   |-- Example: Two-layer Switch
|
|-- 4. Operate at the physical, data link, and network layers
|   |-- Example: Router
|   |-- Example: Three-layer Switch
|
|-- 5. Operate at all five layers
    |-- Example: Gateway
```

Sure, let's go through each of them:

1. **Passive Hub**: A passive hub is a basic network device that connects multiple devices together. It does not process or regenerate signals, but simply repeats or copies the signals it receives. It's essentially a connector that connects wires coming from other devices.

2. **Repeater**: A repeater is a networking device that amplifies and regenerates the incoming signal. Its main purpose is to extend the networking distance by increasing the strength and quality of signals.
![image](https://github.com/djmahe4/ktu-mindmaps/assets/137691824/533ebdf9-282c-4d90-9629-8505c98c2983)
```
Repeater
|
|-- Operates at the physical layer
|
|-- Regenerates signals
|   |-- Receives a weak or corrupted signal
|   |-- Regenerates the original bit pattern
|   |-- Sends the refreshed signal
|
|-- Extends the physical length of a LAN
|   |-- Connects two segments of the same LAN
|   |-- Does not connect two LANs of different protocols
|
|-- Has no filtering capability
|   |-- Forwards every frame it receives
|
|-- Is a regenerator, not an amplifier
|   |-- Does not amplify the signal
|   |-- Regenerates the signal
|
|-- Placement is vital
    |-- Must be placed before the signal becomes too weak or corrupted
    |-- Still able to read the signal well enough to replicate it in its original form
```
![image](https://github.com/djmahe4/ktu-mindmaps/assets/137691824/244c271e-c919-4aff-8e00-5bf8888d833a)


3. **Active Hub**: An active hub, also known as a powered hub or an intelligent hub, strengthens the signal where a passive hub just repeats or copies signals. It needs electricity to operate and is smarter than a passive hub. It's a multi-point repeater with the capability of regenerating signals and can process and monitor information.
![image](https://github.com/djmahe4/ktu-mindmaps/assets/137691824/f62cc20c-ee20-428a-bae4-6f19e16f9d0e)
```
Active Hub
|
|-- Multipart Repeater
|   |-- Regenerates and forwards signals
|
|-- Used in Physical Star Topology
|   |-- Connects multiple stations
|
|-- Seen in Ethernet Implementations
|   |-- Example: 10Base-T
|
|-- Can Create Multiple Levels of Hierarchy
|   |-- Removes length limitation of 10Base-T (100 m)

```

5. **Two-Layer Switch (Layer 2 Switch)**: A two-layer switch operates at the data link layer (Layer 2) of the OSI model. It sends frames to the destination port using a MAC address table which stores the MAC addresses of devices associated with that port.

6. **Router**: A router is a device that connects two or more packet-switched networks or subnetworks. It manages traffic between these networks by forwarding data packets to their intended IP addresses, and allows multiple devices to use the same Internet connection.

7. **Three-Layer Switch (Layer 3 Switch)**: A three-layer switch is a special network device that has the functionality of a router and a switch combined into one chassis. It operates at both the data link layer (Layer 2) and the network layer (Layer 3) of the OSI model.

8. **Gateway**: A gateway is a connecting point of any network that helps it to connect with different networks. It monitors and controls all the incoming and outgoing traffic of the network.