from collections import OrderedDict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def make_tree() -> TreeNode:
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    n8 = TreeNode(18)

    n5.left = n2
    n5.right = n7
    n2.left = n1
    n2.right = n3
    n3.right = n4
    n7.left = n6
    n7.right = n8

    return n5

def print_tree(root: TreeNode):
    lvl_to_vals = OrderedDict()
    traverse(root, lvl_to_vals, 0)
    print(lvl_to_vals)

def traverse(root, lvl_to_vals, lvl):
    if not root:
        return

    cur_vals = lvl_to_vals.get(lvl, [])
    cur_vals.append(root.val)
    lvl_to_vals[lvl] = cur_vals
    traverse(root.left, lvl_to_vals, lvl+1)
    traverse(root.right, lvl_to_vals, lvl+1)

