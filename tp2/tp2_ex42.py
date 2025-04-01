import time


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

if __name__ == "__main__":
    tempo_regular = 0
    tempo_memo = 0
    for _ in range(10):
        inicio = time.time()
        for n in range(10, 31):
            fibonacci(n)
        fim = time.time()
        tempo_regular += fim - inicio

    for _ in range(10):
        inicio = time.time()
        for n in range(10, 31):
            fibonacci_memo(n)
        fim = time.time()
        tempo_memo += fim - inicio

    print(f"Tempo sem memorização: {tempo_regular/10:.14f}")
    print(f"Tempo com memorização: {tempo_memo/10:.14f}")



