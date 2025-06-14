#25) Faça um programa que peça para n pessoas a sua idade, ao final o programa deverá verificar se a média de 
##idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, 
#conforme a média calculada.

q = int(input("quantos pessoas tem na turma?: "))
s = 0
for i in range(q):
    x = float(input("escreva uma das idades e de enter: "))
    s += x
m = s/q
if m <=25:
    print("turma jovem")
elif m >=26 and m <= 60:
    print("turma adulta")
else:
    print("turma idosa")
