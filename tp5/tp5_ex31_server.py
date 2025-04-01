import socket
import ssl

if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 8443

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen()
    print(f"Servidor TLS escutando em {HOST}:{PORT}...")

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile='server.crt', keyfile='server.key')

    while True:
        conexao, addr = sock.accept()
        print(f"Conexão estabelecida com {addr}")
        try:
            with context.wrap_socket(conexao, server_side=True) as tls_con:
                data = tls_con.recv(1024)
                if not data:
                    break
                print("Recebido:", data.decode())
                tls_con.sendall(data)
        except ssl.SSLError as e:
            print("Erro SSL:", e)

    conexao.close()
    print('Conexão encerrada')
