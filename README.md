# Introducao_a_Modelagem_de_Sistemas_Nao_Markovianos_em_Redes_Dinamicas--IMSNMRD-
Simulação em Python de caminhadas aleatórias em redes. Compara matrizes de transição Markovianas (1ª ordem) com fluxos Não-Markovianos (2ª ordem com repulsão topológica), gerando visualizações estocásticas para o projeto IMSNMRD.

Introdução à Modelagem de Sistemas Não-Markovianos em Redes Dinâmicas (IMSNMRD)
Este repositório contém os códigos e simulações desenvolvidos para o projeto de Iniciação Científica IMSNMRD. O objetivo principal é visualizar, calcular e comparar matematicamente como a "memória" afeta a forma como informações (ou agentes) navegam por uma rede complexa.
O código foi escrito em Python e é ideal para ser executado em ambientes de cadernos interativos, como o Jupyter Notebook ou o Google Colab, facilitando a geração de gráficos didáticos para pôsteres acadêmicos e apresentações.

Entendendo o Projeto (De forma simples)
Imagine que você está caminhando por um labirinto (uma Rede ou Grafo), onde as salas são os "Nós" (A, B, C, D) e os corredores são as "Arestas". Como você escolhe o próximo corredor?

1. A Abordagem Clássica: Sem Memória (Cadeia de Markov de 1ª Ordem)Na matemática clássica, assumimos que o viajante sofre de "amnésia". Ao chegar na sala B, ele esquece de onde veio. Ele olha para os corredores disponíveis e escolhe o próximo destino de forma puramente aleatória.Regra Matemática: O estado futuro depende apenas do estado atual ($X_t$).

2. A Abordagem do Projeto: Com Memória (Não-Markoviano de 2ª Ordem)
No mundo real (tráfego de internet, redes sociais, movimento de animais), as coisas têm histórico. Se você acabou de vir da sala A para a sala B, é muito improvável que você dê meia-volta e retorne para A imediatamente. Você vai preferir explorar novos caminhos (salas C ou D).
Regra Matemática: O estado futuro depende do estado atual ($X_t$) E do estado passado ($X_{t-1}$). Aplicamos uma taxa de repulsão (penalidade) ao nó de origem para forçar a exploração da rede.
Este código simula exatamente essa diferença, gerando as matrizes de probabilidade e plotando os gráficos lado a lado.



Como instalar e rodar o projetoPré-requisitosPara rodar este código, você precisará do Python (versão 3.7 ou superior) e de três bibliotecas fundamentais do ecossistema científico.

Abra o seu terminal (ou a primeira célula do Google Colab) e digite:  pip install numpy networkx matplotlib

Executando o Código

O projeto é dividido em blocos lógicos:

Configuração da Topologia: Cria o "mapa" (Grafo) com os nós A, B, C e D.

Cálculo da Matriz de Transição: Usa álgebra linear para definir as probabilidades de 1ª ordem.

Aplicação do Tensor de Repulsão: Calcula as probabilidades de 2ª ordem considerando a trajetória (ex: veio de A para B).

Visualização: Gera um painel comparativo side-by-side (lado a lado) pronto para ser exportado para pôsteres ou slides.

Basta copiar o script completo (ou importar as células no Colab) e executar. O resultado final será uma imagem vetorial com caixas explicativas e legendas automáticas sobre as arestas.


Referências Bibliográficas e Ferramentas
A construção deste código e sua fundamentação teórica baseiam-se em repositórios oficiais e literatura científica validada.

1. Documentação Oficial das Bibliotecas (O "Motor" do Código)
NetworkX (Análise de Redes): Utilizado para a criação da topologia do grafo, layouts de plotagem (spring_layout) e renderização de nós/arestas.

Referência: NetworkX Developers. (2024). NetworkX Documentation. Disponível em: https://networkx.org/

NumPy (Matemática Matricial): Utilizado para o manuseio eficiente de arrays e cálculos de probabilidade (ex: nx.to_numpy_array).

Referência: Harris, C. R. et al. (2020). Array programming with NumPy. Nature, 585(7825), 357-362. Disponível em: https://numpy.org/

Matplotlib (Visualização de Dados): Responsável pela interface gráfica e construção do painel comparativo para o pôster.

Referência: Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. Computing in Science & Engineering, 9(3), 90-95.
