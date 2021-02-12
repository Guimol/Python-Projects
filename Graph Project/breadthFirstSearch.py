import sys

def BFS(grafo, vertice_i): #inicio, recebe como parametro um grafo e um de seus vertices para inicio da busca

  num = {} #inicio dict que marca qual vertice ja foi verificado
  queue = [] #inicio list da estrutura de FILA que marca qual vertice vai ser verificado
  busca = [] #inicio list que marca qual vertice foi verificado (em ordem de verificacao)

  queue.append(vertice_i) #inicio da FILA queue que eh enviado como paramentro da funcao

  if vertice_i not in grafo.get_vertices(): #verifica se o vertice inicial pertence ao grafo
    print("Vertice Invalido!")
    return None

  for aux in range(grafo.countVert()): #percorre todo o grafo para armazenar na variavel num
    x = list(tg.vertices)[aux]
    num[x] = sys.maxsize/2 #variavel arbitraria para mostrar que o vertice ainda nao foi percorrido

  i = 1

  num[vertice_i] = i #guarda o primeiro vertice como um vertice ja visitado

  while queue: #loop enquanto existirem vertices na lista queue
    atual = queue.pop(0) #retira da FILA o primeiro elemento e o armazena na variavel atual
    busca.append(atual) #armazena qual vertice ja foi verificado na variavel de retorno

    for vizinho in grafo.get_adjacentes(atual): #lista de elementos adjacentes do vertice atual
      if num[vizinho] == sys.maxsize/2: #verifica se o vertice ainda nao foi percorrido
        i = i + 1
        num[vizinho] = i #marca o vertice vizinho como ja verificado
        queue.append(vizinho) #adiciona o vizinho a FILA para ver seus proprios vizinhos

  print("Partindo do vértice", vertice_i, "->", end = '')

  return (busca)