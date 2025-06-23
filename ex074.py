#74) Crie uma função calcular_fatorial(numero) que receba um número inteiro não negativo e retorne 
#seu fatorial. Tente implementar uma versão recursiva e uma iterativa (opcional, mas bom para prática). Se o 
#número for negativo, retorna uma mensagem de erro. 

def cal_fatorial(x):
    r = x
    if x == 0:
        return 1
    elif x != 0:
        while r != 1:
                r-=1
                x*=r
        return x
    else:
         return "valor inválido"
x = int(input("quer o fatorial de qual número?: "))
print(cal_fatorial(x))