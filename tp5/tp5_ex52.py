import sys
import subprocess


def main():
    if len(sys.argv) < 2:
        print(f"Uso: python {sys.argv[0]} <IP/host>")
        sys.exit(1)

    target_host = sys.argv[1]

    cmd = ["nmap", "-sV", target_host]

    try:
        resultado = subprocess.run(cmd, capture_output=True, text=True, check=True)
        saida = resultado.stdout

        print(f"\n===> Saída completa do Nmap para o IP {target_host}:\n")
        print(saida)

        print("===> Portas abertas e serviços detectados:\n")

        for linha in saida.splitlines():
            if "/tcp" in linha and ("open" in linha or "filtered" in linha):
                print(linha)

    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o Nmap: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
