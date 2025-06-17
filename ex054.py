#54) Dada uma matriz, crie e imprima uma nova matriz que seja a transposta da matriz original. A transposta de 
#uma matriz é obtida trocando suas linhas por colunas. 

matriz = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
r = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(matriz)):
    for j in range(len(matriz)):
       r[i][j] = matriz[j][i]

print(r)