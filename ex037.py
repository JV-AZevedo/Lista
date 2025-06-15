#37) Uma academia deseja fazer um censo entre seus clientes para descobrir o mais alto, o mais baixo, o mais 
#gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da 
#academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário 
#digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores 
#do cliente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos 
#clientes 

c = 1
alto = 0
baixo = 1000
gordo = 0
magro = 1000
sh = 0
sp = 0
lc = []
lha = [0,0,0]
lhb = [0,0,0]
lpg = [0,0,0]
lpm = [0,0,0]
while True:
    c = int(input("seu código: "))
    if c == 0:
        break
    h = float(input("sua altura(cm): "))
    p = float(input("seu peso(kg): "))
    lc.append(c)
    sh +=h
    sp +=p
    if h > alto:
        alto = h
        lha = c,alto,p
    if h < baixo:
        baixo = h
        lhb = c,baixo,p
    if p > gordo:
        gordo = p
        lpg = c,h,gordo
    if p < magro:
        magro = p
        lpm = c,h,magro
mh = sh/len(lc)
mp = sp/len(lc)
print("mais alto, código:",lha[0],"altura:",lha[1],"peso:",lha[2])
print("mais baixo, código:",lhb[0],"altura:",lhb[1],"peso:",lhb[2])
print("mais gordo, código:",lpg[0],"altura:",lpg[1],"peso:",lpg[2])
print("mais magro, código:",lpm[0],"altura:",lpm[1],"peso:",lpm[2])
print("média de altura:",mh,"média de peso:",mp)

    
