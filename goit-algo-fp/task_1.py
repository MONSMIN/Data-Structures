class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse_list(self):
        prev = None
        cur = self.head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        self.head = prev

    def sort_list(self):
        if self.head is None:
            return
        else:
            current = self.head
            while current.next:
                next_node = current.next
                while next_node:
                    if current.data > next_node.data:
                        current.data, next_node.data = next_node.data, current.data
                    next_node = next_node.next
                current = current.next

    def merge_sorted_lists(self, other_list):
        merged_list = LinkedList()
        cur_self = self.head
        cur_other = other_list.head

        while cur_self and cur_other:
            if cur_self.data < cur_other.data:
                merged_list.insert_at_end(cur_self.data)
                cur_self = cur_self.next
            else:
                merged_list.insert_at_end(cur_other.data)
                cur_other = cur_other.next

        while cur_self:
            merged_list.insert_at_end(cur_self.data)
            cur_self = cur_self.next

        while cur_other:
            merged_list.insert_at_end(cur_other.data)
            cur_other = cur_other.next

        return merged_list


# Приклад використання
llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()

# Видаляємо вузол
llist.delete_node(10)

print("\nЗв'язний список після видалення вузла з даними 10:")
llist.print_list()

# Пошук елемента у зв'язному списку
print("\nШукаємо елемент 15:")
element = llist.search_element(15)
if element:
    print(element.data)

# Реверсування зв'язного списку
print("\nЗв'язний список після реверсування:")
llist.reverse_list()
llist.print_list()

# Сортування зв'язного списку
print("\nЗв'язний список після сортування:")
llist.sort_list()
llist.print_list()

# Об'єднання двох відсортованих списків
llist2 = LinkedList()
llist2.insert_at_end(2)
llist2.insert_at_end(4)
llist2.insert_at_end(6)

print("\nДругий відсортований список:")
llist2.print_list()

merged_list = llist.merge_sorted_lists(llist2)
print("\nОб'єднаний відсортований список:")
merged_list.print_list()
