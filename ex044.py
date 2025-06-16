#44) Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os 
#códigos utilizados são: 
 
#1 , 2, 3, 4  - Votos para os respectivos candidatos  
#(você deve montar a tabela ex: 1 - José/ 2- João/etc) 
#5 - Voto Nulo 
#6 - Voto em Branco 

#Faça um programa que calcule e mostre: 
#a) O total de votos para cada candidato; 
#b) O total de votos nulos; 
#c) O total de votos em branco; 
#d) A percentagem de votos nulos sobre o total de votos; 
#e) A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o 
#valor zero.

c1 = c2 = c3 = c4 = n = b = 0
r = 1
l = []
while True:
    v = int(input("eleitor número "+str(r)+", em qual candidado você quer votar?(1 - João, 2 - Vitor, 3 - Jean, 4 - Bolsonaro, 5 - Nulo, 6 - Branco): "))
    r+=1
    if v == 1:
        c1+=1
    elif v == 2:
        c2+=1
    elif v == 3:
        c3+=1
    elif v == 4:
        c4+=1
    elif v == 5:
        n+=1
    elif v == 6:
        b+=1
    if v == 0:
        break
    l.append(v)
pn = (n/r)*100
pb = (b/r)*100
print("João: ",c1,"voto(s), Vitor: ",c2,"voto(s), Jean: ",c3,"voto(s), Bolsonaro:",c4,"voto(s), Nulo:",n,"voto(s), Branco:",b,"voto(s).")
print(f"Porcentagem de votos nulos: {pn:.2f}%, porcentagem de votos brancos: {pb:.2f}%")