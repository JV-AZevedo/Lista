#33) O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um 
#conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem 
#como a média das temperaturas.

n = int(input("quantidade de temperaturas: "))
menor = None
maior = None
s = 0
for i in range(n):
    x = int(input("escreva uma das temperaturas e de enter: "))
    s += x
    if i == 0:
        menor = x
        maior = x
    else:
        if x>maior:
            maior = x
        elif x<menor:
            menor = x
m = s/n
print("média: ",m,"maior: ",maior,"menor: ",menor)