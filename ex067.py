#67) Dadas duas strings, texto e padrao, verifique se padrao é um prefixo (início) de texto e se padrao é um sufixo 
#(final) de texto. Imprima True ou False para cada verificação. 
#texto = "Desenvolvimento Web" 
#padrao_prefixo = "Desen" # True 
#padrao_sufixo = "Web" # True 
#padrao_nao_existe = "mobile" # False para ambos 

t = "Desenvolvimento Web" 
p_p = "Desen"  
p_s = "Web" 
p_n_e = "mobile"
for i in range(5):
    if p_p[i] == t[i]:
        a = True
    else:
        a = False
print(a)
for j in range(3):
    if p_s[j] == t[j+16]:
        b = True
    else:
        b = False
print(b)