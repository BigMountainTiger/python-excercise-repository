
# https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/

import queue
from utils import utilities


def traverse(tree):
    current = tree
    stack = queue.LifoQueue()

    while True:
        if current is not None:
            stack.put(current)

            # push the left
            current = current.left
        elif not stack.empty():
            current = stack.get()

            # Process the data
            print(current.data)

            # push the right
            current = current.right
        else:
            # Done
            break


if __name__ == '__main__':

    # Build an example tree
    tree = utilities.build_tree()
    traverse(tree)
