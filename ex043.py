#43) O cardápio de uma lanchonete é o seguinte: 
 
#Especificação   Código  Preço 
#Cachorro Quente 100     R$ 1,20 
#Bauru Simples   101     R$ 1,30 
#Bauru com ovo   102     R$ 1,50 
#Hambúrguer      103     R$ 1,20 
#Cheeseburguer   104     R$ 1,30 
#Refrigerante    105     R$ 1,00 
 
#Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a 
#ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar 
#quando o pedido deve ser encerrado.

p=0
while True:
    c = int(input("código do pedido: "))
    q = int(input("quantidade do pedido "+str(c)+": "))
    f = input("encerrar pedido?(S/N) ").upper()
    if c == 100 or c == 103:
        p+= 1.2*q
    elif c == 101 or c == 104:
        p+= 1.3*q
    elif c == 102:
        p+= 1.5*q
    elif c == 105:
        p+= 1*q
    if f == "S":
        break
print(f"total do pedido: {p:.2f}")