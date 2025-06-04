#11)Altere o programa anterior para mostrar no final a soma dos números.

n1 = int(input("escreva o primeiro número: "))
n2 = int(input("escreva o segundo número: "))
s = 0
if n1 > n2:
    for i in range(n2+1,n1):
        s+= i
        print(i)
elif n2 > n1:
    for i in range(n1+1,n2):
        s+= i
        print(i)
print("soma: ",s)