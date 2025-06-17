#55) Dada uma matriz de números, encontre e imprima o maior e o menor elemento presentes na matriz. 

matriz = [[4, 5, 3],[1, 6, 9],[7, 8, 2]]
maior = menor = matriz[0][0]
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if matriz[i][j] > maior:
            maior =matriz[i][j]
        if matriz[i][j] < menor:
            menor =matriz[i][j]
print("maior:",maior,"menor:",menor)