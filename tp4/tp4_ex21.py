from Trie import Trie

if __name__ == "__main__":

    trie = Trie()
    trie.insert("casa")
    trie.insert("carro")
    trie.insert("caminhão")
    trie.insert("cachorro")
    trie.insert("cadeira")

    trie.show_hierarchy()