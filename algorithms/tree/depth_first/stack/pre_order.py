
import queue
from utils import utilities


def traverse(tree):
    stack = queue.LifoQueue()
    stack.put(tree)

    while not stack.empty():
        node = stack.get()
        print(node.data)

        # put right first so left is poped first
        if node.right is not None:
            stack.put(node.right)
        if node.left is not None:
            stack.put(node.left)


if __name__ == '__main__':

    # Build an example tree
    tree = utilities.build_tree()
    traverse(tree)
