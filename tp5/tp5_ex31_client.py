import socket
import ssl



if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 8443

    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        with context.wrap_socket(sock, server_hostname=HOST) as tls_sock:
            print("Cliente: conexão estabelecida")
            mensagem = "Olá, servidor TLS!"
            tls_sock.sendall(mensagem.encode('utf-8'))

            data = tls_sock.recv(1024)
            print("Cliente: recebido:", data.decode('utf-8'))
