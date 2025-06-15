#38) Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que: 
#a) Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00; 
#b) Em 1996 recebeu aumento de 1,5% sobre seu salário inicial; 
#c) A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do 
#ano anterior. Faça um programa que determine o salário atual deste funcionário. Após concluir isto, 
#altere o programa permitindo que o usuário digite o salário inicial do funcionário. 

s = float(input("sálario incial: "))
p = 0.015
s *= 1.015
a = int(input("ano atual: "))
for i in range(1997, a+1):
    p*=2
    s*=(p+1)
print(f"salário atual: {s:.2f}")