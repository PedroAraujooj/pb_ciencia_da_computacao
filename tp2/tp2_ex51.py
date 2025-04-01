import time
from multiprocessing import Pool

def sum_parallel(lst):
    inicio = time.time()
    with Pool() as pool:
        chunk_size = len(lst) // 4
        chunks = [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]
        results = pool.map(sum, chunks)
    fim = time.time()
    return sum(results), fim - inicio
def sum_seq(lst):
    inicio = time.time()
    total = 0
    for i in range(len(lst)):
        total += lst[i]
    fim = time.time()
    return total, fim - inicio




if __name__ == "__main__":
    large_list = list(range(1, 10001))
    resul_parallel = sum_parallel(large_list.copy())
    resul_seq = sum_seq(large_list.copy())
    print(f"Soma paralela: {resul_parallel[0]}, tempo: {resul_parallel[1]:.7f}")
    print(f"Soma sequencial: {resul_seq[0]}, tempo: {resul_seq[1]:.7f}")


