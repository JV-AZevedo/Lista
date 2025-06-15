#39) Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o 
#segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o 
#número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

la = []
lha = []
lhb = []
a = 0
b = 1000
for i in range(10):
    aluno = int(input("número do aluno: "))
    la.append(aluno)
for j in range(10):
    h = float(input("altura do aluno "+str(la[j])+": "))
    if h>a:
        a = h
        lha = la[j],a
    if h<b:
        b = h
        lhb = la[j],b
print("mais alto, número:",lha[0],"altura:",lha[1])
print("mais baixo, número:",lhb[0],"altura:",lhb[1])
