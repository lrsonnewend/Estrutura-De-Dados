'''EP3 - DUPLA: LUCAS RIBEIRO SONNEWEND CARDOSO
                PAULO HENRIQUE DA SILVA CORREIA

        TURMA: 3º ADS B
'''


matriz1 = '''10101
10101
11111'''
matriz2= '''010
111
000
101'''

matriz='''0011001010
0110001010
0011001110
0000000000
0010001010
0010011111
1111100000
0010001110
0010001110'''

matrizona = '''010
111
000
101,
10101
10101
11111,
0011001010
0110001010
0011001110
0000000000
0010001010
0010011111
1111100000
0010001110
0010001110'''

def tudo(matrizSeparada):
  #Salva as coordenadas de todos os '1'
  #INICIO
  for x in range(len(matriz)):
    matrizCada = matriz[x]
    for y in range(len(matrizCada)):
      if matrizCada[y] == '1':
        vetorCoordenada.append(str(x)+','+str(y))
  #FIM

  vetorRegiao = []
  #funcao recursiva para pegar os parentes da coordenada passada
  def proximidades(coordenadas,anterior):
    X = coordenadas[0]
    Y = coordenadas[2]

    cor = str(int(X)+1)+','+str(int(Y)) # olha abaixo
    if cor != anterior:
      if cor in vetorCoordenada:
        if cor not in vetorRegiao:
          vetorRegiao.append(cor)
          proximidades(cor,(X+','+'Y'))

    cor = str(int(X))+','+str(int(Y)+1) # olha a direita
    if cor != anterior:
      if cor in vetorCoordenada:
        if cor not in vetorRegiao:
          vetorRegiao.append(cor)
          proximidades(cor,(X+','+'Y'))

    cor = str(int(X))+','+str(int(Y)-1)#olha a esquerda
    if cor != anterior:
      if cor in vetorCoordenada:
        if cor not in vetorRegiao:
          vetorRegiao.append(cor)
          proximidades(cor,(X+','+'Y'))

    cor = str(int(X)-1)+','+str(int(Y))#olha a acima
    if cor != anterior:
      if cor in vetorCoordenada:
        if cor not in vetorRegiao:
          vetorRegiao.append(cor)
          proximidades(cor,(X+','+'Y'))
          
  for x in vetorCoordenada:
    proximidades(x,('-3'+','+'-3'))
    vetorRegiao.append('ACABOU')



  #percorre o vetor das coordenadas novamente em busca de quem 
  #dos que ficaram isolados
  #exemplo
  '''
  010
  111
  000
  101
  os dois um de baixo, estao isolados e a funcao nao pega eles
  '''
  for x in vetorCoordenada:
    if x not in vetorRegiao:
      vetorRegiao.append('ACABOU')
      vetorRegiao.append(x)

  #tira o excesso dos 'Acabou'      
  vetorAuxiliar = []
  for x in range(len(vetorRegiao)):
    if x == 0:
      vetorAuxiliar.append(vetorRegiao[x])
    else:
      if vetorRegiao[x] != vetorRegiao[x-1]:
        vetorAuxiliar.append(vetorRegiao[x])

  #funcao que altera na posicao indicada por um valor indicado
  def Altera(texto, posicao, valorTroca):
    vet2 = []
    for x in range(len(texto)):
      if x == int(posicao):
        vet2.append(str(valorTroca))
      else:
        vet2.append(texto[x])

    vet = ''.join(vet2)
    return (vet)
        
  valor = 0
  vetorPolo = []

  #percorre cada posicao, acha na matriz, e altera o valor
  def trocaValor(vetor):
    valor = 1
    for p in range(len(vetor)):
      posx = vetor[p]
      posy = posx[2]
      posx = posx[0]
      if vetor[p] == 'ACABOU':
        valor = valor+1
      else:
        for x in range(len(matriz)):
          for y in range(len(matriz[x])):
            if posx == str(x) and posy == str(y):
              temp = str(matriz[x])
              matriz[x] = Altera(temp, posy, valor) 
  trocaValor(vetorAuxiliar)#vetor auxiliar contem as coordenadas separadas por regiao

  #imprime mais bonito a matriz
  def imprimirFinalizada(vetor):
    for x in matriz:
      print(x)
  imprimirFinalizada(matriz)

matrizona = matrizona.split(',')
for x in matrizona:
  vetorCoordenada = [] 
  matriz = x.split()
  print('\n')
  print('Entrada: \n')
  for y in matriz:
    print(y)
  print('\n')
  print('Saida: \n')

  tudo(matriz)
