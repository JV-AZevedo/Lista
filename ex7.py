#7)Faça um programa que leia 5 números e informe o maior número. 

f = 0
m = 0
while f<5:
    n = float(input("escreva um dos valores e de enter: "))
    if n>m:
        m=n
    f+=1
print(m)
