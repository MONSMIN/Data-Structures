import uuid
import networkx as nx
import matplotlib.pyplot as plt


class HeapNode:
    def __init__(self, key, color="skyblue"):
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_heap_edges(graph, heap, pos, parent=None, layer=1, index=1):
    if index <= len(heap):
        node = heap[index - 1]
        graph.add_node(node.id, color=node.color, label=node.val)

        if parent:
            graph.add_edge(parent.id, node.id)

        x = pos[parent.id][0] if parent else 0
        y = pos[parent.id][1] - 1 if parent else 0

        l_child_index = 2 * index
        r_child_index = 2 * index + 1

        l_child = heap[l_child_index - 1] if l_child_index <= len(heap) else None
        r_child = heap[r_child_index - 1] if r_child_index <= len(heap) else None

        if l_child:
            l_x = x - 1 / 2 ** layer
            pos[l_child.id] = (l_x, y)
            add_heap_edges(graph, heap, pos, node, layer + 1, l_child_index)

        if r_child:
            r_x = x + 1 / 2 ** layer
            pos[r_child.id] = (r_x, y)
            add_heap_edges(graph, heap, pos, node, layer + 1, r_child_index)


def draw_heap(heap):
    heap_graph = nx.Graph()  # Зміна DiGraph на Graph, бо купа не вимагає напрямленості
    pos = {heap[0].id: (0, 0)} if heap else {}
    add_heap_edges(heap_graph, heap, pos)

    colors = [node[1]['color'] for node in heap_graph.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in heap_graph.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(heap_graph, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


# Створення бінарної купи
heap = [HeapNode(0), HeapNode(4), HeapNode(1), HeapNode(5), HeapNode(10), HeapNode(3)]

# Відображення бінарної купи
draw_heap(heap)
