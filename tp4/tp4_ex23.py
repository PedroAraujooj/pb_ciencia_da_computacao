from Trie import Trie

if __name__ == "__main__":

    trie = Trie()
    trie.insert("casa")
    trie.insert("carro")
    trie.insert("caminhão")
    trie.insert("cachorro")
    trie.insert("cadeira")

    print("Palavras na Trie: ")
    print(trie.list_words())

    print(f"\nBusca para o prefixo cad: {trie.busca_by_prefixo("cad")}")
    print(f"Busca para o prefixo ca: {trie.busca_by_prefixo("ca")}")

