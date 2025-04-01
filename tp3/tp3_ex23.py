import concurrent.futures

def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def calcular_primos(limite):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = {executor.submit(eh_primo, n): n for n in range(2, limite + 1)}
        primos = []
        for futuro in concurrent.futures.as_completed(futures):
            numero = futures[futuro]
            if futuro.result():
                primos.append(numero)

        return sorted(primos)

if __name__ == "__main__":
    resultado = calcular_primos(100000)
    print(f"Números primos até {100000}:", resultado)
