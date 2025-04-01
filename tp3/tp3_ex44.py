import ipaddress
import random
import time

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


def busca_by_prefixo_seq(lista_pre, end_ip):
    if not lista_pre:
        return None
    melhor_match = None
    melhor_tamanho_prefixo = 0

    for pre in lista_pre:
        prefix_len = 0
        while (prefix_len < len(pre) and
               prefix_len < len(end_ip) and
               pre[prefix_len] == end_ip[prefix_len]):
            prefix_len += 1

        if prefix_len > melhor_tamanho_prefixo:
            melhor_tamanho_prefixo = prefix_len
            melhor_match = pre

    return melhor_match


def gerar_ipv4_network_binario():
    prefix = random.randint(8, 30)
    network_portion = random.getrandbits(prefix)
    network_int = network_portion << (32 - prefix)
    bin_addr = format(network_int, '032b')
    return f"{bin_addr}/{prefix}"


if __name__ == '__main__':
    trie = RadixTrie()
    networks_bin = [gerar_ipv4_network_binario() for _ in range(1000)]
    for net in networks_bin:
        trie.insert(net)
    lista = trie.list_words()
    temp_seq = 0
    temp_trie = 0

    for i in range(20):
        inicio_seq = time.time()
        (busca_by_prefixo_seq(lista, converter_ip_para_binario("192.168.1.100")))
        fim_seq = time.time()
        temp_seq += fim_seq - inicio_seq

        inicio_trie = time.time()
        (trie.busca_by_prefixo(converter_ip_para_binario("192.168.1.100")))
        fim_trie = time.time()
        temp_trie += fim_trie - inicio_trie

    print(f"Tempo médio sequencial: {(temp_seq / 20):.20f}")
    print(f"Tempo médio Trie: {(temp_trie / 20):.20f}")
