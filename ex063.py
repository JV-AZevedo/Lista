#63) Dada uma string contendo várias palavras separadas por espaços, conte e imprima o número de palavras. 

t = input("texto: ")
s=0
tl = " ".join(t.split())
for i in range(len(tl)):
    if tl[i] == " ":
        s+=1
print(s+1)