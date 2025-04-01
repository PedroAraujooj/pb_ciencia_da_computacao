

#Classes fornecidas pelo professor
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def delete(self, word):

        def _delete(node, word, depth):
            if depth == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0

            char = word[depth]
            if char not in node.children:
                return False

            should_delete_child = _delete(node.children[char], word, depth + 1)

            if should_delete_child:
                del node.children[char]
                return len(node.children) == 0 and not node.is_end_of_word

            return False

        _delete(self.root, word, 0)

    def list_words(self):
        def _dfs(node, prefix, words):
            if node.is_end_of_word:
                words.append(prefix)
            for char, child in node.children.items():
                _dfs(child, prefix + char, words)

        words = []
        _dfs(self.root, "", words)
        return words

    def busca_by_prefixo(self, text):
        self.melhor_palavra = None
        self.melhor_tamanho_prefixo = 0
        self._busca_by_prefixo(self.root, "", text)

        return self.melhor_palavra

    def _busca_by_prefixo(self, node, prefix, text):
        if node.is_end_of_word:
            tam_comum = 0
            for i in range(min(len(prefix), len(text))):
                if prefix[i] == text[i]:
                    tam_comum += 1
                else:
                    break
            if tam_comum > self.melhor_tamanho_prefixo:
                self.melhor_tamanho_prefixo = tam_comum
                self.melhor_palavra = prefix

        for char, child_node in node.children.items():
            self._busca_by_prefixo(child_node, prefix + char, text)