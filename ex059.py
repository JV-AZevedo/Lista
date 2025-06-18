#59) Dada uma string, conte e imprima o número de vogais (a, e, i, o, u, ignorando maiúsculas/minúsculas) e o 
#número de consoantes.

def texto(tex):
    v = 0
    c = 0
    for i in range(len(tex)):
        if tex[i] in "aeiou":
            v+=1
        else:
            c+=1
    return 'vogais: ',v, 'consoantes: ' ,c
tex = input("escreva o texto: ").lower()
print(texto(tex))
        
        