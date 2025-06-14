#26) Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada 
#eleitor votar e ao final mostrar o número de votos de cada candidato. 

c1 = 0
c2 = 0
c3 = 0
e = int(input("número total de eleitores: "))
for i in range(1,e+1):
    v = int(input("eleitor número "+str(i)+", em qual candidado você quer votar?(1, 2 ou 3): "))
    if v == 1:
        c1+=1
    elif v == 2:
        c2+=1
    elif v == 3:
        c3+=1
print("candidato 1: ",c1,"voto(s), candidato 2: ",c2,"voto(s), candidato 3: ",c3,"voto(s).")