#53) Dada uma matriz e um elemento específico, conte e imprima quantas vezes esse elemento aparece na matriz.

matriz = [[1, 1, 1],[1, 2, 1],[1, 2, 2]]
n = 0
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if matriz[i][j] == 1:
            n+=1
print("1 aparece",n,"vezes")