#73) Crie uma função filtrar_numeros(lista, tipo) que receba uma lista de números e uma string 
#tipo ('pares', 'impares', 'positivos', 'negativos'). A função deve retornar uma nova lista contendo apenas os 
#números que correspondem ao tipo especificado. Se o tipo for inválido, retorna uma lista vazia. 

def filtro(l,t):
    l2 = []
    for j in range(len(l)):
        if t == "p":
            if float(l[j]) % 2 == 0:
                l2.append(l[j])
        elif t == "i":
            if float(l[j]) % 2 != 0:
                l2.append(l[j])
        elif t == "+":
            if float((l[j])) > 0:
                l2.append(l[j])
        elif t == "-":
            if float((l[j])) < 0:
                l2.append(l[j])
        else:
            return "unidade inválida"
    return l2
l = input("lista de números separados por espaço: ").split()
t = input("apenas tipo: pares(p), impares(i), positivos(+), negativos(-) ").lower()
print(filtro(l,t))