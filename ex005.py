#5)Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
#Valide a entrada e permita repetir a operação. 

a = int(input("populção de A: "))
ta = float(input("taxa de crescimento de A(sem simbolo de %): "))
b = int(input("populção de B: "))
tb = float(input("taxa de crescimento de B(sem simbolo de %): "))
ta = ta/100 +1
tb = tb/100 +1
ano = 0
while a>b and ta >= tb or b>a and tb>=ta:
    print("valores inválidos")
    a = int(input("populção de A: "))
    ta = float(input("taxa de crescimento de A(sem simbolo de %): "))
    b = int(input("populção de B: "))
    tb = float(input("taxa de crescimento de B(sem simbolo de %): "))
if a>b:
    while b<=a:
        a*=ta
        b*=tb
        ano+=1
    print("o tempo necessario para B passar A é de: ",ano,"anos")
if b>a:
    while a<=b:
        a*=ta
        b*=tb
        ano+=1
    print("o tempo necessario para A passar B é de: ",ano,"anos")