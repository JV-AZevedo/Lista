#28) Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor 
#médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para cada um. 

q = int(input("quantidade de CDs: "))
s = 0
for i in range(1,q+1):
    v = float(input("valor do CD "+str(i)+": "))
    s += v
m = s/q
print("média de preço por CD:",m)