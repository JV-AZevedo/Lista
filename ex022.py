#22) Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível. 
n = int(input("escreva o número: "))
p = 1
d = []
if n == 1 or n == 0:
    print("o número: ",n,"não é primo")
while p <= n:
    if n % p == 0:
        d.append(p)        
        p+=1
    else:
        p+=1
if len(d) == 2:
    print("o número: ",n,"é primo, divisível por: ",d)
elif len(d)!=2 and n!=0 and n!= 1:
    print("o número: ",n,"não é primo, divisível por: ",d)