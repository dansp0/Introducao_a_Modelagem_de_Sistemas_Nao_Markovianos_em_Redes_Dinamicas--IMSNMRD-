import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
 
# 1. Configuração do Grafo
G = nx.Graph()
nos = ['A', 'B', 'C', 'D']
arestas = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
G.add_edges_from(arestas)
 
# 2. Matriz de Transição (1ª Ordem)
# Cria a matriz P baseada no grau dos nós (probabilidade uniforme)
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
 
# 5. Visualização Didática para Pôster
fig, axes = plt.subplots(1, 2, figsize=(16, 7))
fig.patch.set_facecolor('#f9f9f9')  # Fundo suave para contraste em pôsteres
pos = nx.spring_layout(G, seed=42)
 
# --- Gráfico 1: 1ª Ordem ---
nx.draw_networkx_nodes(G, pos, ax=axes[0], node_color='lightblue', node_size=2500, edgecolors='gray')
nx.draw_networkx_labels(G, pos, ax=axes[0], font_size=14, font_weight='bold')
nx.draw_networkx_edges(G, pos, ax=axes[0], edge_color='gray', width=2)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels_markov, ax=axes[0],
                             font_color='red', font_size=12, font_weight='bold')
axes[0].set_title("Dinâmica Markoviana Clássica (1ª Ordem)\nSistema sem memória",
                  fontsize=16, fontweight='bold', pad=15)
caixa_texto_1 = "Regra:\nO próximo passo depende\nAPENAS do nó atual (B).\nDestinos são equiprováveis."
axes[0].text(0.05, 0.95, caixa_texto_1, transform=axes[0].transAxes, fontsize=12,
             verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.9))
 
# --- Gráfico 2: 2ª Ordem ---
nx.draw_networkx_nodes(G, pos, ax=axes[1], node_color='lightgreen', node_size=2500, edgecolors='gray')
nx.draw_networkx_nodes(G, pos, ax=axes[1], nodelist=[no_anterior], node_color='salmon',
                       node_size=2500, edgecolors='gray')  # Destaca a origem
nx.draw_networkx_labels(G, pos, ax=axes[1], font_size=14, font_weight='bold')
nx.draw_networkx_edges(G, pos, ax=axes[1], edge_color='gray', width=2)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels_memoria, ax=axes[1],
                             font_color='purple', font_size=12, font_weight='bold')
axes[1].set_title("Dinâmica Não-Markoviana (2ª Ordem)\nMemória com Repulsão",
                  fontsize=16, fontweight='bold', pad=15)
caixa_texto_2 = (f"Trajetória Histórica: {no_anterior} $\\rightarrow$ {no_atual}\n\nRegra:\n"
                 f"Retornar para '{no_anterior}' é penalizado (10%).\nForça a exploração de C e D (45%).")
axes[1].text(0.05, 0.95, caixa_texto_2, transform=axes[1].transAxes, fontsize=12,
             verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.9))
 
# --- Legenda Global Explicativa ---
patch_origem = mpatches.Patch(color='salmon', label='Nó de Origem ($X_{t-1}$)')
patch_atual = mpatches.Patch(color='lightgreen', label='Estado Atual ($X_t$) / Destinos')
fig.legend(handles=[patch_origem, patch_atual], loc='lower center', ncol=2,
           fontsize=14, bbox_to_anchor=(0.5, 0.02))
 
plt.tight_layout(rect=[0, 0.08, 1, 1])
plt.show()