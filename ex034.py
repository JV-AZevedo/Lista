#34) Os números primos possuem várias aplicações dentro da Computação, por exemplo na criptografia. Um 
#número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um 
#número inteiro e determine se ele é ou não um número primo. 

n = int(input("escreva o número: "))
p = 1
if n == 1 or n == 0:
    print("o número: ",n,"não é primo")
while p <= n:
    if n % p == 0 and p != n and p != 1:
        print("o número: ",n,"não é primo")
        break
    else:
        p+=1
    if n == p:
        print("o número: ",n,"é primo")