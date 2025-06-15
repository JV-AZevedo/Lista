#32) Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. 
#A saída deve ser conforme o exemplo abaixo: 
#Fatorial de: 5 
#5! =  5 . 4 . 3 . 2 . 1 = 120 

n = int(input("você quer o fatorial de que número?: "))
r = n
l = []
if n == 0:
    print(1)
else:
    while r != 1:
            l.append(str(r))         
            r-=1
            n*=r 
    l.append(str(1))
    t = " . ".join(l)
    print('Fatorial de:',l[0])
    print(l[0]+"! =",t,"=",n)