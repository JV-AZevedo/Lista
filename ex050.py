#50) Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com 
#N termos. 

n = int(input("quantidade de termos: "))
x = 2
lx = []
r = 1
for i in range(n):
    lx.append(x)
    r+=1/x
    x+=1
print("resultado da soma:",r)