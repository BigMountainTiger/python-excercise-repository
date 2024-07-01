# https://www.geeksforgeeks.org/iterative-postorder-traversal/

import queue
from utils import utilities


# 2 stack implementation
def traverse(tree):
    s1 = queue.LifoQueue()
    s2 = queue.LifoQueue()

    s1.put(tree)

    while not s1.empty():
        node = s1.get()

        s2.put(node)
        if node.left is not None:
            s1.put(node.left)
        if node.right is not None:
            s1.put(node.right)

    while not s2.empty():
        node = s2.get()
        print(node.data)


if __name__ == '__main__':

    # Build an example tree
    tree = utilities.build_tree()
    traverse(tree)
