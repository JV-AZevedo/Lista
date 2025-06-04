#2)Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

u = input('nome de usuário: ')
s = input('senha: ')
while u == s:
    print('senha nao pode ser igual ao nome de usuario')
    s = input('senha: ')
