#72) Crie uma função converter_temperatura(valor, unidade_origem, unidade_destino) que converte um valor de temperatura entre Celsius ('C'), Fahrenheit ('F') e Kelvin 
#('K'). A função deve retornar o valor convertido. Se as unidades estiverem inválidas, retorne uma mensagem de erro. 
#Fórmulas: 
#Celsius para Fahrenheit: F = C * 1.8 + 32 
#Fahrenheit para Celsius: C = (F - 32) / 1.8 
#Celsius para Kelvin: K = C + 273.15 
#Kelvin para Celsius: C = K - 273.15 
#Fahrenheit para Kelvin: K = (F - 32) / 1.8 + 273.15 
#Kelvin para Fahrenheit: F = (K - 273.15) * 1.8 + 32 

def cal(t,ui,uf):
    if ui == "c" and uf == "f":
        r = t*1.8+32
    elif ui == "f" and uf == "c":
        r = (t - 32) / 1.8
    elif ui == "c" and uf == "k":
        r = t + 273.15
    elif ui == "k" and uf == "c":
        r = t - 273.15
    elif ui == "f" and uf == "k":
        r = (t - 32) / 1.8 + 273.15
    elif ui == "k" and uf == "f":
        r = (t - 273.15) * 1.8 + 32
    else:
        return "unidade inválida"
    return r
t = float(input("temperatura: "))
ui = input("unidade de origem(C/F/K): ").lower()
uf = input("unidade de destino(C/F/K): ").lower()

print(cal(t,ui,uf))