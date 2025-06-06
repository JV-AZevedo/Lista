#16) A série de Fibonacci é formada pela sequência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série 
#até que o valor seja maior que 500.
n = [0]
f = 1
r =  0
while True:
    if f<=500:
        n.append(f)
        f+=n[r]
        r+=1
    else:
        break
print(n)