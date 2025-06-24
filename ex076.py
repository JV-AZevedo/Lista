#76) Crie uma função desenhar_triangulo(altura, tipo) que receba uma altura (inteiro positivo) e 
#uma string tipo ('esquerda', 'direita', 'centralizado'). A função deve imprimir um triângulo de asteriscos (*) 
#com a base na parte inferior, alinhado de acordo com o tipo. A função não retorna nada, apenas imprime. 

def des_triangulo(h, t):
    for i in range(1, h + 1):
        if t == 'e':
            l = '*' * i
        elif t == 'd':
            l = ' ' * (h - i) + '*' * i
        else:  
            esp = h - i
            l = ' ' * esp + '*' * (2 * i - 1)
        print(l)
h = int(input("altura: "))
t = input("tipo: esquerda(e), direita(d), centralizado(c): ")
des_triangulo(h,t)