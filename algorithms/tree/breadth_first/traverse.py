import queue
from utils import utilities


def traverse(tree):
    # https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
    # Breadth first traverse requires an FIFO queue
    q = queue.Queue()
    q.put(tree)

    while not q.empty():
        node = q.get()

        # We can make decisions by the data
        # just print it for now
        print(node.data)

        if node.left is not None:
            q.put(node.left)
        if node.right is not None:
            q.put(node.right)


if __name__ == '__main__':

    # Build an example tree
    tree = utilities.build_tree()
    traverse(tree)
