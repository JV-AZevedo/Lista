#19) Altere o programa anterior para que ele aceite apenas números entre 0 e 1000. 

n = int(input("quantidade de números: "))
menor = None
maior = None
x=0
s = 0
for i in range(n):
    while True:
        x = int(input("escreva um dos valores(entre 0 e 1000) e de enter: "))
        if x>=0 and x<=1000:
            break
        else:
            print("valor inválido")
    s += x
    if i == 0:
        menor = x
        maior = x
    else:
        if x>maior:
            maior = x
        elif x<menor:
            menor = x
        else:
            print("valor inválido")
print("soma: ",s,"maior: ",maior,"menor: ",menor)