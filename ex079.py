#79) Crie uma função ler_e_imprimir(nome_arquivo) que receba o nome de um arquivo de texto e 
#imprima todo o seu conteúdo no console. Se o arquivo não existir, a função deve imprimir uma mensagem de 
#erro. 

def contar_linhas(arq):
    f = open(arq, 'r', encoding='utf-8')
    c = f.read()
    f.close()
    return c
print(contar_linhas("ndados.txt"))