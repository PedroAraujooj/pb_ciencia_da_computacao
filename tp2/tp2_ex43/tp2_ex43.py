import time
import matplotlib.pyplot as plt


def tores_de_hanoi(n, origem, destino, aux):
    if n == 1:
        print(f"Mova o disco 1 de {origem} para {destino}")
    else:
        tores_de_hanoi(n - 1, origem, aux, destino)
        print(f"Mova o disco {n} de {origem} para {destino}")
        tores_de_hanoi(n - 1, aux, destino, origem)

if __name__ == "__main__":
    tempo = [0]*4

    for n in range(1, 5):
        inicio = time.time()
        print(f"Torre com {6*n} discos ==============================")
        tores_de_hanoi(6*n, 'A', 'B', 'C')
        print(f"fim da torre com {6*n} discos =======================")
        fim = time.time()
        tempo[n - 1] += fim - inicio

    plt.figure(figsize=(8, 6))
    plt.plot([6*i for i in range(1, 5)], tempo, marker='o')
    plt.title('Tempo de Execução x Número de discos')
    plt.xlabel('Número de discos')
    plt.ylabel('Segundos')
    plt.grid(True)
    plt.savefig("tp2_ex43.png")


