import concurrent.futures
import multiprocessing

def soma_parcial(numeros):
    return sum(numeros)

def soma_total_paralela():
    num_partes = multiprocessing.cpu_count()
    numeros = list(range(1, 10000000 + 1))
    tamanho_chunk = len(numeros) // num_partes

    chunks = [numeros[i * tamanho_chunk: (i + 1) * tamanho_chunk] for i in range(num_partes)]

    with concurrent.futures.ProcessPoolExecutor(max_workers=num_partes) as executor:
        resultados = list(executor.map(soma_parcial, chunks))

    soma_total = sum(resultados)
    return soma_total

if __name__ == '__main__':
    resultado = soma_total_paralela()
    print("A soma total é:", resultado)
