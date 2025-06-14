#15) A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a 
#série até o n−ésimo termo. 

t = int(input("quantos termos da série de fibonacci você quer?: "))
n = [0]
f = 1
r =  0
while r<t:
    n.append(f)
    f+=n[r]
    r+=1
n.remove(0)
print(n)
