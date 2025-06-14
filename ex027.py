#27) Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e 
#a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos. 

t = int(input("quantidade de turmas: "))
s = 0
for i in range(1,t+1):
    while True:
        a = int(input("quantidade de alunos da turma "+str(i)+": "))
        if a>40:
            print("valor inválido")
        else:
            s+=a
            break
m = s/t
print("média de alunos por turma: ",m)
