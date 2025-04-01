import concurrent.futures
import time

import matplotlib.pyplot as plt

def calcular_primos_seq(y):
    inicio = time.time()
    if y < 2:
        return []
    eh_primo = [True] * (y + 1)
    eh_primo[0] = False
    eh_primo[1] = False

    for i in range(2, int(y**0.5) + 1):
        if eh_primo[i]:
            for multiplo in range(i*i, y + 1, i):
                eh_primo[multiplo] = False

    fim = time.time()
    return [num for num in range(2, y + 1) if eh_primo[num]], fim - inicio

def _eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def calcular_primos_paralelo(limite):
    inicio = time.time()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = {executor.submit(_eh_primo, n): n for n in range(2, limite + 1)}
        primos = []
        for futuro in concurrent.futures.as_completed(futures):
            numero = futures[futuro]
            if futuro.result():
                primos.append(numero)
        fim = time.time()
        return sorted(primos), fim - inicio

if __name__ == "__main__":
    tempos_seq=[0]*10
    tempos_paralell=[0]*10
    for i in range(10):
        tempos_seq[i] = calcular_primos_seq(10000 * (1+1))[1]
        tempos_paralell[i] = calcular_primos_paralelo(10000 * (1+1))[1]

    plt.figure(figsize=(8, 6))
    plt.plot(tempos_seq, [i for i in range(10)], marker='o')
    plt.plot(tempos_paralell, [i for i in range(10)], marker='x')
    plt.title('Número do range x Tempo de Execução')
    plt.xlabel('Segundos')
    plt.ylabel('Número do range')
    plt.grid(True)
    plt.savefig("tp3_ex24.png")
