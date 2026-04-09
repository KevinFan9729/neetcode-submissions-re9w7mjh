# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # Both p and q are smaller than the current node: This means that the LCA must be in the left subtree.
        # Both p and q are larger than the current node: This means that the LCA must be in the right subtree.
        # p and q are on different sides of the current node 
            #(or one of them is equal to the current node): This means the current node is the LCA.
        ans = None
        def dfs(node):
            nonlocal ans
            if not node:
                return None
            if p.val < node.val and q.val < node.val:
                dfs(node.left)
            if p.val > node.val and q.val > node.val:
                dfs(node.right)
            if (p.val >= node.val and q.val <= node.val) or (p.val <= node.val and q.val >= node.val):
                ans = node
                return node
            return ans
        ans = dfs(root)
        return ans 