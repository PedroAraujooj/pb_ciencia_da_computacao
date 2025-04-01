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

    def show_hierarchy(self):
        def dfs(char, node, depth):
            if char is not None:
                print("   " * depth + f"{char}")
            for c, child in node.children.items():
                dfs(c, child, depth + 1)

        for c, child_node in self.root.children.items():
            dfs(c, child_node, 0)

    def busca_by_prefixo(self, prefixo):

        node = self.root
        for char in prefixo:
            if char not in node.children:
                return []
            node = node.children[char]
        palavras = []
        self._busca_by_prefixo(node, prefixo, palavras)
        return palavras

    def _busca_by_prefixo(self, current_node, palavra_formada, palavras):
        if current_node.is_end_of_word:
            palavras.append(palavra_formada)
        for ch, child_node in current_node.children.items():
            self._busca_by_prefixo(child_node, palavra_formada + ch, palavras)
