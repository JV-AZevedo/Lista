#10)Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo 
#compreendido por eles.

n1 = int(input("escreva o primeiro número: "))
n2 = int(input("escreva o segundo número: "))
if n1 > n2:
    for i in range(n2+1,n1):
        print(i)
elif n2 > n1:
    for i in range(n1+1,n2):
        print(i)