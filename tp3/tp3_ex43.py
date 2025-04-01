import ipaddress

from tp3.ArvoreTrie import Trie
from tp3.RadixTrie import RadixTrie

def converter_ip_v6_para_binario(ip_str):
    try:
        ip = ipaddress.IPv6Address(ip_str)
        bin_str = format(int(ip), '0128b')
        return bin_str
    except ValueError as e:
        print(f"Erro ao converter endereço ou network: {e}")
        return None

def converter_net_v6_para_binario(net_str):
    try:
        net = ipaddress.IPv6Network(net_str, strict=False)
        bin_str = f"{int(net.network_address):0128b}/{net.prefixlen}"
        return bin_str
    except ValueError as e:
        print(f"Erro ao converter endereço ou network: {e}")
        return None

def converter_binario_para_ip_v6(bin_str):
    try:
        ip_int = int(bin_str, 2)
        ip = ipaddress.IPv6Address(ip_int)
        return ip
    except ValueError as e:
        print(f"Erro ao converter endereço ou network: {e}")
        return None

def converter_binario_para_network_v6(bin_net_str):
    try:
        bin_addr, prefix_str = bin_net_str.split('/')
        prefix = int(prefix_str)
        ip_int = int(bin_addr, 2)
        ip_addr = ipaddress.IPv6Address(ip_int)
        network = ipaddress.IPv6Network(f"{ip_addr}/{prefix}", strict=False)
        return network
    except ValueError as e:
        print(f"Erro ao converter endereço ou network: {e}")
        return None


if __name__ == '__main__':
    trie = RadixTrie()
    trie.insert(converter_net_v6_para_binario("2001:db8::/32"))
    trie.insert(converter_net_v6_para_binario("2001:db8:1234::/48"))

    print(converter_binario_para_network_v6(trie.busca_by_prefixo(converter_ip_v6_para_binario("2001:db8:1234:5678::1"))))
