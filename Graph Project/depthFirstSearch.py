import sys

def DFS(object, num, edges, i):
  num[object] = i #marca o vertice atual e qual sua ordem de verificacao
  i = i + 1
  for x2 in tg.get_adjacentes(object): #procura os adjacentes do vertice atual
    if num[x2] == sys.maxsize/2: #verifica se o adjacente atual ja foi verificado

      #txt = str(object) + " - " + str(x2) #opcao de lista que mostra as arestas verificadas
      #edges.append(txt)
      
      edges.append(x2) #adiciona o adjacente atual na lista de vertices verificados
      DFS(x2, num, edges, i) #inicia a recursao usando o adjacente atual

def depthFirstSearch(grafo, vertice_i): #inicio, recebe como parametros o grafo do problema e qual vertice inicial da busca
  
  num = {} #inicio dict que marca qual vertice ja foi verificado

  if vertice_i not in grafo.get_vertices(): #verifica se o vertice inicial pertence ao grafo
    print("Vertice Invalido!")
    return None

  for aux in range(grafo.countVert()): #percorre todo o grafo para armazenar na variavel num
    x = list(tg.vertices)[aux]
    num[x] = sys.maxsize/2 #variavel arbitraria para mostrar que o vertice ainda nao foi percorrido

  edges = [] #inicia lista de arestas que foram verificadas
  
  while vertice_i in grafo.get_vertices() and num[vertice_i] == sys.maxsize/2: #verifica se o vertice escolhido existe e o vertice ja foi marcado
      DFS(vertice_i, num, edges, 1)

  print("Partindo do vértice", vertice_i, "->", end = '')

  return (edges) #devolve a lista de vertices que foram verificados