from typing import Self, Optional
import random


class Node:
    def __init__(self, data: int):
        self.red: bool = True

        # node data
        self.data: int = data
        self.parent: Optional[Self] = None
        self.left: Optional[Self] = None
        self.right: Optional[Self] = None

    def assign_left_child(self, node: Self):
        self.left = node
        if node is not None:
            node.parent = self

    def assign_right_child(self, node: Self):
        self.right = node
        if node is not None:
            node.parent = self


def is_red(node: Optional[Node]) -> bool:
    return True if node is not None and node.red else False


def is_black(node: Optional[Node]) -> bool:
    return True if node is None or not node.red else False


def min_value_node(node: Optional[Node]) -> Optional[Node]:
    if node is None:
        return None

    while node.left is not None:
        node = node.left

    return node


def flip_color(node: Node):
    node.red = True
    node.left.red = False
    node.right.red = False


def fix_color(node: Node):
    node.red = False
    node.left.red = True
    node.right.red = True


def left_rotate(n0: Node) -> Node:
    n1 = n0.right
    n2 = n1.left

    n1.assign_left_child(n0)
    n0.assign_right_child(n2)
    n1.parent = None

    return n1


def right_rotate(n0: Node) -> Node:
    n1 = n0.left
    n2 = n1.right

    n1.assign_right_child(n0)
    n0.assign_left_child(n2)
    n1.parent = None

    return n1


def rotate(node: Node, reds: str) -> Node:

    match reds:
        case 'll':
            node = right_rotate(node)
        case 'rr':
            node = left_rotate(node)
        case 'lr':
            node.assign_left_child(left_rotate(node.left))
            node = right_rotate(node)
        case 'rl':
            node.assign_right_child(right_rotate(node.right))
            node = left_rotate(node)

    return node


def print_tree(node: Optional[Node]):
    if node is None:
        return

    print_tree(node.left)
    print(f'data = {node.data}, color = {'red' if node.red else 'black'}')
    print_tree(node.right)


def validate_RedBlack(node: Optional[Node]) -> tuple[int, int]:
    if node is None:
        return 0, 1

    l_height, l_black_height = validate_RedBlack(node.left)
    r_height, r_black_height = validate_RedBlack(node.right)

    if l_black_height != r_black_height:
        raise Exception('Black height is not equal')

    if is_red(node) and (is_red(node.left) or is_red(node.right)):
        raise Exception('Consecutive red node detected')

    return max(l_height, r_height) + 1, l_black_height + 1 if is_black(node) else l_black_height


def insert(node: Optional[Node], data) -> tuple[Node, str]:
    if node is None:
        return Node(data), ''

    if data < node.data:
        child, reds = insert(node.left, data)
        node.assign_left_child(child)
        side = 'l'
    else:
        child, reds = insert(node.right, data)
        node.assign_right_child(child)
        side = 'r'

    reds = '' if is_black(child) else side + reds

    if len(reds) < 2:
        return node, reds

    aunt = node.right if side == 'l' else node.left
    if is_red(aunt):
        flip_color(node)
        return node, ''

    node = rotate(node, reds)
    fix_color(node)

    return node, ''


def fix_black(node: Node, incident: str) -> tuple[Node, bool]:
    # Sibling of the incident node is black

    balanced = True
    if incident == 'l':
        S = node.right
        SL, SR = S.left, S.right

        if is_red(SR):
            node.red, S.red, SR.red = False, node.red, False
            node = left_rotate(node)
        elif is_red(SL):
            S.red, SL.red = True, False
            S = right_rotate(S)
            node.right = S

            node.red, S.red, S.right.red = False, node.red, False
            node = left_rotate(node)
        else:
            S.red = True
            if is_red(node):
                node.red = False
            else:
                balanced = False

    else:
        S = node.left
        SL, SR = S.left, S.right

        if is_red(SL):
            node.red, S.red, SL.red = False, node.red, False
            node = right_rotate(node)
        elif is_red(SR):
            S.red, SR.red = True, False
            S = left_rotate(S)
            node.left = S

            node.red, S.red, S.left.red = False, node.red, False
            node = right_rotate(node)
        else:
            S.red = True
            if is_red(node):
                node.red = False
            else:
                balanced = False

    return node, balanced


def fix_red(node: Node, incident: str) -> tuple[Node, bool]:
    # Sibling of the incident node is red

    if incident == 'l':
        S = node.right
        node.red, S.red = True, False
        node = left_rotate(node)

        node.left, _ = fix_black(node.left, 'l')
    else:
        S = node.left
        node.red, S.red = True, False
        node = right_rotate(node)

        node.right, _ = fix_black(node.right, 'r')

    return node, True


def fix_deletion(node: Node, incident: str) -> tuple[Node, bool]:
    S = node.right if incident == 'l' else node.left
    return fix_black(node, incident) if is_black(S) else fix_red(node, incident)


def delete(node: Optional[Node], data: int) -> tuple[Optional[Node], bool]:
    if node is None:
        return None, True

    if data < node.data:
        incident = 'l'
        node.left, balanced = delete(node.left, data)
    elif data > node.data:
        incident = 'r'
        node.right, balanced = delete(node.right, data)
    else:
        deletable = False
        if node.left is None:
            deletable, child = True, node.right
        elif node.right is None:
            deletable, child = True, node.left

        if deletable:
            if is_red(node):
                return child, True
            else:
                if is_red(child):
                    child.red = False
                    return child, True
                else:
                    return child, False

        min_node = min_value_node(node.right)
        node.data = min_node.data
        incident = 'r'
        node.right, balanced = delete(node.right, min_node.data)

    if not balanced:
        node, balanced = fix_deletion(node, incident)

    return node, balanced


class RedBlackTree:
    def __init__(self):
        self.root: Node = None

    def insert(self, data: int):
        self.root, _ = insert(self.root, data)
        self.root.red = False

    def delete(self, data: int):
        self.root, _ = delete(self.root, data)
        if self.root is not None:
            self.root.red = False

    def print_tree(self):
        print_tree(self.root)

    def validate_RedBlack(self):
        root = self.root

        validate_RedBlack(root)
        if is_red(root):
            raise ('root is red')


if __name__ == '__main__':

    tree = RedBlackTree()

    numbers = [i for i in range(1, 101)]
    random.shuffle(numbers)
    for i in numbers:
        tree.insert(i)

    numbers = [i for i in range(1, 51)]
    random.shuffle(numbers)
    for i in numbers:
        tree.delete(i)

    # validate_RedBlack()
    tree.validate_RedBlack()

    print('print tree')
    tree.print_tree()
