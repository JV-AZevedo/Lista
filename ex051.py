#51) Faça um programa que mostre os n termos da Série a seguir: 
#S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.  
#Imprima no final a soma da série.

n = int(input("quantidade de termos: "))
x = y = 1
lx = []
ly = []
lz = []
lb=["/"]
lm=["+"]
r = 0
for i in range(n):
    lx.append(x)
    ly.append(y)
    lz += str(lx[i]) + str(lb[0]) + str(ly[i]) + str("".join(lm[0]))
    r+=x/y
    x+=1
    y+=2
print("".join(lz))
print("resultado da soma:",r)