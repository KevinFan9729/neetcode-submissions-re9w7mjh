# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # use dfs to find out the height of the left and right subtree
        # use a variable to track if the height difference is more than 1
        # base case if node is None, we will return 0

        balanced = True
        def dfs(node):
            nonlocal balanced
            if not node:
                return 0
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            if abs(left_height - right_height) >1:
                balanced = False
                return -1
            if balanced == False:
                return -1
            return max(left_height, right_height) + 1
        
        dfs(root)
        return balanced
        