# CodeAlpha_BasicNetworkSniffer

# Basic Network Sniffer 🕵️‍♂️

This project is the first task completed during an internship with **CodeAlpha**, focusing on fundamental cybersecurity and network analysis. The tool is a simple command-line network sniffer built in Python using the `scapy` library.

## Project Goals

The primary objectives of this task were to:

1.  **Capture** network traffic packets flowing through a specific network interface.
2.  **Analyze** the captured packets to understand their structure (L2, L3, L4 layers).
3.  **Display** useful information such as source/destination IPs, MAC addresses, protocols, and payloads.
4.  Gain a foundational understanding of network protocols like **TCP, UDP, ICMP, and ARP**.

## 🛠️ Technology Used

  * **Language:** Python 3.x
  * **Library:** [Scapy](https://scapy.net/) (for packet capture and dissection)

## Installation and Setup

### 1\. Prerequisites

You must have **Python 3** installed on your system.

### 2\. Install Scapy

The `scapy` library needs to be installed, and depending on your OS, you may need additional dependencies for raw packet capturing (like `libpcap` on Linux/macOS or Npcap/WinPcap on Windows).

```bash
pip install scapy
```

### 3\. Running with Administrator/Root Privileges

Network sniffing requires access to the network interface, which is a privileged operation. You must run the script with administrative rights:

**On Linux/macOS:**

```bash
sudo python your_sniffer_script.py
```

**On Windows:**
Run your command prompt or PowerShell "As Administrator."

## 🚀 How to Run the Sniffer

1.  **Save the Code:** Save the final Python script (e.g., `network_sniffer.py`).
2.  **Execution:** Run the script using the elevated privileges.

<!-- end list -->

```bash
# Example command (adjust based on your filename)
sudo python network_sniffer.py
```

The program will immediately start listening on the specified interface (e.g., `"Wi-Fi"`) and print details for every packet it captures.

## 📝 Code Functionality (Simplified)

The sniffer's analysis function dissects packets based on their layers:

| Layer | Protocol | Information Extracted |
| :---: | :--- | :--- |
| **L3** | **IP** | Source IP, Destination IP |
| **L2** | **Ethernet** | Source MAC, Destination MAC |
| **L4** | **TCP/UDP** | Source Port, Destination Port, Protocol Name |
| **L3** | **ICMP** | Type and Code (for diagnostics like Ping/Tracert) |
| **L2** | **ARP** | Sender IP (`psrc`) and MAC (`hwsrc`) for local address resolution |
| **L5+** | **Raw** | Packet payload data (if present) |

## Example Output

When running the sniffer, you will see output similar to this:

```
-------------------- NEW PACKET --------------------
Source: 192.168.1.10 (00:1a:2b:3c:4d:5e) --> Destination: 8.8.8.8 (ff:ff:ff:ff:ff:ff)
Protocol: UDP (Port: 54321 -> 53)
Payload Data (RAW):
b'\x11\x11\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x07google\x03com\x00\x00\x01\x00\x01'
--------------------------------------------------
ARP Packet: 192.168.1.1 is at aa:bb:cc:dd:ee:ff
--------------------------------------------------
Source: 192.168.1.10 (00:1a:2b:3c:4d:5e) --> Destination: 142.250.6.142 (00:11:22:33:44:55)
Protocol: TCP (Port: 44321 -> 443)
--------------------------------------------------
```

-----

## 🔗 Connect with Me

- [LinkedIn](https://www.linkedin.com/in/naji-abdellah-834411315/)
- [GitHub](https://github.com/naji-abdellah) 
- naji.abdellah.cp@gmail.com 

---

Made with ❤️ by **[NAJI ABDELLAH]**
