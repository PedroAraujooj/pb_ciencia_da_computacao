import ipaddress

from tp3.ArvoreTrie import Trie
from tp3.RadixTrie import RadixTrie

def converter_ip_para_binario(ip_str):
    try:
        ip = ipaddress.IPv4Address(ip_str)
        bin_str = format(int(ip), '032b')
        return bin_str
    except ValueError as e:
        print(f"Erro ao converter endereço ou network: {e}")
        return None

def converter_net_para_binario(net_str):
    try:
        net = ipaddress.IPv4Network(net_str, strict=False)
        bin_str = f"{int(net.network_address):032b}/{net.prefixlen}"
        return bin_str
    except ValueError as e:
        print(f"Erro ao converter endereço ou network: {e}")
        return None

def converter_binario_para_ip(bin_str):
    try:
        ip_int = int(bin_str, 2)
        ip = ipaddress.IPv4Address(ip_int)
        return ip
    except ValueError as e:
        print(f"Erro ao converter endereço ou network: {e}")
        return None

def converter_binario_para_network(bin_net_str):
    try:
        bin_addr, prefix_str = bin_net_str.split('/')
        prefix = int(prefix_str)
        ip_int = int(bin_addr, 2)
        ip_addr = ipaddress.IPv4Address(ip_int)
        network = ipaddress.IPv4Network(f"{ip_addr}/{prefix}", strict=False)
        return network
    except ValueError as e:
        print(f"Erro ao converter endereço ou network: {e}")
        return None


if __name__ == '__main__':
    trie = RadixTrie()
    trie.insert(converter_net_para_binario("192.168.0.0/16"))
    trie.insert(converter_net_para_binario("192.168.1.0/24"))
    trie.insert(converter_net_para_binario("10.0.0.0/8"))

    print(converter_binario_para_network(trie.busca_by_prefixo(converter_ip_para_binario("192.168.1.100"))))
