import socket
import ssl

_original_send = ssl.SSLSocket.send
_original_recv = ssl.SSLSocket.recv


def monkeypatched_send(self, data, flags=0):
    if isinstance(data, memoryview):
        data = data.tobytes()
    print(f"Interceptado (envio): {data}")
    return _original_send(self, data, flags)


def monkeypatched_recv(self, buflen=1024, flags=0):
    data = _original_recv(self, buflen, flags)
    if data:
        print(f"Interceptado (recebido): {data}")
    return data


ssl.SSLSocket.send = monkeypatched_send
ssl.SSLSocket.recv = monkeypatched_recv

if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 8443

    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        with context.wrap_socket(sock, server_hostname=HOST) as tls_sock:
            print("Cliente TLS: conexão estabelecida")

            tls_sock.sendall('Ola do cliente TLS!'.encode('utf-8'))

            data = tls_sock.recv(1024)
            if data:
                print("Cliente TLS: recebido:", data.decode('utf-8'))

    print("Cliente TLS: conexão encerrada")
