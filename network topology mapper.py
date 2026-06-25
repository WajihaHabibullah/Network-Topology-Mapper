import socket
import networkx as nx
import matplotlib.pyplot as plt
from scapy.all import ARP, Ether, srp

def scan_network(ip_range):
    print(f"Scanning {ip_range}...\n")
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    result = srp(packet, timeout=2, verbose=0)[0]
    devices = []
    for sent, received in result:
        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc
        })
    return devices

def get_hostname(ip):
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        return hostname
    except:
        return "Unknown"

def draw_graph(devices):
    G = nx.Graph()
    router = "192.168.18.1\n(Router)"
    G.add_node(router)
    for device in devices:
        if device['ip'] == "192.168.18.1":
            continue
        label = f"{device['ip']}\n{device['hostname']}"
        G.add_node(label)
        G.add_edge(router, label)
    plt.figure(figsize=(10, 7))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos,
            with_labels=True,
            node_color="skyblue",
            node_size=3000,
            font_size=8,
            font_weight="bold",
            edge_color="gray")
    plt.title("Network Topology Map", fontsize=14)
    plt.tight_layout()
    plt.show()

ip_range = input("Enter IP range to scan (e.g. 192.168.18.1/24): ")
devices = scan_network(ip_range)

print(f"Found {len(devices)} devices:\n")
for device in devices:
    device['hostname'] = get_hostname(device['ip'])
    print(f"IP: {device['ip']}  MAC: {device['mac']}  Name: {device['hostname']}")

draw_graph(devices)
