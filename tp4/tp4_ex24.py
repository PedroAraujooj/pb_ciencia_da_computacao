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
    trie.show_hierarchy()

    print(f"\nApós retirada da cadeira: ")
    trie.delete("cadeira")
    print(trie.list_words())
    trie.show_hierarchy()
