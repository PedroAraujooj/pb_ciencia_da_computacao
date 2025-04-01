from scapy.all import ARP, sniff, conf


def arpDisplay(pack):
    if pack.haslayer(ARP) and pack[ARP].op == 2:
        ip_fonte = pack[ARP].psrc
        mac_fonte = pack[ARP].hwsrc
        print(f"IP: {ip_fonte}, MAC: {mac_fonte}")


if __name__ == "__main__":
    sniff(iface=conf.iface, prn=arpDisplay, filter="arp", store=0, count=10)
