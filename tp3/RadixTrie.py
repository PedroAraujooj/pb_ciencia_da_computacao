def common_prefix(s1: str, s2: str) -> int:
    i = 0
    while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
        i += 1
    return i

class RadixTrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class RadixTrie:
    def __init__(self):
        self.root = RadixTrieNode()

    def insert(self, word: str):
        node = self.root
        while word:
            for edge, child in list(node.children.items()):
                common_length = common_prefix(edge, word)
                if common_length > 0:
                    if common_length == len(edge):
                        word = word[common_length:]
                        node = child
                        break
                    else:
                        leftover_edge = edge[common_length:]
                        leftover_word = word[common_length:]
                        intermediate = RadixTrieNode()
                        intermediate.children[leftover_edge] = child
                        del node.children[edge]
                        node.children[edge[:common_length]] = intermediate
                        if leftover_word:
                            new_node = RadixTrieNode()
                            new_node.is_word = True
                            intermediate.children[leftover_word] = new_node
                        else:
                            intermediate.is_word = True
                        return
            else:
                new_node = RadixTrieNode()
                new_node.is_word = True
                node.children[word] = new_node
                return
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root
        while word:
            found = False
            for edge, child in node.children.items():
                if word.startswith(edge):
                    word = word[len(edge):]
                    node = child
                    found = True
                    break
            if not found:
                return False
        return node.is_word

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        while prefix:
            found = False
            for edge, child in node.children.items():
                if prefix.startswith(edge):
                    prefix = prefix[len(edge):]
                    node = child
                    found = True
                    break
                elif edge.startswith(prefix):
                    return True
            if not found:
                return False
        return True

    def _collect_words(self, node: RadixTrieNode, prefix: str) -> list:
        words = []
        if node.is_word:
            words.append(prefix)
        for edge, child in node.children.items():
            words.extend(self._collect_words(child, prefix + edge))
        return words

    def busca_by_prefixo(self, address: str) -> str:
        words = self._collect_words(self.root, "")
        best_word = ""
        best_common = 0
        for w in words:
            cp = common_prefix(w, address)
            if cp > best_common:
                best_common = cp
                best_word = w
        return best_word

    def list_words(self):

        def _dfs(node, prefix, words):
            if node.is_word:
                words.append(prefix)
            for char, child in node.children.items():
                _dfs(child, prefix + char, words)

        words = []
        _dfs(self.root, "", words)
        return words
        pass

