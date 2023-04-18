import networkx as nx
import matplotlib.pyplot as plt

# Carrega o conjunto de dados
G = nx.read_edgelist('bio-CE-LC.edges', nodetype=int, data=False)

# Imprime informações básicas sobre o grafo
print(f'O grafo tem {G.number_of_nodes()} nós e {G.number_of_edges()} arestas.')
print(f'A densidade do grafo é {nx.density(G):.4f}.')

# Calcula a distribuição de graus
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
degree_count = dict([(deg, degree_sequence.count(deg)) for deg in degree_sequence])
print(f'Distribuição de graus: {degree_count}')

max_degree = max([d for n, d in G.degree()])
print(f"Grau máximo: {max_degree}")

min_degree = min([d for n, d in G.degree()])
print(f"Grau mínimo: {min_degree}")

avg_degree = sum(dict(G.degree()).values()) / len(G)
print(f"Grau médio: {avg_degree}")

assortativity = nx.assortativity.degree_pearson_correlation_coefficient(G)
print(f"Assortatividade: {assortativity}")

num_triangles = sum(nx.triangles(G).values())
print(f"Número de triângulos: {num_triangles}")

max_num_triangles = max(nx.triangles(G).values())
print(f"Número máximo de triângulos: {max_num_triangles}")

avg_clustering = nx.average_clustering(G)
print(f"Coeficiente de agrupamento médio: {avg_clustering}")

cliques = list(nx.find_cliques(G))
max_clique_size = max([len(clique) for clique in cliques])
print(f"Limite inferior do clique máximo: {max_clique_size}")


# Utiliza um layout circular
pos = nx.circular_layout(G)

# Desenha o grafo com as novas configurações
fig, ax = plt.subplots(figsize=(10, 8))
nx.draw(G, pos=pos, node_size=50, with_labels=True)
plt.title('Layout Circular')
plt.savefig(f'grafic/1.png', dpi=600)
plt.close()

# Utiliza um layout kamada-kawai
pos = nx.kamada_kawai_layout(G)

# Desenha o grafo com as novas configurações
fig, ax = plt.subplots(figsize=(10, 8))
nx.draw_networkx(G, pos=pos, node_size=100, with_labels=False)
plt.title('Layout Kamada-Kawai')
plt.savefig(f'grafic/2.png', dpi=600, bbox_inches='tight')
plt.close()

# Utiliza um layout spring
fig, ax = plt.subplots(figsize=(10, 8))
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos=pos, node_size=100, with_labels=False)
plt.title('Spring Layout')
plt.savefig(f'grafic/3.png', dpi=600, bbox_inches='tight')
plt.close()

# Utiliza um layout spectral
fig, ax = plt.subplots(figsize=(10, 8))
pos = nx.spectral_layout(G)
nx.draw_networkx(G, pos=pos, node_size=100, with_labels=False)
plt.title('Spectral Layout')
plt.savefig(f'grafic/4.png', dpi=600, bbox_inches='tight')
plt.close()

# Utiliza um layout random
fig, ax = plt.subplots(figsize=(10, 8))
pos = nx.random_layout(G)
nx.draw_networkx(G, pos=pos, node_size=100, with_labels=False)
plt.title('Random Layout')
plt.savefig(f'grafic/5.png', dpi=600, bbox_inches='tight')
plt.close()
