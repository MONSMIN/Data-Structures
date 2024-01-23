
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.key < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def find_min_value(root):
    while root.left is not None:
        root = root.left
    return root.key

def find_max_value(root):
    while root.right is not None:
        root = root.right
    return root.key

def tree_sum(root):
    if root is None:
        return 0
    return root.key + tree_sum(root.left) + tree_sum(root.right)


root = None
keys = [20, 8, 22, 4, 12, 10, 14]

for key in keys:
    root = insert(root, key)

min_value = find_min_value(root)
max_value = find_max_value(root)
total_sum = tree_sum(root)

print("Найменше значення в дереві:", min_value)
print("Найбільше значення в дереві:", max_value)
print("Сума всіх значень в дереві:", total_sum)