#45) Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve 
#perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o 
#total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita 
#uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar: 
#a) Maior e Menor Acerto; 
#b) Total de Alunos que utilizaram o sistema; 
#c) A Média das Notas da Turma. 
#Gabarito da Prova: 
#01 - A 
#02 - B 
#03 - C 
#04 - D 
#05 - E 
#06 - E 
#07 - D 
#08 - C 
#09 - B 
#10 - A 
#Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova 
#antes dos alunos usarem o programa.

questao = ["01","02","03","04","05","06","07","08","09","10"]
resposta = ["A","B","C","D","E","E","D","C","B","A"]
maiornota = 0
menornota = 11
snotas =0
ma = 0
while True:
    nota = 0
    ma+=1
    for i in range(10):
        r = input("resposta da questão "+str(questao[i])+": ").upper()
        if r == resposta[i]:
            nota+=1
    print(nota)
    snotas+=nota
    mnotas = snotas/ma
    if nota> maiornota:
        maiornota = nota
    elif nota<menornota:
        menornota = nota
    p = input("próximo aluno?(S/N): ").upper()
    if p == "N":
        break
print("média da turma:",mnotas,"menor nota:",menornota,"maior nota:",maiornota)