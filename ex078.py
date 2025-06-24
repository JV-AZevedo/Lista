#78) Crie uma função contar_linhas(nome_arquivo) que receba o nome de um arquivo de texto e 
#retorne o número total de linhas que ele contém. Se o arquivo não existir, a função deve retornar 0 e imprimir 
#uma mensagem de erro. 

def contar_linhas(arq):
    f = open(arq, 'r', encoding='utf-8')
    c = 0
    for _ in f:
        c += 1
    f.close()
    return c
print(contar_linhas("ndados.txt"))