#24) Faça um programa que calcule e mostre a média aritmética de N notas.

q = int(input("quantos números você quer calcular?: "))
s = 0
for i in range(q):
    x = float(input("escreva um dos valores e de enter: "))
    s += x
m = s/q
print("média:",m)