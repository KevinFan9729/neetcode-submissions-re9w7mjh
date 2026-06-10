# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # use dfs
        # say if we check the left subtree has p and q, lca is in the left
        # if we check the right subtree has p and q, lca is in the right
        # if one is found in the right and one is found in the left then current node is lca
        # Time O(n)
        # Space O(h)

        def dfs(node):
            if not node:
                return
            
            if node == p:
                return node
            if node == q:
                return node
            
            leftCheck = dfs(node.left)
            rightCheck = dfs(node.right)

            if leftCheck and rightCheck:
                # p and q are in both sides
                return node
            
            return leftCheck or rightCheck

        res = dfs(root)
        return res