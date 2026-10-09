import networkx as nx

# 1. Configuração do Grafo (A base do sistema)
G = nx.Graph()
nos = ['A', 'B', 'C', 'D']
arestas = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
G.add_edges_from(arestas)

print("--- ESTRUTURA DA REDE ---")
print(f"Nós disponíveis: {G.nodes()}")
print(f"Conexões (Arestas): {G.edges()}")
print(f"Vizinhos do nó B: {list(G.neighbors('B'))}")