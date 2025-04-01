import time
import random

class Estudante:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __str__(self):
        return f"{self.nome} - {self.nota}"

    __repr__ = __str__
def quicksort_estudantes(array):
    if len(array) <= 1:
        return array
    pivot = array[-1]
    menores = [estudante for estudante in array[:-1] if estudante.nota <= pivot.nota]
    maiores = [estudante for estudante in array[:-1] if estudante.nota > pivot.nota]
    return quicksort_estudantes(maiores) + [pivot] + quicksort_estudantes(menores)


if __name__ == "__main__":
    estudantes = [Estudante("Pedro", 8.8),
                  Estudante("Maria", 5.5),
                  Estudante("Agatha", 10.0),
                  Estudante("João", 8.0),
                  Estudante("Mathias", 8.1),
                  Estudante("Matheus", 3.0),
                  Estudante("Marcos", 7.6),
                  Estudante("Lucas", 7.7),
                  Estudante("Anderson", 9.3),
                  Estudante("Larissa", 6.0),
                ]
    print(quicksort_estudantes(estudantes))
