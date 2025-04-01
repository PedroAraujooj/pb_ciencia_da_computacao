import math

cidades = {
    'A': (0, 0),
    'B': (1, 5),
    'C': (5, 2),
    'D': (6, 6),
    'E': (8, 3)
}

def distancia(a, b):
    x1, y1 = a
    x2, y2 = b
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def tsp_vizinho_mais_proximo(cidades, inicio='A'):
    nao_visitadas = set(cidades.keys())
    rota = [inicio]
    nao_visitadas.remove(inicio)

    atual = inicio

    while nao_visitadas:
        proxima, dist_min = None, float('inf')
        for c in nao_visitadas:
            d = distancia(cidades[atual], cidades[c])
            if d < dist_min:
                dist_min = d
                proxima = c
        rota.append(proxima)
        nao_visitadas.remove(proxima)
        atual = proxima

    rota.append(inicio)
    return rota


if __name__ == "__main__":
    cidade_inicial = 'A'

    rota_encontrada = tsp_vizinho_mais_proximo(cidades, inicio=cidade_inicial)

    print("Rota encontrada:", " -> ".join(rota_encontrada))
