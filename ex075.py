#75) Crie uma função sao_anagramas(palavra1, palavra2) que receba duas strings e retorna True se 
#elas forem anagramas (contêm as mesmas letras, na mesma quantidade, mas em ordem diferente), e False 
#caso contrário. Ignore maiúsculas/minúsculas e espaços. 

def sao_anagramas(p1, p2):
    p1 = p1.replace(" ", "").lower()
    p2 = p2.replace(" ", "").lower()
    if len(p1) != len(p2):
        return False
    return sorted(p1) == sorted(p2)
p1 = input("palavra um: ")
p2 = input("palavra dois: ")
print(sao_anagramas(p1,p2))