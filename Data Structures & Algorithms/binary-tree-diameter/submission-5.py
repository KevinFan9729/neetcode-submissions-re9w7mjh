# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # we may want to try a dfs approach
        # we find the depth of the left sub tree 
        # we find the depth of the right sub tree
        # our diameter is the sum of left and right height
        # dfs(curr_node)
        # O(n)
        # O(h) space
        diameter = 0
        def dfs(curr_node):
            nonlocal diameter
            if not curr_node:
                return 0
            left_height = dfs(curr_node.left)
            right_height = dfs(curr_node.right)
            diameter = max(diameter, left_height + right_height) # diameter is the  longest path
            # height of the tree (subtree) is the max between height of 
            # left tree and the height of right tree + 1,
            # which this 1 is the height of the current node
            return max(left_height, right_height) + 1 
        dfs(root)
        return diameter
