# Network Topology Mapper

A Python-based network topology mapper that discovers all active devices on a local network using ARP scanning and visualizes them as an interactive graph.

---

## Features

- ARP sweep to discover all live hosts on a network
- Hostname resolution for each discovered device
- MAC address detection
- Visual network graph — router at center, all devices connected
- User input for IP range — scan any local network

---

## How It Works

The tool sends ARP (Address Resolution Protocol) broadcast packets to every IP in the given range. Any device that responds is considered a live host. Their IP, MAC address, and hostname are recorded, then visualized as a network graph using NetworkX and Matplotlib.

| Response | Meaning |
|---|---|
| ARP Reply received | Device is online |
| No response | Device is offline or filtered |

---

## Technologies Used

- Python 3
- `scapy` — ARP packet crafting and sending
- `socket` — hostname resolution
- `networkx` — network graph construction
- `matplotlib` — graph visualization

---

## Installation

```bash
git clone https://github.com/WajihaHabibullah/Network-Topology-Mapper.git
cd Network-Topology-Mapper
pip install scapy networkx matplotlib
python topology_mapper.py
```

---

## Usage

```bash
python topology_mapper.py
Enter IP range to scan (e.g. 192.168.18.1/24): 192.168.18.1/24
```

---

## Sample Output

```
Scanning 192.168.18.1/24...

Found 6 devices:

IP: 192.168.18.1    MAC: 70:fd:45:43:7f:78   Name: Unknown  (Router)
IP: 192.168.18.10   MAC: 3e:d8:70:5b:43:08   Name: Unknown  (Phone)
IP: 192.168.18.30   MAC: 40:ed:00:8b:71:d5   Name: Unknown  (TP-Link Device)
IP: 192.168.18.165  MAC: 2c:98:11:1f:e8:d5   Name: Wajiha   (Laptop)
IP: 192.168.18.202  MAC: c2:df:f3:92:8e:31   Name: Unknown  (Phone)
IP: 192.168.18.254  MAC: a0:9f:7a:39:5c:02   Name: Unknown  (Router Interface)
```

A network graph window opens showing all devices connected to the router.

---

## Real World Application

Network topology mapping is the first step in **internal network reconnaissance** during a penetration test. Once live hosts are discovered, each device can be further analyzed using a port scanner to identify open services and potential vulnerabilities.

This tool works alongside the [Port Scanner](https://github.com/WajihaHabibullah/Port-Scanner) for a complete recon workflow:
1. **Topology Mapper** — discover all live hosts
2. **Port Scanner** — scan each host for open ports and services

---

## Legal & Ethical Notice

> Only scan networks you own or have **explicit written permission** to test.
> Unauthorized network scanning may be illegal under cybersecurity laws including Pakistan's PECA 2016.
> This tool is intended for educational purposes and authorized security assessments only.

---

## Author

**Wajiha Habibullah**
CS Student — NUCES FAST, Karachi
[github.com/WajihaHabibullah](https://github.com/WajihaHabibullah)

---

## Related Projects

- [Port Scanner](https://github.com/WajihaHabibullah/Port-Scanner)
- [DNS Query Resolver](https://github.com/WajihaHabibullah/DNS-Query-Resolver-)
