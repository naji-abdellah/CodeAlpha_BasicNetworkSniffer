from scapy.all import *


def packet_analysis(pkt):
    print("-------------------- new packet --------------------")

    # 1. check for the essential network layer (IP)
    if IP in pkt:

        # extract (MAC) and (IP) info
        src_ip = pkt[IP].src
        dst_ip = pkt[IP].dst
        src_mac = pkt.src
        dst_mac = pkt.dst

        print(f"source: {src_ip} ({src_mac}) --> destination: {dst_ip} ({dst_mac})")

        # 2. check for the transport layers
        if TCP in pkt:
            protocol = "TCP"
            print(f"protocol: {protocol} (port: {pkt[TCP].sport} -> {pkt[TCP].dport})")

        elif UDP in pkt:
            protocol = "UDP"
            print(f"protocol: {protocol} (port: {pkt[UDP].sport} -> {pkt[UDP].dport})")

        elif ICMP in pkt:
            protocol = "ICMP"
            print(f"protocol: {protocol} (type: {pkt[ICMP].type}, code: {pkt[ICMP].code})")

        else:
            protocol = "other"
            print(f"protocol: {protocol} (IP ID: {pkt[IP].id})")

        # 3. check for payload
        if Raw in pkt:
            print("payload data :")
            # decode the payload for better readability
            try:
                print(pkt[Raw].load.decode('utf-8'))
            except:
                print(pkt[Raw].load)

    # 4. handle non-IP traffic (like ARP)
    elif ARP in pkt:
        print(f"ARP packet: {pkt[ARP].psrc} is at {pkt[ARP].hwsrc}")

    print("--------------------------------------------------")


# sniff 10 packets on the Wi-Fi interface, applying the analysis function
sniff(iface="Wi-Fi", prn=packet_analysis, count=10)