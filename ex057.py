#57) Dada uma matriz, determine e imprima se ela é uma matriz quadrada (o número de linhas é igual ao número 
#de colunas) e se todas as linhas têm o mesmo número de colunas. Imprima True ou False. 

m = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
q = True
linhas = len(m)
if linhas == 0:
    q = False
else:
    for i in m:
        if len(i) != linhas:
            q = False
            break
print(q)