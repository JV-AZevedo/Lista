#56) Crie e imprima uma matriz com linhas por colunas preenchida com um padrão simples. Para este exercício, 
#preencha a matriz com o produto dos seus índices (ou seja, elemento[i][j] = i * j).

l = int(input("número de linhas: "))
c = int(input("número de colunas: "))
m = [[0]*c for k in range(l)]
for i in range(l):
    for j in range(c):
        m[i][j] = i*j
print(m)