# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # oh the key word is bineary 'search' tree
        # meaning that left nodes are smaller than current
        # right nodes are biiger than current
        # there are no equal nodes as all node values are unqiue (stated in the question)
        # current node is the LCA if it is between p and q (we will go through depth)
        # I guess we can solve with dfs and bfs?
        # Time O(n)
        # Space O(h) # due to the recursive stack
        if p.val > q.val:# make sure that value of p is smaller than q, otherwise swap
            p, q = q, p
        def dfs(root):
            if not root:
                return
            if p.val <= root.val <= q.val:
                return root
            if p.val > root.val:
                return dfs(root.right)
            if q.val < root.val:
                return dfs(root.left)
        
        ans = dfs(root)
        return ans
