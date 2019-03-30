
                #TRABALHO ESTRUTURA DE DADOS (EP1)
    #Lucas Ribeiro Sonnewend Cardoso e Paulo Henrique da Silva Correia
    #Turma: ADS 3B
    

from random import shuffle
import time
import timeit

def quicksort(lista):
    if len(lista) <= 1: 
        return lista
    
    pivo = lista[0]
    iguais  = [x for x in lista if x == pivo]
    menores = [x for x in lista if x <  pivo]
    maiores = [x for x in lista if x >  pivo]
    return quicksort(menores) + \
           iguais + quicksort(maiores)


def merge(e, d):
    r = []
    i, j = 0, 0
    while i < len(e) and j < len(d):
        if e[i] <= d[j]:
            r.append(e[i])
            i += 1
        else:
            r.append(d[j])
            j += 1
    r += e[i:]
    r += d[j:]
    return r

def mergesort(v):
    if len(v) <= 1:
        return v
    else:
        m = len(v) // 2
        e = mergesort(v[:m])
        d = mergesort(v[m:])
        return merge(e, d)

    
def selection(v):        
    resp = []
    while v:
        m = min(v)
        resp.append(m)
        v.remove(m)
    return resp


def native(vetorNat):
    return(vetorNat.sort())



timeMax = 30.00

posicoesVetor = 0

tempoCorrido = 0.00

tempoSelect = []

vetorSelect = []

while(tempoCorrido < timeMax):

    tempoCorrido = timeit.default_timer()
    posicoesVetor += 2000
    vet = list(range(posicoesVetor))
    shuffle(vet)
    selection(vet)
    tempoCorrido = timeit.default_timer()-tempoCorrido
    tempoSelect.append("%.2f" % tempoCorrido)
    vetorSelect.append(posicoesVetor)

    
posicoesVetor = 0

tempoMerge = []
vetorMerge = []
tempoCorrido = 0.00

while(posicoesVetor <= vetorSelect[-1]):
    
    inicio = timeit.default_timer()
    posicoesVetor += 2000
    vet = list(range(posicoesVetor))
    shuffle(vet)
    mergesort(vet)
    tempoCorrido = timeit.default_timer()-inicio
    tempoMerge.append("%.2f" % tempoCorrido)
    vetorMerge.append(posicoesVetor)

posicoesVetor = 0

tempoQuick = []
vetorQuick = []
tempoCorrido = 0.00

while(posicoesVetor<=vetorSelect[-1]):
    
    inicio = timeit.default_timer()
    posicoesVetor += 2000
    vet = list(range(posicoesVetor))
    shuffle(vet)
    quicksort(vet)
    tempoCorrido = timeit.default_timer()-inicio
    tempoQuick.append("%.2f" % tempoCorrido)
    vetorQuick.append(posicoesVetor)


posicoesVetor = 0

tempoNativo = []
vetorNativo = []
tempoCorrido = 0.00

while(posicoesVetor<=vetorSelect[-1]):
    
    inicio = timeit.default_timer()
    posicoesVetor += 2000
    vet = list(range(posicoesVetor))
    shuffle(vet)
    native(vet)
    tempoCorrido = timeit.default_timer()-inicio
    tempoNativo.append("%.2f" % tempoCorrido)
    vetorNativo.append(posicoesVetor)



print('-----------------------------------------------')
print('       |                 times                |')
print('-----------------------------------------------')
print('       |  Mergesort QuickSort Selection Native|')


for i in range(len(vetorSelect)):
    if(vetorSelect[i] >=10000):
        if(float(tempoSelect[i]) >= 10.00):
            print (str(vetorSelect[i])+'       '+(tempoMerge[i])+'       '+tempoQuick[i]+'     '+tempoSelect[i]+'    '+tempoNativo[i])

        else:
            print (str(vetorSelect[i])+'       '+(tempoMerge[i])+'       '+tempoQuick[i]+'     '+tempoSelect[i]+'     '+tempoNativo[i])           

    else:
        print (str(vetorSelect[i])+'        '+(tempoMerge[i])+'       '+tempoQuick[i]+'     '+tempoSelect[i]+'     '+tempoNativo[i])

        
