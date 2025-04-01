def contar_cadeiras(N, C):
    dp = [[0]*C for _ in range(N+1)]
    for c in range(C):
        dp[1][c] = 1
    total = [0]*(N+1)
    total[1] = sum(dp[1])
    for i in range(2, N+1):
        for c in range(C):
            dp[i][c] = total[i-1] - dp[i-1][c]
        total[i] = sum(dp[i])
    return total[N]

if __name__ == '__main__':
    N1 = 5
    C1 = 3
    resultado1 = contar_cadeiras(N1, C1)
    print(f"Número de maneiras de pintar {N1} cadeiras com {C1} cores exemplo 1: {resultado1}")

    N2 = 8
    C2 = 9
    resultado2 = contar_cadeiras(N2, C2)
    print(f"Número de maneiras de pintar {N2} cadeiras com {C2} cores exemplo 2: {resultado2}")

    N3 = 15
    C3 = 5
    resultado3 = contar_cadeiras(N3, C3)
    print(f"Número de maneiras de pintar {N3} cadeiras com {C3} cores exemplo 3: {resultado3}")
