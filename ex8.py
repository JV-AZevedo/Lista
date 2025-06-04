#8)Faça um programa que leia 5 números e informe a soma e a média dos números. 

f = 0
l = []
s = 0
while f<5:
    n = float(input("escreva um dos valores e de enter: "))
    l.append(n)
    f+=1
for i in range(len(l)):
    s += l[i]
    m = s/len(l)
print("soma: ",s,"média: ",m)