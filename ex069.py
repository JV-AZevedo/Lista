#69) Crie uma função contar_palavras(lista_de_frases) que receba uma lista de strings (frases). A 
#função deve retornar um dicionário onde as chaves são as palavras (em minúsculas) e os valores são o número 
#de vezes que cada palavra aparece em todas as frases. Ignore pontuações e trate múltiplas palavras separadas 
#por espaços. 

from collections import Counter
def contador(l):
    dc = Counter(l)
    print(dc)
l = input('texto: ').split()
contador(l)