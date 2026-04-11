# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # the Lowest Common Ancestor is between the target nodes
        # use dfs to find a node that is between p and q
        # Time O(n)
        # Space O(h)
        pval, qval = p.val, q.val
        if pval > qval: # make sure pval is smaller than qval
            pval, qval = qval, pval
        def dfs(root):
            if not root:
                return
            if pval <= root.val <= qval:
                return root
            if root.val < pval:
                return dfs(root.right)
            elif root.val > qval:
                return dfs(root.left)
            
        lca = dfs(root)
        return lca