from collections import OrderedDict
from typing import List

from ds.tree_node import TreeNode, print_tree, make_tree


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        lvl_to_vals = OrderedDict()
        self.traverse(root, lvl_to_vals, 0)
        vals = []
        for lvl_to_val in lvl_to_vals.values():
            vals.append(lvl_to_val)
        return vals

    def traverse(self, root, lvl_to_vals, lvl):
        if not root:
            return

        cur_vals = lvl_to_vals.get(lvl, [])
        cur_vals.append(root.val)
        lvl_to_vals[lvl] = cur_vals
        self.traverse(root.left, lvl_to_vals, lvl+1)
        self.traverse(root.right, lvl_to_vals, lvl+1)

tree = make_tree()
lst = Solution().levelOrder(tree)
print(lst)