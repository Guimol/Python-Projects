class Grafo(object):
    def __init__(self):
        self.vertices = {} #inicia o dict de vertices no grafo
    
    def add_aresta(self, chave_de, chave_para, peso):
        if chave_de not in self.vertices: #checagem de existencia do vertice no dict
            self.vertices[chave_de] = {} #caso não exista a ligacao ainda eh adicionada ao dict
        if chave_para not in self.vertices: #checagem de existencia do vertice no dict
            self.vertices[chave_para] = {} #caso não exista a ligacao ainda eh adicionada ao dict
        self.vertices[chave_de][chave_para] = peso #adiciona o peso de cada aresta e faz o mesmo com seu equivalente oposto
        self.vertices[chave_para][chave_de] = peso

    def countVert(self): #contador de vertices no grafo
      i = 0
      for aux in self.get_vertices():
        i = i + 1
      return i

    def mostraGrafo(self):
        for x in self.vertices.items():
            print(x)
            
    def get_vertices(self):
    #retorna list type e não dict_keys type
        return(list(self.vertices.keys()))

    def get_adjacentes(self, chave):
    #retorna list type e não dict_keys type
        return(list(self.vertices[chave].keys()))
        
    def get_pesosAdjacentes(self, chave):
    #retorna list type e não dict_keys type
        return(list(self.vertices[chave].values()))