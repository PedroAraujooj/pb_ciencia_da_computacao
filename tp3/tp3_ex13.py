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

    print(f'Resultado da busca: {bst.search(40)}')
    bst.remove(40)
    print(f'Resultado da busca após remoção do 40: {bst.search(40)}')


