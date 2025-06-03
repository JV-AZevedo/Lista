a = int(input("populção de A: "))
ta = float(input("taxa de crescimento de A(sem simbolo de %): "))
b = int(input("populção de B: "))
tb = float(input("taxa de crescimento de B(sem simbolo de %): "))
ta = ta/100 +1
tb = tb/100 +1
ano = 0
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