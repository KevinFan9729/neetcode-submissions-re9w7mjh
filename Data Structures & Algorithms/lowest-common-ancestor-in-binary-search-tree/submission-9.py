# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # lca is bewteen p and q
        # we can ensure that value of p is smaller to q
        # use a dfs to find the lca which is bewteen pval and qval
        # Time O(n)
        # Space O(h)
        pVal, qVal = p.val, q.val

        if pVal > qVal:
            pVal, qVal = qVal, pVal

        def dfs(root):
            if not root:
                return
            if pVal <= root.val <= qVal:
                return root
            lca = root
            if root.val < pVal:
                lca = dfs(root.right)
            else:
                lca = dfs(root.left)
            return lca

        res = dfs(root)
        return res

