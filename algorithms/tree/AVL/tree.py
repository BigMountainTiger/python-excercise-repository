# https://www.geeksforgeeks.org/introduction-to-avl-tree/
# https://www.geeksforgeeks.org/avl-tree-in-python/#
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


def height(node):
    return 0 if node is None else node.height


def balance_factor(node):
    return 0 if node is None else height(node.left) - height(node.right)


def validate_AVL(node):
    if node is None:
        return

    bf = balance_factor(node)
    if bf < -1 or bf > 1:
        raise Exception(f'data = {node.data}, bf = {bf}')

    validate_AVL(node.left)
    validate_AVL(node.right)


def print_tree(node):
    if node is None:
        return

    print_tree(node.left)
    print(f'data = {node.data}, height = {
          height(node)}, bf = {balance_factor(node)}')
    print_tree(node.right)


def min_value_node(node):
    if node is None:
        return None

    while node.left is not None:
        node = node.left

    return node


def left_rotate(n0):
    n1 = n0.right
    n2 = n1.left

    n1.left = n0
    n0.right = n2

    n0.height = 1 + max(height(n0.left), height(n0.right))
    n1.height = 1 + max(height(n1.left), height(n1.right))

    return n1


def right_rotate(n0):
    n1 = n0.left
    n2 = n1.right

    n1.right = n0
    n0.left = n2

    n0.height = 1 + max(height(n0.left), height(n0.right))
    n1.height = 1 + max(height(n1.left), height(n1.right))

    return n1


def rotate(node):
    bf = balance_factor(node)

    if bf > 1 and balance_factor(node.left) >= 0:
        node = right_rotate(node)

    if bf < -1 and balance_factor(node.right) <= 0:
        node = left_rotate(node)

    if bf > 1 and balance_factor(node.left) < 0:
        node.left = left_rotate(node.left)
        node = right_rotate(node)

    if bf < -1 and balance_factor(node.right) > 0:
        node.right = right_rotate(node.right)
        node = left_rotate(node)

    return node


def insert(node, data):
    if node is None:
        return Node(data)
    elif data < node.data:
        node.left = insert(node.left, data)
    else:
        node.right = insert(node.right, data)

    node.height = 1 + max(height(node.left), height(node.right))
    return rotate(node)


def delete(node, data):
    if node is None:
        return None

    if data < node.data:
        node.left = delete(node.left, data)
    elif data > node.data:
        node.right = delete(node.right, data)
    else:
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left

        min_node = min_value_node(node.right)
        node.data = min_node.data
        node.right = delete(node.right, min_node.data)

    node.height = 1 + max(height(node.left), height(node.right))
    return rotate(node)


def search(node, data):
    if node is None or node.data == data:
        return node

    if node.data < data:
        return search(node.right, data)

    return search(node.left, data)


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # It is better not to allow duplicates in a binary tree
        # If duplicates are absolutely necessary, it is better to make the data section of a node to be an array,
        # but search the tree by the key
        self.root = insert(self.root, data)

    def delete(self, data):
        self.root = delete(self.root, data)

    def search(self, data):
        return search(self.root, data)

    def validate_AVL(self):
        validate_AVL(self.root)

    def print_tree(self):
        print_tree(self.root)


if __name__ == '__main__':
    tree = AVLTree()

    print('Test insertions')
    for i in range(1, 101):
        tree.insert(i)
        tree.validate_AVL()

    print()
    print('Test deletions')
    for i in range(51, 101):
        tree.delete(i)
        tree.validate_AVL()

    print()
    print('Test search')
    for data in (51, 20):
        node = tree.search(data)
        print(f'{data} is{' not ' if node is None else ' '}found')

    # tree.print_tree()
