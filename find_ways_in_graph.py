from networkx_graph import CREATED_GRAPH


def dfs(graph, start, goal, path=[]):
    path = path + [start]
    if start == goal:
        return path
    for node in graph.neighbors(start):
        if node not in path:
            newpath = dfs(graph, node, goal, path)
            if newpath:
                return newpath
    return None


def bfs(graph, start, goal):
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == goal:
            return path
        for neighbor in graph.neighbors(node):
            if neighbor not in path:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return None


# Приклад використання
start_node = 'A'
goal_node = 'D'

dfs_path = dfs(CREATED_GRAPH, start_node, goal_node)
bfs_path = bfs(CREATED_GRAPH, start_node, goal_node)

print(f"Шлях DFS від {start_node} до {goal_node}: {dfs_path}")
print(f"Шлях BFS від {start_node} до {goal_node}: {bfs_path}")
