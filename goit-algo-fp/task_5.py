import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def depth_first_traversal(node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    yield node
    for neighbor in [node.left, node.right]:
        if neighbor and neighbor not in visited:
            yield from depth_first_traversal(neighbor, visited)

def breadth_first_traversal(node):
    queue = [node]
    visited = set()
    while queue:
        current_node = queue.pop(0)
        if current_node not in visited:
            visited.add(current_node)
            yield current_node
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

def draw_traversal(traversal):
    tree = nx.DiGraph()
    pos = {}
    visited_nodes = set()
    current_y = 0  # Змінна для збереження поточної вертикальної позиції

    # Визначення максимальної довжини обходу для налаштування кольорів
    max_depth = max(len(list(depth_first_traversal(traversal[0]))), len(traversal))

    for i, node in enumerate(traversal):
        # Обчислення колірного відтінку в залежності від позиції в обході
        color_intensity = 1 - (i / max_depth)
        color = f"#{int(255 * color_intensity):02x}{int(255 * color_intensity):02x}{int(255 * color_intensity):02x}"

        if node not in visited_nodes:
            visited_nodes.add(node)
            tree.add_node(node.id, color=color, label=node.val)
            pos[node.id] = (0, current_y)  # Встановлюємо позицію вузла залежно від поточної вертикальної позиції
            current_y -= 1  # Зменшуємо поточну вертикальну позицію для наступного шару дерева

    for node in traversal:
        if node.left and node.left in visited_nodes:
            tree.add_edge(node.id, node.left.id)
        if node.right and node.right in visited_nodes:
            tree.add_edge(node.id, node.right.id)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()



# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення дерева
draw_tree(root)

# Обхід у глибину
depth_first = list(depth_first_traversal(root))
draw_traversal(depth_first)

# Обхід у ширину
breadth_first = list(breadth_first_traversal(root))
draw_traversal(breadth_first)
