#31) O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de 
#conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá 
#receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser 
#informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e 
#perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta 
#operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser 
#conforme o exemplo abaixo: 
#Lojas Tabajara  
#Produto 1: R$ 2.20 
#Produto 2: R$ 5.80 
#Produto 3: R$ 0 
#Total: R$ 9.00 ##(na verdade o total desse exemplo fica 8, professor errou o calculo)
#Dinheiro: R$ 20.00 
#Troco: R$ 11.00 

while True:
    x = 1
    p = 1
    l = []
    t = 0
    y = 1
    z = 0
    while p != "0":
        p = (input("valor do produto "+str(x)+": "))
        x+=1
        l.append(p)
        t+=float(p)
    print(f"Valor total: R$ {t:.2f}")
    d = float(input("valor recebido pelo cliente: "))
    print("Lojas Tabajara")
    for i in range(1,x):
        for j in range(y):
            print("Produto "+str(i)+": R$",l[z])      
            z+=1
    print(f"Total: R$ {t:.2f}")
    print(f"Dinheiro: R$ {d:.2f}")
    print(f"Troco: R$ {d-t:.2f}")
    n = input("próxima compra?(S/N): ").upper()
    if n == "N":
        break
