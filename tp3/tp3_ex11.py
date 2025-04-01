from tp3.ArvoreBinaria import BinaryTree

if __name__ == "__main__":
    bst = BinaryTree()

    bst.add(50)
    bst.add(30)
    bst.add(70)
    bst.add(20)
    bst.add(40)
    bst.add(60)
    bst.add(80)

    print(f'In-order: {bst.inorder()}')
    print(f'Pre-order: {bst.preorder()}')
    print(f'Pos-order: {bst.postorder()}')