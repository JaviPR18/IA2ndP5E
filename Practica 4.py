import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Grafo:
    def __init__(self):
        self.vertices = set()
        self.aristas = []

    def agregar_vertice(self, valor):
        self.vertices.add(valor)

    def agregar_arista(self, inicio, fin, peso):
        self.aristas.append((inicio, fin, peso))
        self.aristas.append((fin, inicio, peso))

    def prim(self, inicio):
        arbol = []
        visitados = set(inicio)
        aristas_posibles = [
            (peso, inicio, fin) for inicio, fin, peso in self.aristas if inicio == inicio
        ]
        heapq.heapify(aristas_posibles)

        while aristas_posibles:
            peso, inicio, fin = heapq.heappop(aristas_posibles)
            if fin not in visitados:
                visitados.add(fin)
                arbol.append((inicio, fin, peso))
                aristas_posibles.extend(
                    (peso, fin, proximo_fin)
                    for proximo_inicio, proximo_fin, peso in self.aristas
                    if proximo_inicio == fin and proximo_fin not in visitados
                )
                heapq.heapify(aristas_posibles)

        return arbol

# Crear un grafo de ejemplo
grafo_ejemplo = Grafo()
grafo_ejemplo.agregar_vertice("A")
grafo_ejemplo.agregar_vertice("B")
grafo_ejemplo.agregar_vertice("C")
grafo_ejemplo.agregar_vertice("D")

grafo_ejemplo.agregar_arista("A", "B", 2)
grafo_ejemplo.agregar_arista("A", "C", 1)
grafo_ejemplo.agregar_arista("B", "C", 3)
grafo_ejemplo.agregar_arista("B", "D", 4)
grafo_ejemplo.agregar_arista("C", "D", 5)

inicio = "A"
arbol_prim = grafo_ejemplo.prim(inicio)

# Crear un grafo dirigido para visualizar con networkx
G = nx.DiGraph()

for arista in arbol_prim:
    G.add_edge(arista[0], arista[1], weight=arista[2])

# Dibujar el grafo
pos = nx.spring_layout(G)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
