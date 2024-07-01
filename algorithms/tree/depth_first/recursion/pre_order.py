# https://www.w3schools.com/dsa/dsa_algo_binarytrees_preorder.php

from utils import utilities


def traverse(node):
    if node is None:
        return

    # Pre-order Traversal is done by visiting the root node first,
    # then recursively do a pre-order traversal of the left subtree,
    # followed by a recursive pre-order traversal of the right subtree.
    # It's used for 
    # creating a copy of the tree, prefix notation of an expression tree, etc.
    print(node.data)

    traverse(node.left)
    traverse(node.right)


if __name__ == '__main__':

    # Build an example tree
    tree = utilities.build_tree()
    traverse(tree)
