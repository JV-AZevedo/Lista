#41) Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da 
#dívida, valor dos juros, quantidade de parcelas e valor da parcela. 
#Os juros e a quantidade de parcelas seguem a tabela abaixo: 
 
#Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida 
#1       0 
#3       10 
#6       15 
#9       20 
#12      25 
 
#Exemplo de saída do programa: 
 
#Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela 
#R$ 1.000,00     0               1                       R$  1.000,00 
#R$ 1.100,00     100             3                       R$    366,00 
#R$ 1.150,00     150             6                       R$    191,67 

vjuros = 0
vparce = 0
v=float(input("valor da dívida: "))

print("Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela")
print(f"R$ {v:.2f}","     0                1                     ",v)
vjuros = v*0.1
vparce = (v+(vjuros*3))/3
print(f"R$ {v:.2f}      {vjuros:.2f}           3                      {vparce:.2f}")
vjuros = v*0.15
vparce = (v+(vjuros*6))/6
print(f"R$ {v:.2f}      {vjuros:.2f}           6                      {vparce:.2f}")
vjuros = v*0.20
vparce = (v+(vjuros*9))/9
print(f"R$ {v:.2f}      {vjuros:.2f}           9                      {vparce:.2f}")
vjuros = v*0.25
vparce = (v+(vjuros*12))/12
print(f"R$ {v:.2f}      {vjuros:.2f}           12                     {vparce:.2f}")

    

