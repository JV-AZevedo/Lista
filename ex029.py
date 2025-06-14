#29) O Sr. Manoel Joaquim possui uma grande loja de artigos de R$1,99, com cerca de 10 caixas. Para agilizar o 
#cálculo de quanto cada cliente deve pagar, ele desenvolveu uma tabela que contém o número de itens que o 
#cliente comprou e o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o 
#cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver o programa que monta 
#esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo: 
#Lojas Quase Dois - Tabela de preços 
#1 - R$ 1.99 
#2 - R$ 3.98 
#... 
#50 - R$ 99.50 

p = 1
x = 1
pr= 1.99
print("Lojas Quase Dois - Tabela de preços")
while p<=50:
    print(p,f"- {pr*x:.2f}")
    p+=1
    x+=1