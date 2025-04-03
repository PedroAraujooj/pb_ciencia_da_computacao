import ipaddress

def valida_ip(ip_str, prefixo):
    try:
        ip = ipaddress.IPv4Address(ip_str)
        network = ipaddress.IPv4Network(prefixo, strict=False)
        # print(network)
        return ip in network
    except ValueError as e:
        print(f"Erro ao converter endereço ou prefixo: {e}")
        return False


if __name__ == '__main__':
    ip = "192.168.1.5"
    prefixo = "192.168.1.0/24"

    if valida_ip(ip, prefixo):
        print(f"O IP {ip} está contido no prefixo {prefixo}.")
    else:
        print(f"O IP {ip} NÃO está contido no prefixo {prefixo}.")
