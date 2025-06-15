#40) Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram 
#obtidos os seguintes dados: 
#a) Código da cidade; 
#b) Número de veículos de passeio (em 1999); 
#c) Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber: 
#d) Qual o maior e menor índice de acidentes de trânsito e a que cidade pertence; 
#e) Qual a média de veículos nas cinco cidades juntas; 
#f) Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

sv = 0
sa = 0
maior = None
menor = None
lma = []
lme = []
lmac2 = []
for j in range(5):
    c = int(input("código da cidade: "))
    v = int(input("número de veículos: "))
    a = int(input("número de acidentes: "))
    i = v/a
    sv+=v
    if  j == 0:
        maior = i
        menor = i
        lma = lme = (c, i)
    else:
        if i>maior:
            maior = i
            lma = c,i
        if i<menor:
            menor = i
            lme = c,i
        if v<2000:
            sa+=a
            lmac2.append(c)
mv = sv/5
mac2 = sa/len(lmac2)
print("maior indíce de acidentes, código:",lma[0],f"indice de acidentes: {lma[1]:.2f}")
print("menor indíce de acidentes, código:",lme[0],f"indice de acidentes: {lme[1]:.2f}")
print("média de veículos:",mv)
print("média de acidentes em cidade com menos de 2000 veículos:",mac2)
