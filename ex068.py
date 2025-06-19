#68) Crie uma função calculadora(num1, num2, operacao) que receba dois números e uma string 
#operacao ('soma', 'subtracao', 'multiplicacao', 'divisao'). A função deve retornar o resultado da operação 
#correspondente. Se a operação for inválida ou se tentar dividir por zero, retorne uma mensagem de erro 
#adequada. 

def cal(n1,n2,op):
    if op == "s":
        r = n1+n2
    elif op == "sub":
        r = n1 - n2
    elif op == "m":
        r = n1*n2
    elif op == "d":
        if n2 == 0:
            return "operação inválida"
        else:
            r = n1/n2
    else:
        return "operação inválida"
    return r
n1 = float(input("número 1: "))
n2 = float(input("número 2: "))
op = input("operação(soma(s),subtração(sub),multiplicação(m),divisão(d): ").lower()
print(cal(n1,n2,op))