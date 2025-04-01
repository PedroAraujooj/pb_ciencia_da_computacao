from tp3.ArvoreBinaria import BinaryTree


def valida_bst(bst):
    return _valida_bst(bst.root, float('-inf'), float('inf'))


def _valida_bst(node, min, max):
    if node is None:
        return True
    if not (min < node.value and node.value < max):
        return False
    return (_valida_bst(node.left, min, node.value) and
            _valida_bst(node.right, node.value, max))


if __name__ == "__main__":
    bst = BinaryTree()

    bst.add(50)
    bst.add(30)
    bst.add(70)
    bst.add(20)
    bst.add(40)
    bst.add(60)
    bst.add(80)

    print(f'Resultado da validacao: {valida_bst(bst)}')
    bst.getNode(80).value = 10
    print(f'Resultado da validacao após quebra: {valida_bst(bst)}')
