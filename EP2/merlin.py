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
    #print (p)
    pass
 
##for p in enumerações(['Jessica', 'Fernanda', 'Pamela', 'Renata']):
##    print (p)




#a)
sim = open('casamento.txt')
nao = open('casamento no.txt')
todos = open('cavaleiros.txt')

aux = []
sim = sim.read()
sim = sim.split('\n')

nao = nao.read()
nao = nao.split('\n')

todos = todos.read()
todos = todos.split('\n')

cavaleirosSim = []
cavaleirosNao = []
cavaleirosTotal = []

#cria vetor com todos os cavaleiros que podem ser casados
#########################################################
for s in range(len( sim)):
    s1 =(sim[s])
    s1 = s1.split()
    s1 = s1[1:]
    for x in s1:
        cavaleirosSim.append(x)

cavaleirosSim = sorted(set(cavaleirosSim))
##########################################################

#cria vetor com todos os cavaleiros que nao vao ser casados
#########################################################
for n in range(len( nao)):
    n1 =(nao[n])
    n1 = n1.split()
    n1 = n1[1:]
    cavaleirosNao.append(n1)


##########################################################


#cria vetor com todos os cavaleiros 
#########################################################
for t in range(len( todos)):
    t1 =(todos[t])
    t1 = t1.split()
    for x in t1:
        cavaleirosTotal.append(x)

cavaleirosTotal = sorted(set(cavaleirosTotal))
##########################################################
'''
aux = []
aux = cavaleirosTotal
for p in permutações(aux):
    cavaleirosTotal = aux
    #damas
    quantidadeCasadas = 0
    quantidadeDamas = 0
    for s in range(len(sim)):
        casou = False
        s1 = (sim[s])
        s1 = s1.split()
        dama = s1[0]
        cavaDela = s1[1:]

        n1 = (nao[s])
        n1 = n1.split()
        cavaNao = n1[1:]

    
        for x in cavaleirosTotal:
            if x in cavaDela:
                cavaleirosTotal.remove(x)
                casou = True
                break
            else:
                if len(cavaNao) > 0:                
                    for i in cavaNao:
                        if str(i) != str(x):
                            cavaleirosTotal.remove(x)
                            casou = True
                            break
                        else:
                            continue
                    
                else:#se nao tiver quem nao deseja casar, pega o proximo da lista
                    cavaleirosTotal.remove(x)
                    casou = True
                    break
        


        quantidadeDamas+=1
        if casou:
            quantidadeCasadas+=1

    if quantidadeCasadas == quantidadeDamas:
        print('Todas Casaram')
        break
    else:
        print('Algumas nao casaram')

'''

#B)

cavaleirosAmigo = open('cavaleiros.txt')

cavaleirosAmigo = cavaleirosAmigo.read()

cavaleirosAmigo = cavaleirosAmigo.split('\n')
   

temp = []
for x in permutações(cavaleirosTotal):
    temp = x
    for i in range(len(temp)):
        for s in range(len(cavaleirosAmigos


        
        '''#for y in range(len(x)):
        #posicao 0
        if x[-1] in cavaleirosAmigo[6]:
            print('kk')
        #posicao 0

        #posicao 1
        if x[1] in cavaleirosAmigo[0]:
            print('bruno esta no adriano')

        #posicao 1
        '''        
        break
    break

'''print(f'Linha: {cavaleirosAmigo[s]}')
        break
    print(f'Permutação: {x}')
    break'''
        

    






