#13) Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao 
#segundo número. Não utilize a função de potência da linguagem.

b = int(input("qual a base?: "))
e = int(input("qual o expoente?: "))
r = 1
for i in range(e):
    r*=b
print(r)