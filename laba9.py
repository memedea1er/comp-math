"""
Генерация дерева и вывод его в виде древовидной структуры с помощью символов.
Также вычисляется наибольшая глубина дерева.

Переменные:
- root_node: корень сгенерированного дерева
- max_depth: глубина дерева
- indent: префикс для отступов при печати узлов
- is_last: указывает, является ли узел последним у дочерних узлов своего родителя
"""

import random

# Генерация узла
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.branches = []

    def __str__(self):
        return str(self.value)

# Генерация дерева
def generate_random_tree(depth):
    if depth == 0:
        return None
    root = TreeNode(random.randint(1, 100))
    num_branches = random.randint(0, 3)
    for _ in range(num_branches):
        root.branches.append(generate_random_tree(depth - 1))
    return root

# Вывод дерева
def print_tree(root, prefix='', is_tail=True):
    if root is None:
        return
    print(prefix + ('└── ' if is_tail else '├── ') + str(root.value))
    prefix += '    ' if is_tail else '│   '
    branches_count = len(root.branches)
    for i, branch in enumerate(root.branches):
        is_last_child = (i == branches_count - 1)
        print_tree(branch, prefix, is_last_child)

# Вычисление максимальной глубины
def max_depth(root):
    if root is None:
        return 0
    if not root.branches:
        return 1
    return 1 + max(max_depth(branch) for branch in root.branches)


# Пример использования
depth = random.randint(0, 10)
tree = generate_random_tree(depth)
print("Сгенерированное дерево:")
print_tree(tree)
print("Наибольшая глубина дерева:", max_depth(tree))