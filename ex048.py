#48) Faça um programa que peça um número inteiro positivo e em seguida mostre este número invertido. 
#Exemplo: 
#12376489 
#=> 98467321 

n = input("número para inverter: ")
l = []
for i in range(len(n)):
    l.append(n[len(n)-1-i])
print("".join(l))