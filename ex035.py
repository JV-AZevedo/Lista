#35) Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos 
#existentes entre 1 e um número inteiro informado pelo usuário. 

n = int(input("escreva um número: "))
p = []
for i in range(2,n+1):
    primo = True
    for j in range(2,i):
        if i % j == 0:
            primo = False        
    if primo:
        p.append(i)
print("números primos entre 1 e",n,":",p)