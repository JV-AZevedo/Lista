#36) Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, 
#mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser 
#informados também pelo usuário, conforme exemplo abaixo: 
 
#Montar a tabuada de: 5 
#Começar por: 4 
#Terminar em: 7 
 
#Vou montar a tabuada de 5 começando em 4 e terminando em 7: 
#5 X 4 = 20 
#5 X 5 = 25 
#5 X 6 = 30 
#5 X 7 = 35 
 
#Obs: Você deve verificar se o usuário não digitou o final menor que o inicial. 

while True:
    n = int(input('escreva o número que você quer a tabuada: '))
    i = int(input("começar a tabuada por: "))
    f = int(input("finalizar a tabuada em: "))
    x = 0
    if i < f:
        print("Vou montar a tabuada de "+str(n)+" começando em "+str(i)+" e terminando em "+str(f)+": ")
        for i in range(i,f+1):
            x = n*i
            print(n, "X",i, "=" ,x)
        break
    else:
        print("valores inválidos")