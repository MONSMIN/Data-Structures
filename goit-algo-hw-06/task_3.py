import networkx as nx
import heapq
from metro_graph import G  # Підключте ваш граф тут

def dijkstra(graph, start, end):
    distances = {vertex: float('infinity') for vertex in graph.nodes}
    distances[start] = 0
    priority_queue = [(0, start)]
    previous_vertices = {vertex: None for vertex in graph.nodes}

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight['weight']

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    path, current_vertex = [], end
    while previous_vertices[current_vertex] is not None:
        path.insert(0, current_vertex)
        current_vertex = previous_vertices[current_vertex]

    if path:
        path.insert(0, start)

    return distances[end], path

if __name__ == "__main__":
    start_trip = "Heroiv Dnipra"
    end_trip = "Akademmistechko"

    distance, route = dijkstra(G, start_trip, end_trip)

    if distance == float('infinity'):
        print(f"Маршрут між '{start_trip}' та '{end_trip}' не знайдено.")
    else:
        print(f"Найкоротший маршрут між '{start_trip}' та '{end_trip}': {route}")
        print(f"Відстань: {distance}")





# def find_shortest_path(graph, start_station, end_station):
#     all_pairs_shortest_paths = dict(nx.all_pairs_dijkstra_path_length(graph, weight='weight'))

#     if start_station not in stations or end_station not in stations:
#         print("Невірно вказані станції")
#         return None

#     try:
#         shortest_distance = all_pairs_shortest_paths[start_station][end_station]
#         shortest_path = nx.shortest_path(graph, source=start_station, target=end_station, weight='weight')
#         return shortest_path, shortest_distance
#     except nx.NetworkXNoPath:
#         print(f"Неможливо знайти шлях між {start_station} і {end_station}")
#         return None

# if __name__ == "__main__":
#     start_trip = "Heroiv Dnipra"
#     end_trip = "Akademmistechko"

#     result = find_shortest_path(G, start_trip, end_trip)

#     if result:
#         shortest_path, shortest_distance = result
#         print(f"Найкоротший шлях між {start_trip} і {end_trip}: {shortest_path}")
#         print(f"Відстань: {shortest_distance}")
