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

    print(f'In-order inicial: {bst.inorder()}')
    bst.remove(20)
    print(f'In-order após remoção do 20: {bst.inorder()}')
    bst.remove(30)
    print(f'In-order após remoção do 30: {bst.inorder()}')
    bst.remove(50)
    print(f'In-order após remoção do 50: {bst.inorder()}')

