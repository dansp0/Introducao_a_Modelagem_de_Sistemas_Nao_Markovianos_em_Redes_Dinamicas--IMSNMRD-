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
print(f"Nós: {G.nodes()}")
print(np.round(P, 2))

# 3. Probabilidades específicas saindo de B
vizinhos_B = list(G.neighbors('B'))
idx_B = list(G.nodes()).index('B')
probs_markov = [P[idx_B, list(G.nodes()).index(v)] for v in vizinhos_B]

# Dicionário de labels para o plot
labels_markov = {('B', v): f"{p:.2f}" for v, p in zip(vizinhos_B, probs_markov)}

# 4. Cálculo Não-Markoviano (Memória com Repulsão)
no_atual = 'B'
no_anterior = 'A'
taxa_retorno = 0.10

probs_memoria = []
prob_restante = 1.0 - taxa_retorno
vizinhos_exploraveis = len(vizinhos_B) - 1

for vizinho in vizinhos_B:
    if vizinho == no_anterior:
        probs_memoria.append(taxa_retorno)
    else:
        probs_memoria.append(prob_restante / vizinhos_exploraveis)

# Dicionário de labels para o plot
labels_memoria = {('B', v): f"{p:.2f}" for v, p in zip(vizinhos_B, probs_memoria)}

print("\n--- DINÂMICA DE 2ª ORDEM ---")
print(f"Trajetória: {no_anterior} -> {no_atual}")
for v, p in zip(vizinhos_B, probs_memoria):
    print(f"Probabilidade de ir para {v}: {p:.2f}")