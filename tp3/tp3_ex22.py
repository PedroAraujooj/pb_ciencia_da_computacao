import concurrent.futures


def process_row(args):
    return calc_linha(*args)


def calc_linha(linha, colunas):
    linha_final = []
    for i in range(len(colunas)):
        total = 0
        for j in range(len(linha)):
            total += linha[j] * colunas[i][j]
        linha_final.append(total)
    return linha_final


def cal_matrix(matrixA, matrixB):
    if len(matrixA[0]) != len(matrixB):
        raise ValueError("Número de colunas de A deve ser igual ao número de linhas de B.")
    linhasA = matrixA
    colunasB = []
    for i in range(len(matrixB[0])):
        coluna = [matrixB[j][i] for j in range(len(matrixB))]
        colunasB.append(coluna)

    linhaAndColunas = [(linhasA[i], colunasB) for i in range(0, len(linhasA))]
    with concurrent.futures.ProcessPoolExecutor() as executor:
        resultados = list(executor.map(process_row, linhaAndColunas))
    return resultados


if __name__ == '__main__':
    matrixA = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    matrixB = [
        [7, 8],
        [9, 10],
        [11, 12]
    ]

    resultado = cal_matrix(matrixA, matrixB)

    print("Matriz A:")
    for linha in matrixA:
        print(linha)

    print("\nMatriz B:")
    for linha in matrixB:
        print(linha)

    print("\nMatriz Resultado (A x B):")
    for linha in resultado:
        print(linha)
