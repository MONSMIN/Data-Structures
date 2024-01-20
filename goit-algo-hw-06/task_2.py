from collections import deque
import networkx as nx
from metro_graph import G


def dfs(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = dfs(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths

def bfs(graph, start, end):
    queue = deque([(start, [start])])
    while queue:
        current, path = queue.popleft()
        for neighbor in graph[current]:
            if neighbor not in path:
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))
                if neighbor == end:
                    return new_path
    return []

def main(G):
    # Створення словника, представляючого граф у форматі, який приймає dfs і bfs
    graph_dict = {node: [] for node in G.nodes()}
    for u, v in G.edges():
        graph_dict[u].append(v)
        graph_dict[v].append(u)

    # Знаходження шляхів за допомогою DFS і BFS
    start_station = "Akademmistechko"
    end_station = "Chervonyi Khutir"

    dfs_paths = dfs(graph_dict, start_station, end_station)
    bfs_path = bfs(graph_dict, start_station, end_station)

    # Вивід результатів
    print(f"DFS шляхи між станціями {start_station} та {end_station}:")
    for i, path in enumerate(dfs_paths, 1):
        print(f"Шлях до кінкевої {i}: {path}")

    print(f"\nBFS шлях між станціями {start_station} та {end_station}:")
    print(f"Шлях: {bfs_path}")

if __name__ == "__main__":
    main(G)
