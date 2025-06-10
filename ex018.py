#18) Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
n = int(input("quantidade de números: "))
menor = None
maior = None
s = 0
for i in range(n):
    x = int(input("escreva um dos valores e de enter: "))
    s += x
    if i == 0:
        menor = x
        maior = x
    else:
        if x>maior:
            maior = x
        elif x<menor:
            menor = x
print("soma: ",s,"maior: ",maior,"menor: ",menor)