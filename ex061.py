#61) Dada uma string, crie e imprima uma nova string onde todos os espaços em branco extras (múltiplos espaços 
#entre palavras, espaços no início ou fim) foram removidos, deixando apenas um único espaço entre as 
#palavras. 
#texto_com_espacos = "   Olá   mundo   Python     "
# Saída esperada: "Olá mundo Python" 
# Saída esperada: "Olá mundo Python" 

t = input("texto: ")
tl = " ".join(t.split())
print(tl)
