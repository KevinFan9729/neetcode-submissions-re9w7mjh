from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # dfs apporch navigate to the end to each route 
        # once at the leaf, count the length of the path

        def dfs(node):
            if not node:
                return 0
            
            left_tree_length = dfs(node.left)
            right_tree_length = dfs(node.right)
            max_len = max(left_tree_length,right_tree_length) +1
            return max_len
        return dfs(root)
             
                
        