#52) Dada uma matriz quadrada (o número de linhas é igual ao número de colunas), calcule e imprima a soma dos 
#elementos da diagonal principal e a soma dos elementos da diagonal secundária.

matriz = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
dgp = 0
dgs = 0
for i in range(len(matriz)):
        dgp += matriz[i][i]
        dgs += matriz[i][len(matriz)-1-i]
print("soma diagonal principal:",dgp,"soma diagonal secundária:",dgs)
