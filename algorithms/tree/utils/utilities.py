import queue


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


def pre_order_print(node):
    if node is None:
        return

    print(f'data - {node.data} | height - {node.height}')
    pre_order_print(node.left)
    pre_order_print(node.right)


def in_order_print(node):
    if node is None:
        return

    in_order_print(node.left)
    print(f'data - {node.data} | height - {node.height}')
    in_order_print(node.right)


def post_order_print(node):
    if node is None:
        return

    post_order_print(node.left)
    post_order_print(node.right)
    print(f'data - {node.data} | height - {node.height}')


def breadth_first_print(root):
    q = queue.Queue()
    q.put(root)

    while not q.empty():
        node = q.get()
        print(f'data - {node.data} | height - {node.height}')

        if node.left is not None:
            q.put(node.left)
        if node.right is not None:
            q.put(node.right)


def build_tree():
    # build an example tree

    # root
    root = Node('Root')

    # A, B
    A = Node('A')
    B = Node('B')
    root.left = A
    root.right = B

    # A children
    A1 = Node('A1')
    A2 = Node('A2')
    A.left = A1
    A.right = A2

    A11 = Node('A11')
    A12 = Node('A12')
    A1.left = A11
    A1.right = A12

    A21 = Node('A21')
    A22 = Node('A22')
    A2.left = A21
    A2.right = A22

    # B children
    B1 = Node('B1')
    B2 = Node('B2')
    B.left = B1
    B.right = B2

    B11 = Node('B11')
    B12 = Node('B12')
    B1.left = B11
    B1.right = B12

    B21 = Node('B21')
    B22 = Node('B22')
    B2.left = B21
    B2.right = B22

    return root
