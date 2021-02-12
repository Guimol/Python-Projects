class Grafo:

    def __init__(self, vertices):
        self.listaAdj = {}
        self.nvertices = vertices
        
    #arestas bidirecionais
    def add_aresta (self, vert1, vert2):
        if vert1 not in self.listaAdj:
            self.listaAdj[vert1] = []
        if vert2 not in self.listaAdj:
            self.listaAdj[vert2] = []
        self.listaAdj[vert1].append(vert2)
        self.listaAdj[vert2].append(vert1)
        
    def get_vertices(self):
        #retorna list type e nao dict_keys type
        return( list(self.listaAdj.keys()))
    
    def get_adjacentes(self, vertice):
        return(self.listaAdj[vertice])
        
    def mostraLista(self):
        for x in self.listaAdj.items():
            print(x)

class Grafo(object):
    def __init__(self, vertices):
        self.vertices = {}
        self.nv=vertices
    
    def add_aresta(self, chave_de, chave_para, peso)
        if chave_de not in self.vertices:
            self.vertices[chave_de] = {}
        if chave_para not in self.vertices:
            self.vertices[chave_para] = {}
        self.vertices[chave_de][chave_para] = peso

    def mostraGrafo(self):
        for x in self.vertices.items():
            print(x)
            
    def get_vertices(self):
    #retorna list type e não dict_keys type
        return(list(self.vertices.keys()))
        
    def get_adjacentes(self, chave):
        return(list(self.vertices[chave].keys()))
        
    def get_pesosAdjacentes(self, chave):
        return(list(self.vertices[chave].values()))
       
class Vertice(object):
    def __init__(self, num, dist):
        self.num = num
        self.dist = dist #dado adicional = distancia
    
    def __repr__(self):
        return str(self.num) + "-" + str(self.dist)
        
    def mudaDist(self, dist2):
        self.dist = dist2
        
class Tg(object):
    def __init__(self, vertices):
        self.vertices = {}
        self.nv = vertices
        
    def add_aresta(self, chave_de: Vertice, chave_para: Vertice, peso):
        if chave_de not in self.vertices:
            self.vertices[chaves_de] = {}
        if chave_para not in self.vertices:
            self.vertices[chaves_para] = {}
        self.vertices[chave_de][chave_para] = peso
        
    def mostraGrafo(self):
        for x in self.vertices.items():
            print(x)



