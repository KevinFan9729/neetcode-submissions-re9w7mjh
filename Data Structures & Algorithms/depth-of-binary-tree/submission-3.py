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
            max_len = 0
            if not node:
                return 0
            
            left_tree_length = dfs(node.left) + 1
            right_tree_length = dfs(node.right) + 1
            max_len = max(left_tree_length,right_tree_length,max_len)
            return max_len
        ans = dfs(root)
        return ans
             
                
        