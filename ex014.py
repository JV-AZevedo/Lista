#14) Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a 
#quantidade de números ímpares. 
p = 0
i = 0
for j in range(10):
    n = int(input("escreva um dos valores e de enter: "))
    if n % 2 == 0:
        p+=1
    else:
        i+=1
print("quantida de números pares: ",p,"quantidade de ímpares: ",i)