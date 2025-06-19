#65) Dada uma string e dois índices (início e fim), extraia e imprima a substring que começa no índice inicio e 
#termina antes do índice fim. Lide com casos onde os índices podem estar fora dos limites da string (ajuste-os 
#para o início/fim da string). 
#texto_completo = "Programação em Python" 
#indice_inicio = 4 
#indice_fim = 12 
# Saída esperada: "amacao " 
#texto_completo_2 = "ABCDE" 
#indice_inicio_2 = 1 
#indice_fim_2 = 10 # Fora do limite 
# Saída esperada: "BCDE"

t = input("texto: ")
i = int(input("início: "))
f = int(input("fim: "))
t2 = []
if f > len(t):
    f = len(t)
for j in range(i,f):
    t2.append(t[j])
print("".join(t2))
