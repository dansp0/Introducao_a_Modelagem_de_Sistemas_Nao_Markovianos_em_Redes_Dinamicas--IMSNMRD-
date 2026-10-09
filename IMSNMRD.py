import numpy as np
import networkx as nx

# 1. Configuração do Grafo
G = nx.Graph()
nos = ['A', 'B', 'C', 'D']
arestas = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
G.add_edges_from(arestas)

# 2. Matriz de Transição (1ª Ordem)
matriz_adj = nx.adjacency_matrix(G).todense()
graus = np.array(matriz_adj.sum(axis=1)).flatten()
P = matriz_adj / graus[:, np.newaxis]

print("--- MATRIZ DE TRANSIÇÃO P (1ª ORDEM) ---")
print(np.round(P, 2))

# 3. Probabilidades específicas saindo de B
vizinhos_B = list(G.neighbors('B'))
idx_B = list(G.nodes()).index('B')
probs_markov = [P[idx_B, list(G.nodes()).index(v)] for v in vizinhos_B]

labels_markov = {('B', v): f"{p:.2f}" for v, p in zip(vizinhos_B, probs_markov)}
print(f"Probabilidades saindo de B: {labels_markov}")