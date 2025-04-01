import concurrent.futures


def _get_max_value_seq(node):
    if node is None:
        return float('-inf')
    left_max = _get_max_value_seq(node.left)
    right_max = _get_max_value_seq(node.right)
    return max(node.value, left_max, right_max)

def _dfs_seq(node, target):
    if node is None:
        return None
    if node.value == target:
        return [node]

    esq = _dfs_seq(node.left, target)
    if esq is not None:
        return [node] + esq

    dire = _dfs_seq(node.right, target)
    if dire is not None:
        return [node] + dire

    return None


def _sequencial_search(node, value):
    if node is None:
        return False
    if node.value == value:
        return True
    return _sequencial_search(node.left, value) or _sequencial_search(node.right, value)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.value})"


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(self.root, value)

    def _add(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._add(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._add(current.right, value)

    def search(self, value):

        return self._search(self.root, value)

    def _search(self, current, value):

        if current is None:
            return False
        if current.value == value:
            return True
        if value < current.value:
            return self._search(current.left, value)
        else:
            return self._search(current.right, value)

    def getNode(self, value):

        return self._getNode(self.root, value)

    def _getNode(self, current, value):

        if current is None:
            return None
        if current.value == value:
            return current
        if value < current.value:
            return self._getNode(current.left, value)
        else:
            return self._getNode(current.right, value)

    def remove(self, value):
        self.root = self._remove(self.root, value)

    def _remove(self, current, value):
        if current is None:
            return current

        if value < current.value:
            current.left = self._remove(current.left, value)
        elif value > current.value:
            current.right = self._remove(current.right, value)
        else:
            if current.left is None and current.right is None:
                return None
            if current.left is None:
                return current.right
            if current.right is None:
                return current.left
            min_larger_node = self._get_min(current.right)
            current.value = min_larger_node.value
            current.right = self._remove(current.right, min_larger_node.value)
        return current

    def _get_min(self, current):
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, current, result):
        if current is not None:
            self._inorder(current.left, result)
            result.append(current.value)
            self._inorder(current.right, result)

    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, current, result):
        if current is not None:
            result.append(current.value)
            self._preorder(current.left, result)
            self._preorder(current.right, result)

    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, current, result):
        if current is not None:
            self._postorder(current.left, result)
            self._postorder(current.right, result)
            result.append(current.value)

    def height(self):
        return self._height(self.root)

    def _height(self, current):

        if current is None:
            return -1
        left_height = self._height(current.left)
        right_height = self._height(current.right)
        return 1 + max(left_height, right_height)

    def get_min_value(self):
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current.value

    def get_max_value(self):
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.value

    def search_paralelo(self, value):
        if self.root is None:
            return False
        if self.root.value == value:
            return True
        with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
            future_left = executor.submit(_sequencial_search, self.root.left, value)
            future_right = executor.submit(_sequencial_search, self.root.right, value)
            return future_left.result() or future_right.result()

    def dsf_paralelo(self, target):
        if self.root is None:
            return None
        if self.root.value == target:
            return [self.root]

        with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
            future_left = executor.submit(_dfs_seq, self.root.left, target)
            future_right = executor.submit(_dfs_seq, self.root.right, target)

            left_path = future_left.result()
            if left_path is not None:
                return [self.root] + left_path

            right_path = future_right.result()
            if right_path is not None:
                return [self.root] + right_path

        return None

    def get_max_value_paralelo(self):
        if self.root is None:
            return None
        with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
            future_left = executor.submit(_get_max_value_seq, self.root.left)
            future_right = executor.submit(_get_max_value_seq, self.root.right)
            left_max = future_left.result()
            right_max = future_right.result()

        return max(self.root.value, left_max, right_max)
