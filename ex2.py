import time
import tracemalloc
import pandas as pd


# Classes fornecidas pelo professor
class TabelaHash:
    def __init__(self, capacidade=10):
        self.capacidade = capacidade
        self.tabela = [[] for _ in range(capacidade)]
        self.size = 0

    def hash(self, chave):
        return hash(chave) % self.capacidade

    def inserir(self, chave, valor):
        indice = self.hash(chave)
        for par in self.tabela[indice]:
            if par[0] == chave:
                par[1] = valor
                return
        self.tabela[indice].append([chave, valor])
        self.size += 1

    def buscar(self, chave):
        indice = self.hash(chave)
        for par in self.tabela[indice]:
            return par[1]
        return None

    def remover(self, chave):
        indice = self.hash(chave)
        for i, par in enumerate(self.tabela[indice]):
            if par[0] == chave:
                del self.tabela[indice][i]
                self.size -= 1
                return True
        return False

    def __str__(self):
        resultado = []
        for lista in self.tabela:
            for par in lista:
                resultado.append(f"{par[0]}: {par[1]}")
        return "{ " + ", ".join(resultado) + " }"


class Pilha:
    def __init__(self, lista=None):
        if lista is None:
            self.itens = []
        else:
            self.itens = lista

    def is_empty(self):
        return len(self.itens) == 0

    def push(self, item):
        self.itens.append(item)

    def pop(self):
        if not self.is_empty():
            return self.itens.pop()
        else:
            return "A pilha está vazia"

    def peek(self):
        if not self.is_empty():
            return self.itens[-1]
        else:
            return "A pilha está vazia"

    def size(self):
        return len(self.itens)

    def display(self):
        print("Pilha:", self.itens)

    def clonar(self):
        return Pilha(list(self.itens))

    def recuperar(self, posicao):
        if posicao == -1:
            return self.peek()
        if posicao < 0 or posicao >= self.size():
            raise IndexError("Posição inválida")
        temp = Pilha()
        for _ in range(self.size() - posicao - 1):
            temp.push(self.pop())
        item = self.peek()
        while not temp.is_empty():
            self.push(temp.pop())

        return item

    def inserir(self, posicao, item):
        if posicao < 0 or posicao > self.size():
            raise IndexError("Posição inválida")
        temp = Pilha()
        for _ in range(self.size() - posicao):
            temp.push(self.pop())
        self.push(item)
        while not temp.is_empty():
            self.push(temp.pop())

    def remover(self, posicao):
        if posicao < 0 or posicao >= self.size():
            raise IndexError("Posição inválida")
        temp = Pilha()
        for _ in range(self.size() - posicao - 1):
            temp.push(self.pop())
        item = self.pop()
        while not temp.is_empty():
            self.push(temp.pop())
        return item

class Fila:
    def __init__(self, lista=None):
        if lista is None:
            self.itens = []
        else:
            self.itens = lista

    def is_empty(self):
        return len(self.itens) == 0

    def enqueue(self, item):
        self.itens.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.itens.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.itens[0]

    def size(self):
        return len(self.itens)

    def display(self):
        if self.is_empty():
            print("A fila está vazia")
        else:
            print("Fila:", end=" ")
            for item in self.itens:
                print(item, end=" ")
            print()

    def clonar(self):
        return Fila(list(self.itens))


def ler_listagem_arquivos(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        return [linha.strip() for linha in arquivo.readlines()]


def ler_operacoes(nome_arquivo):
    df = pd.read_excel(nome_arquivo)
    insercoes = []
    remocoes = []
    for index, row in df.iterrows():
        if pd.notna(row['Posição']) and pd.notna(row['Operação']):
            posicao = int(row['Posição'])
            operacao = row['Operação']
            nome_arquivo = row.get('Nome do Arquivo', None)
            if operacao == 'Inserção':
                insercoes.append({'posicao': posicao, 'nome_arquivo': nome_arquivo})
        if pd.notna(row['Posição.1']) and pd.notna(row['Operação.1']):
            posicao = int(row['Posição.1'])
            operacao = row['Operação.1']
            if operacao == 'Remoção':
                remocoes.append({'posicao': posicao})
    return insercoes, remocoes


def inicializar_tabela_hash(lista):
    tabela = TabelaHash(capacidade=len(lista))
    for idx, item in enumerate(lista):
        tabela.inserir(idx, item)
    return tabela


def recuperacao_tabela_hash(tabela, posicoes):
    recuperados = []
    listaMediaTempo = [0] * 5
    listaMediaMemo = [0] * 5
    for i in range(10):
        recuperados = []
        tracemalloc.start()
        start_time = time.time()
        for idx, pos in enumerate(posicoes):
            valor = tabela.buscar(pos)
            current, peak = tracemalloc.get_traced_memory()
            end_time = time.time()
            elapsed_time = end_time - start_time
            listaMediaTempo[idx] += elapsed_time
            listaMediaMemo[idx] += peak
            # print(
            #     f"Tabela Hash - Recuperação da posição {pos}: tempo = {elapsed_time:.6f}s, memória = {peak / 1024:.2f} KiB")
            recuperados.append(valor)
    tracemalloc.stop()
    for i in range(5):
        print(
            f"Tabela Hash - Recuperação da posição {posicoes[i]}: tempo = {(listaMediaTempo[i] / 10):.6f}s, memória = {(listaMediaMemo[i] / 10) / 1024:.2f} KiB")
    return recuperados


def insercao_remocao_tabela_hash(tabela, insercoes, remocoes):
    total_ops = len(insercoes)
    listaMediaTempo = [0] * 8
    listaMediaMemo = [0] * 8
    listaMediaTempoRemove = [0] * 8
    listaMediaMemoRemove = [0] * 8
    for i in range(10):
        op_count = 0
        start_time = time.time()
        tracemalloc.start()
        for idx, op in enumerate(insercoes, 1):
            tabela.inserir(op['posicao'], op['nome_arquivo'])
            op_count += 1
            if op_count % 50 == 0 or op_count == total_ops:
                current, peak = tracemalloc.get_traced_memory()
                end_time = time.time()
                elapsed_time = end_time - start_time
                listaMediaTempo[int((op_count / 50) - 1)] = listaMediaTempo[int((op_count / 50) - 1)] + elapsed_time
                listaMediaMemo[int((op_count / 50) - 1)] = listaMediaMemo[int((op_count / 50) - 1)] + peak
        op_count = 0
        for idx, op in enumerate(remocoes, 1):
            tabela.remover(op['posicao'])
            op_count += 1
            if op_count % 50 == 0 or op_count == total_ops:
                current, peak = tracemalloc.get_traced_memory()
                end_time = time.time()
                elapsed_time = end_time - start_time
                listaMediaTempoRemove[int((op_count / 50) - 1)] = listaMediaTempoRemove[
                                                                      int((op_count / 50) - 1)] + elapsed_time
                listaMediaMemoRemove[int((op_count / 50) - 1)] = listaMediaMemoRemove[int((op_count / 50) - 1)] + peak
        tracemalloc.stop()
    for i in range(8):
        print(
            f"Tabela Hash - Após {50 * (i + 1)} inserções: tempo médio = {(listaMediaTempo[i] / 10):.8f}s, memória média = {(listaMediaMemo[i] / 10) / 1024:.2f} KiB")
    for i in range(8):
        print(
            f"Tabela Hash - Após 400 inserções e {50 * (i + 1)} remoções: tempo médio = {(listaMediaTempoRemove[i] / 10):.8f}s, memória média = {(listaMediaMemoRemove[i] / 10) / 1024:.2f} KiB")


def inicializar_pilha(lista):
    pilha = Pilha(lista)
    return pilha


def recuperacao_pilha(pilha, posicoes):
    recuperados = []
    listaMediaTempo = [0] * 5
    listaMediaMemo = [0] * 5
    for i in range(10):
        recuperados = []
        start_time = time.time()
        tracemalloc.start()
        for idx, pos in enumerate(posicoes):
            valor = pilha.recuperar(pos)
            current, peak = tracemalloc.get_traced_memory()
            end_time = time.time()
            elapsed_time = end_time - start_time
            listaMediaTempo[idx] += elapsed_time
            listaMediaMemo[idx] += peak
            #print(f"Pilha - Recuperação da posição {pos}: tempo = {elapsed_time:.6f}s, memória = {peak / 1024:.2f} KiB")
            recuperados.append(valor)
    tracemalloc.stop()
    for i in range(5):
        print(
            f"Pilha - Recuperação da posição {posicoes[i]}: tempo = {int(listaMediaTempo[i] / 10):.6f}s, memória = {(listaMediaMemo[i] / 10) / 1024:.2f} KiB")
    return recuperados


def insercao_remocao_pilha(pilha, insercoes, remocoes):
    total_ops = len(insercoes)
    listaMediaTempo = [0] * 8
    listaMediaMemo = [0] * 8
    listaMediaTempoRemove = [0] * 8
    listaMediaMemoRemove = [0] * 8
    for i in range(10):
        op_count = 0
        start_time = time.time()
        tracemalloc.start()
        for idx, op in enumerate(insercoes, 1):
            pos = op['posicao']
            if 0 <= pos <= len(pilha.itens):
                pilha.inserir(pos, op['nome_arquivo'])
            op_count += 1
            if op_count % 50 == 0 or op_count == total_ops:
                current, peak = tracemalloc.get_traced_memory()
                end_time = time.time()
                elapsed_time = end_time - start_time
                listaMediaTempo[int((op_count / 50) - 1)] = listaMediaTempo[int((op_count / 50) - 1)] + elapsed_time
                listaMediaMemo[int((op_count / 50) - 1)] = listaMediaMemo[int((op_count / 50) - 1)] + peak
        op_count = 0
        for idx, op in enumerate(remocoes, 1):
            pos = op['posicao']
            if 0 <= pos < len(pilha.itens):
                pilha.remover(pos)
            op_count += 1
            if op_count % 50 == 0 or op_count == total_ops:
                current, peak = tracemalloc.get_traced_memory()
                elapsed_time = time.time() - start_time
                listaMediaTempoRemove[int((op_count / 50) - 1)] = listaMediaTempoRemove[int((op_count / 50) - 1)] + elapsed_time
                listaMediaMemoRemove[int((op_count / 50) - 1)] = listaMediaMemoRemove[int((op_count / 50) - 1)] + peak
        tracemalloc.stop()
    for i in range(8):
        print(
            f"Pilha - Após {50 * (i + 1)} inserções: tempo médio = {(listaMediaTempo[i] / 10):.8f}s, memória média = {(listaMediaMemo[i] / 10) / 1024:.2f} KiB")
    for i in range(8):
        print(
            f"Pilha - Após 400 inserções e {50 * (i + 1)} remoções: tempo médio = {(listaMediaTempoRemove[i] / 10):.8f}s, memória média = {(listaMediaMemoRemove[i] / 10) / 1024:.2f} KiB")


def inicializar_fila(lista):
    fila = Fila(lista)
    return fila


def recuperacao_fila(fila, posicoes):
    recuperados = []
    listaMediaTempo = [0] * 5
    listaMediaMemo = [0] * 5
    for i in range(10):
        recuperados = []
        start_time = time.time()
        tracemalloc.start()
        for idx, pos in enumerate(posicoes):
            valor = fila.itens[pos]
            current, peak = tracemalloc.get_traced_memory()
            end_time = time.time()
            elapsed_time = end_time - start_time
            listaMediaTempo[idx] += elapsed_time
            listaMediaMemo[idx] += peak
            #print(f"Fila - Recuperação da posição {pos}: tempo = {elapsed_time:.6f}s, memória = {peak / 1024:.2f} KiB")
            recuperados.append(valor)
    tracemalloc.stop()
    for i in range(5):
        print(
            f"Fila - Recuperação da posição {posicoes[i]}: tempo = {int(listaMediaTempo[i] / 10):.6f}s, memória = {(listaMediaMemo[i] / 10) / 1024:.2f} KiB")
    return recuperados


def insercao_remocao_fila(fila, insercoes, remocoes):
    total_ops = len(insercoes)
    listaMediaTempo = [0] * 8
    listaMediaMemo = [0] * 8
    listaMediaTempoRemove = [0] * 8
    listaMediaMemoRemove = [0] * 8
    for i in range(10):
        op_count = 0
        start_time = time.time()
        tracemalloc.start()
        for idx, op in enumerate(insercoes, 1):
            pos = op['posicao']
            if 0 <= pos <= len(fila.itens):
                fila.itens.insert(pos, op['nome_arquivo'])
            op_count += 1
            if op_count % 50 == 0 or op_count == total_ops:
                current, peak = tracemalloc.get_traced_memory()
                end_time = time.time()
                elapsed_time = end_time - start_time
                listaMediaTempo[int((op_count / 50) - 1)] = listaMediaTempo[int((op_count / 50) - 1)] + elapsed_time
                listaMediaMemo[int((op_count / 50) - 1)] = listaMediaMemo[int((op_count / 50) - 1)] + peak
        op_count = 0
        for idx, op in enumerate(remocoes, 1):
            pos = op['posicao']
            if 0 <= pos < len(fila.itens):
                del fila.itens[pos]
            op_count += 1
            if op_count % 50 == 0 or op_count == total_ops:
                current, peak = tracemalloc.get_traced_memory()
                elapsed_time = time.time() - start_time
                listaMediaTempoRemove[int((op_count / 50) - 1)] = listaMediaTempoRemove[int((op_count / 50) - 1)] + elapsed_time
                listaMediaMemoRemove[int((op_count / 50) - 1)] = listaMediaMemoRemove[int((op_count / 50) - 1)] + peak
        tracemalloc.stop()
    for i in range(8):
        print(
            f"Fila - Após {50 * (i + 1)} inserções: tempo médio = {(listaMediaTempo[i] / 10):.8f}s, memória média = {(listaMediaMemo[i] / 10) / 1024:.2f} KiB")
    for i in range(8):
        print(
            f"Fila - Após 400 inserções e {50 * (i + 1)} remoções: tempo médio = {(listaMediaTempoRemove[i] / 10):.8f}s, memória média = {(listaMediaMemoRemove[i] / 10) / 1024:.2f} KiB")


if __name__ == "__main__":
    nome_arquivo_lista = 'pb_tp1.txt'
    nome_arquivo_operacoes = 'operacoes.xlsx'
    lista_arquivos = ler_listagem_arquivos(nome_arquivo_lista)
    insercoes, remocoes = ler_operacoes(nome_arquivo_operacoes)
    posicoes_recuperacao = [0, 99, 999, 4999, -1]

    print("\n--- Operações na Tabela Hash ---")
    tabela_hash = inicializar_tabela_hash(list(lista_arquivos))
    recuperados_hash = recuperacao_tabela_hash(tabela_hash, list(posicoes_recuperacao))
    print(f"Arquivos recuperados da Tabela Hash: {recuperados_hash}")
    insercao_remocao_tabela_hash(tabela_hash, insercoes, remocoes)

    print("\n--- Operações na Pilha ---")
    pilha = inicializar_pilha(list(lista_arquivos))
    recuperados_pilha = recuperacao_pilha(pilha, list(posicoes_recuperacao))
    print(f"Arquivos recuperados da Pilha: {recuperados_pilha}")
    insercao_remocao_pilha(pilha, insercoes, remocoes)

    print("\n--- Operações na Fila ---")
    fila = inicializar_fila(list(lista_arquivos))
    recuperados_fila = recuperacao_fila(fila, list(posicoes_recuperacao))
    print(f"Arquivos recuperados da Fila: {recuperados_fila}")
    insercao_remocao_fila(fila, insercoes, remocoes)
