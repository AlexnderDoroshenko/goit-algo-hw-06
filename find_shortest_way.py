import heapq

from networkx_graph import CREATED_GRAPH


# Додаємо ребра (дороги) з вагами
edges = [
    ('A', 'B', 5), ('A', 'C', 10), ('B', 'C', 2),
    ('B', 'D', 4), ('C', 'D', 1), ('D', 'E', 3)
]
CREATED_GRAPH.add_weighted_edges_from(edges)


def dijkstra(graph, start):
    queue = []
    heapq.heappush(queue, (0, start))  # (вага, вершина)
    distances = {node: float('infinity') for node in graph.nodes()}
    distances[start] = 0
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances


# Використання алгоритму Дейкстри
shortest_paths = dijkstra(CREATED_GRAPH, 'A')
print("Найкоротші шляхи від A до всіх інших вершин:", shortest_paths)
