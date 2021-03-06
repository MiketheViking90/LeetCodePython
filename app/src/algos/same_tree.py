from ds.tree_node import TreeNode


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if bool(p) ^ bool(q):
            return False

        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
