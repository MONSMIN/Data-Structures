import networkx as nx
import matplotlib.pyplot as plt
from data import stations, red_line, blue_line, green_line, transfers, posion_station

G = nx.Graph()
G.add_nodes_from(stations)

# Додаємо ребра до графа G
G.add_edges_from(red_line, color='red')
G.add_edges_from(blue_line, color='blue')
G.add_edges_from(green_line, color='green')
G.add_edges_from(transfers, color='gray', linestyle='dashed')


red_stations = [station for station, _, _ in red_line]
blue_stations = [station for station, _, _ in blue_line]
green_stations = [station for station, _, _ in green_line]

fig, ax = plt.subplots(figsize=(18, 10))

labels = {station: station.split()[-1] for station in stations}


nx.draw_networkx_nodes(G, posion_station, nodelist=red_stations, node_color='red', node_size=700)
nx.draw_networkx_nodes(G, posion_station, nodelist=blue_stations, node_color='blue', node_size=700)
nx.draw_networkx_nodes(G, posion_station, nodelist=green_stations, node_color='green', node_size=700)
nx.draw_networkx_labels(G, posion_station, labels=labels, font_size=8, bbox=dict(facecolor='white', alpha=0.75, edgecolor='none'))


edge_labels = {(u, v): G[u][v]['weight'] for u, v in G.edges}
nx.draw_networkx_edge_labels(G, posion_station, edge_labels=edge_labels)

edge_colors = [G[u][v]['color'] for u, v in G.edges]
edge_styles = [G[u][v]['linestyle'] if 'linestyle' in G[u][v] else '-' for u, v in G.edges]
nx.draw_networkx_edges(G, posion_station, edge_color=edge_colors, style=edge_styles)


red_patch = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='Red Line_1')
blue_patch = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label='Blue Line_2')
green_patch = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='green', markersize=10, label='Green Line_3')
transfer_patch = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='gray', linestyle='dashed', markersize=10, label='Transfers')


plt.legend(handles=[red_patch, blue_patch, green_patch, transfer_patch])

if __name__ == "__main__":
    plt.show()
