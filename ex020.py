#20) Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o 
#fatorial a números inteiros positivos e menores que 16. 

while True:
    n = int(input("você quer o fatorial de qual número?(apenas inteiros positivos menores que 16): "))
    r = n
    if n < 0 or n > 16:
        print("valor inválido")
    if n == 0:
        print(1)
    elif n >= 0 and n <= 16:
        while r != 1:
            r-=1
            n*=r
        print(n)
    d = input("quer fatorar outro número?(S/N): ").upper()
    if d == "S":
            print("ok")
    else:
        break