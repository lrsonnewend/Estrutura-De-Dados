#Paulo Henrique da Silva
#Lucas Ribeiro Sonnewend
#3 Semestre Turma B 2019

def enumerações(items):
    n = len(items)
    s = [0]*(n+1)
    k = 0
    while True:
        if s[k] < n:
            s[k+1] = s[k] + 1
            k += 1
        else:
            s[k-1] += 1
            k -= 1
        if k == 0: break
        else:
            lista = []
            for j in range(1, k+1):
                lista.append(items[s[j]-1])
            yield lista
 
def combinações(items, n):
    if n==0: yield []
    else:
        for i in range(len(items)):
            for cc in combinações(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc
 
def permutações(items):
    return combinações(items, len(items))
 

     
for p in permutações(['Adriano','Bruno', 'Diogo', 'Eclis', 'Gabriel', 'Leandro', 'Walber']):
    pass
 



#a)
'''qtdDamas = 0
casamento = open('casamento.txt')

casamento = casamento.read()
casamento = casamento.split('\n')
aux = []
for p in permutações(['Adriano','Bruno', 'Diogo', 'Eclis', 'Gabriel', 'Leandro', 'Walber']):
    aux = ['Adriano','Bruno', 'Diogo', 'Eclis', 'Gabriel', 'Leandro', 'Walber']
    qtdDamas = 0
    for s in range(len( casamento)):
        s1 =(casamento[s])
        s1 = s1.split()
        dama = s1[:1]
        cavaDela = s1[1:]
        for x in cavaDela:
            if x in aux:
                aux.remove(x)
                qtdDamas +=1
                break
            else:
                continue
    if qtdDamas == len(casamento):
        print('Todas Casaram')
        break
    else:
        continue
if qtdDamas < len(casamento):
    print('Algumas não casaram')
    '''
#B)

cavaleirosAmigo = open('cavaleiros.txt')

cavaleirosAmigo = cavaleirosAmigo.read()

cavaleirosAmigo = cavaleirosAmigo.split('\n')
   
cavaleirosTotal = []
cavaleirosTotal = ['Adriano','Bruno', 'Diogo', 'Eclis', 'Gabriel', 'Leandro', 'Walber']

for p in permutações(cavaleirosTotal):
    formou = 0
    cavaleirosTotal = p
    for x in range(len(cavaleirosTotal)):        
        for y in range(len(cavaleirosAmigo)):
            posAmigo = cavaleirosAmigo[y]
            posAmigo = posAmigo.split()
            if cavaleirosTotal[x-1] == posAmigo[0]:
                if cavaleirosTotal[x] in cavaleirosAmigo[y]:
                    formou += 1

        
                
          
    if len(cavaleirosTotal) == formou:
        print(f' A Távola ficou na seguinte formação:\n {p}')
        break
