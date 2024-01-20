import networkx as nx
from metro_graph import G
from data import stations

def find_shortest_path(graph, start_station, end_station):
    all_pairs_shortest_paths = dict(nx.all_pairs_dijkstra_path_length(graph, weight='weight'))

    if start_station not in stations or end_station not in stations:
        print("Невірно вказані станції")
        return None

    try:
        shortest_distance = all_pairs_shortest_paths[start_station][end_station]
        shortest_path = nx.shortest_path(graph, source=start_station, target=end_station, weight='weight')
        return shortest_path, shortest_distance
    except nx.NetworkXNoPath:
        print(f"Неможливо знайти шлях між {start_station} і {end_station}")
        return None

if __name__ == "__main__":
    start_trip = "Heroiv Dnipra"
    end_trip = "Akademmistechko"

    result = find_shortest_path(G, start_trip, end_trip)

    if result:
        shortest_path, shortest_distance = result
        print(f"Найкоротший шлях між {start_trip} і {end_trip}: {shortest_path}")
        print(f"Відстань: {shortest_distance}")
