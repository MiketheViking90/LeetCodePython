from typing import List

from ds.tree_node import TreeNode


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        trav = []
        self.traverse(root, trav)
        return trav

    def traverse(self, root, trav):
        if not root:
            return

        self.traverse(root.left, trav)
        trav.append(root.val)
        self.traverse(root.right, trav)