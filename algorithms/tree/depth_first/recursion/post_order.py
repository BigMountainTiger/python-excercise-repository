# https://www.w3schools.com/dsa/dsa_algo_binarytrees_postorder.php

from utils import utilities


def traverse(node):
    if node is None:
        return

    traverse(node.left)
    traverse(node.right)

    # Post-order Traversal works by recursively doing a Post-order Traversal of the left subtree and the right subtree,
    # followed by a visit to the root node.
    # It is used for deleting a tree, post-fix notation of an expression tree, etc.
    print(node.data)


if __name__ == '__main__':

    # Build an example tree
    tree = utilities.build_tree()
    traverse(tree)
