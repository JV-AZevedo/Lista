civil_l = ['s', 'c', 'v', 'd']
nome = input('nome: ')
while len(nome) < 4:
    print('nome deve conter no mínimo 4 caracteres')
    nome = input('nome: ')
idade = int(input('idade: '))
while idade < 1 or idade > 150:
    print('idade inválida')
    idade = int(input('idade: '))
salario = float(input('salário: '))
while salario <= 0:
    print('salário inválido')
    salario = float(input('salário: '))
sexo = input('masculino(m) ou feminino(f): ').lower()
while sexo != 'm' and sexo != 'f':
    print('resposta inválida')
    sexo = input('masculino(m) ou feminino(f)')
civil = input('solteiro(s),casado(c),viúvo(v),divorciado(d)').lower()
while civil not in civil_l:
    print('resposta inválida')
    civil = input('solteiro(s),casado(c),viúvo(v),divorciado(d)').lower()