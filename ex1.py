#1)Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

n = float(input("qual foi sua nota?: "))
while n > 10 or n < 0:
    print("resposta inválida")
    n = float(input("qual foi sua nota?: "))