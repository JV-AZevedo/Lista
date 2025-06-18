#62) Dada uma string, verifique se ela é um palíndromo (lê-se da mesma forma de trás para frente, ignorando 
#maiúsculas/minúsculas e espaços). Imprima True ou False. 
#palavra1 = "arara" # True 
#palavra2 = "Ame a ema" # True 
#palavra3 = "Python" # False 

n = input("texto para inverter: ")
l = []
for i in range(len(n)):
    l.append(n[len(n)-1-i])
if "".join(l) == "".join(n):
    print("True")
else:
    print("False")