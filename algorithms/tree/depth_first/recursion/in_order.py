# https://www.w3schools.com/dsa/dsa_algo_binarytrees_inorder.php

from utils import utilities


def traverse(node):
    if node is None:
        return

    traverse(node.left)

    # In-order Traversal does a recursive In-order Traversal of the left subtree,
    # visits the root node, and finally, does a recursive In-order Traversal of the right subtree.
    # This traversal is mainly used for Binary Search Trees where it returns values
    # -- in ascending order.
    print(node.data)
    
    traverse(node.right)


if __name__ == '__main__':

    # Build an example tree
    tree = utilities.build_tree()
    traverse(tree)
