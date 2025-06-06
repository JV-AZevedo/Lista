#17) Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120 

n = int(input("você quer o fatorial de que número?: "))
r = n
if n == 0:
    print(1)
else:
    while r != 1:
            r-=1
            n*=r
    print(n)