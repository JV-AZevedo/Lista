#42) Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão 
#nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for 
#lido um número negativo. 

i0 = []
i1 = []
i2 = []
i3 = []
while True:
    n = int(input("escreva um dos valores e de enter: "))
    if n >= 0 and n <=25:
        i0.append(n)
    elif n >= 26 and n <=50:
        i1.append(n)
    elif n >= 51 and n <=75:
        i1.append(n)
    elif n >= 76 and n <=100:
        i1.append(n)
    else:
        break
print("números entre 0-25:",i0,"números entre 26-50:",i1,"números entre 51-75:",i2,"números entre 76-100:",i3)