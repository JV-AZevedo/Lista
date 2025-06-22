#70) Crie uma função gerar_senha(comprimento, incluir_numeros=True, incluir_simbolos=False) que gere uma senha aleatória. A função deve ter um parâmetro obrigatório 
#comprimento (inteiro) e dois parâmetros opcionais booleanos. 
#● Se incluir_numeros for True, a senha pode conter dígitos (0-9). 
#● Se incluir_simbolos for True, a senha pode conter caracteres especiais (!@#$%^&*). 
#● A senha sempre deve conter letras (maiúsculas e minúsculas). 
#● Retorne a senha gerada. 
#Dica: Use o módulo random e string para caracteres.

import random
import string
def gerar_senha(c, n=True, s=False):
    carac = string.ascii_letters
    if n == True:
        carac+=string.digits
    if s == True:
        carac+="!@#$%*"
    senha = "".join(random.choice(carac) for _ in range(c))
    return senha
c = int(input("comprimento: "))
n = input("incluir numeros?(S/N): ").lower()
if n == "s":
     n = True
else:
    n = False
s = input("incluir simbolos?(S/N): ").lower()
if s == "s":
    s = True
else:
    s = False    
print(gerar_senha(c,n,s))

