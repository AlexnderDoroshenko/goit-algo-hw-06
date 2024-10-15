import networkx as nx
import matplotlib.pyplot as plt

# Створимо граф
G = nx.Graph()

# Додаємо вершини (міста)
nodes = ['A', 'B', 'C', 'D', 'E']
G.add_nodes_from(nodes)

CREATED_GRAPH = G

# Візуалізація графа
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue',
        node_size=2000, font_size=16)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Транспортна мережа міста")
plt.show()

# Аналіз характеристик
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступінь вершин:", degrees)
