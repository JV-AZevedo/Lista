#71) Crie uma função validar_email(email) que receba uma string de e-mail e retorne True se o e-mail for 
#considerado válido, True e False caso contrário. 
#Um e-mail válido para este exercício deve: 
#● Conter um único "@" (arroba). 
#● Ter pelo menos um caractere antes do "@". 
#● Ter pelo menos um caractere entre o "@" e o ".". 
#● Ter pelo menos dois caracteres após o ".".

import re
def validar_email(t):
    p = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(p, t) is not None
t = "joao@gmail.com"
print(validar_email(t)) 
        
