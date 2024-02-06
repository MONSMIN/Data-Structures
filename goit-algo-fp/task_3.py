import networkx as nx
import matplotlib.pyplot as plt
import heapq


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances


def visualize_graph(graph):
    G = nx.Graph()

    for vertex, edges in graph.items():
        for neighbor, weight in edges.items():
            G.add_edge(vertex, neighbor, weight=weight)

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.show()


graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Виклик функцій для алгоритму Дейкстри та візуалізації графа
start_vertex = 'A'
shortest_distances = dijkstra(graph, start_vertex)
print(f"Найкоротші відстані від {start_vertex}: {shortest_distances}")

visualize_graph(graph)
