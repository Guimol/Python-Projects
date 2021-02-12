import sys

def Dijk(grafo, vertice_i): #inicio, recebe como parametro um grafo e um de seus vertices para inicio da busca
  
  if vertice_i not in grafo.get_vertices(): #verifica se o vertice inicial pertence ao grafo
    print("Vertice Invalido!")
    return None
  
  dist = {} #inicio do dict que guarda a estimativa de distancia de cada vertice
  pai = {} #inicio do dict que vai armazenar os vertices pai 
  aberto = [] #inicio da lista que mostra quais vertices tao aberto
  texto = [] #inicio da lista para mostrar os caminhos que devem ser percorridos

  for aux in grafo.get_vertices(): #percorre todos os dicts e listas para preencher com valores infinitos
    dist[aux] = sys.maxsize/2
    pai[aux] = -sys.maxsize/2
    aberto.append(aux)

  dist[vertice_i] = 0 #inicia com a distancia do vertice inicial sendo zero

  while aberto: #loop de enquanto houverem vertices abertos
    menorDist = sys.maxsize/2 
    for aux in aberto: #armazena todos os vertices abertos na variavel auxiliar
      if dist[aux] < menorDist: #encontra a menor distancia dos vertices abertos
        menorDist = dist[aux]
        menorV = aux
        
    atual = aberto.pop(aberto.index(menorV)) #torna o vertice com a menor distancia o atual

    for v in grafo.get_adjacentes(atual): #armazena os vertices adjacentes do atual 
      if v in aberto: #encontra dos vertices adjacentes aqueles que ainda estao abertos
        if (dist[atual] + grafo.vertices[atual][v]) < dist[v]: #encontra a menor distancia nos vertices adjacentes em relacao com as outras distancias ja calculadas
          dist[v] = dist[atual] + grafo.vertices[atual][v] #armazena a menor distancia encontrada
          pai[v] = atual #armazena no dict pai qual vertice levou ao atual

  for v in grafo.get_vertices(): #impressao dos caminhos de cada vertice partindo do inicial
    if v != vertice_i:
      aux = v
      aux_texto = "Fim desse Caminho"
      while aux != vertice_i:
        aux_texto = str(aux) + " - " + str(aux_texto)
        aux = pai[aux]
      aux_texto = "Caminho de " + str(vertice_i) + " a " + str(v) + ": " + str(vertice_i) + " - " + str(aux_texto)
      texto.append(aux_texto)

  return texto #retorna uma lista de strings que mostra o melhor caminho a cada vertice partindo do inicial
