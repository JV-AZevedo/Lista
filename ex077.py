#77) Crie uma função combinar_listas(*listas) que receba um número variável de listas como 
#argumentos. A função deve retornar uma única lista contendo todos os elementos de todas as listas de entrada, 
#na ordem em que foram passadas. 
#Para os próximos exercícios, crie os seguintes arquivos: 
#dados.txt 
#Linha 1: Olá Mundo  
#Linha 2: Python é poderoso  
#Linha 3: Manipulação de arquivos 
#numeros.txt 
#10  
#25  -5  
#100  
#15 
#nomes.txt 
#Alice  
#Bob  
#Carlos  
#Diana  
#Eduardo 

def combinar_listas(*listas):
    r = []
    for i in listas:
        r.extend(i)
    return r
l1 = [1, 2, 3]
l2 = ['a', 'b']
l3 = ['a', 'b']
print(combinar_listas(l1, l2, l3))