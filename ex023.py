#23) Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
#O programa deverá mostrar também o número de divisões que ele executou para encontrar os números 
#primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados. 

n = int(input("escreva um número: "))
d = 0
p = []
for i in range(2,n+1):
    primo = True
    for j in range(2,i):
        d+=1
        if i % j == 0:
            primo = False        
    if primo:
        p.append(i)
print("números primos entre 1 e",n,":",p,", total de divisões executadas: ",d)