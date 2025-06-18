#60) Dada uma string, crie e imprima uma nova string que seja a versão invertida da original. 
#Exemplo: 
#frase = "Python é divertido" 
# Saída esperada: "oditrevíd é nohtyP" 

n = input("texto para inverter: ")
l = []
for i in range(len(n)):
    l.append(n[len(n)-1-i])
print("".join(l))