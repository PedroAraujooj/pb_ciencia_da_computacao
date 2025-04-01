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
    print("\n Contêm caminhonete?")
    print(trie.search("caminhonete"))
    print("\n Contêm caminhão?")
    print(trie.search("caminhão"))
