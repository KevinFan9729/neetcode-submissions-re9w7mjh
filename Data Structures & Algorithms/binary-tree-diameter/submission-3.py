# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # use dfs, diameter at any node is the sum of the heights 
        # of its left and right subtrees.
        max_len = 0
        def dfs(root):
            nonlocal max_len
            if not root:
                return 0
            
            left_subtree_len = dfs(root.left)
            right_subtree_len = dfs(root.right)
            max_len = max(max_len, left_subtree_len + right_subtree_len)
            height_at_node = max(left_subtree_len, right_subtree_len) +1
            # Return the height of the subtree rooted at the current node
            return height_at_node
        dfs(root)
        return max_len

        