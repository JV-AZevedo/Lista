#58) Dada uma matriz, crie e imprima uma nova matriz onde a ordem das linhas foi invertida. A primeira linha se 
#torna a última, a segunda se torna a penúltima, e assim por diante. Os elementos dentro de cada linha devem 
#permanecer na mesma ordem. 

m = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
mm = m[::-1]
for l in mm:
    print(l)