from typing import Optional

from ds.tree_node import TreeNode


class Solution:
    def invertTree(self, root: TreeNode) -> Optional[TreeNode]:
        if not root:
            return None

        root.left = self.invertTree(root.right)
        root.right = self.invertTree(root.left)

        return root
