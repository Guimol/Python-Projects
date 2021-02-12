import sys

def Prim(grafo, vertice_i): #inicio, recebe como parametro um grafo e um de seus vertices para inicio da busca

  if vertice_i not in grafo.get_vertices(): #verifica se o vertice inicial pertence ao grafo
    print("Vertice Invalido!")
    return None

  pai = [] #inicio list que armazena a lista de vertices ligados, que formam a arvore minima do algoritmo
  queue = [] #inicio list da estrutura de FILA que marca qual vertice vai ser verificado

  queue = grafo.get_vertices() #insere todos os vertices do grafo na FILA 
  atual = queue.pop(queue.index(vertice_i)) #retira o vertice inicial da FILA de busca
  texto = "Arvore Minima iniciada em " + str(atual) #variavel texto para exibir a arvore minima
  pai.append(texto) #insere o vertice inicial no inicio da lista de vertices da arvore minima

  while queue: #enquanto a FILA tiver membros executa
    menorDist = sys.maxsize/2 #infinito que inicia a variavel de busca da menor distancia entre dois vertices
    for aux in grafo.get_adjacentes(atual): #acha os vertices adjacentes do vertice atual
      if aux in queue: #verifica se o vertice adjacente encontrado ainda esta na FILA de busca, se não, não alterar ele
        if grafo.vertices[aux][atual] < menorDist: #loop para encontrar do vertice atual a menor distancia e que vertice eh o de menor distancia
          menorV = aux
          aux_adj = aux
          menorDist = grafo.vertices[aux][atual]
      
    texto = str(atual) + " - " + str(aux_adj)
    atual = queue.pop(queue.index(menorV)) #retira da FILA o vertice com menor distancia do atual e reinicia o loop com esse menor encontrado
    pai.append(texto) #insere o atual que ja terminou de achar os minimos na lista da arvore minima

  return pai #retorna uma lista de strings que mostra quais arestas formam a arvore minima desse grafo