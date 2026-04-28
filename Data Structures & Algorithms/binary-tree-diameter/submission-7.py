# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # What is the longest path that passes through this node as the highest turning point?
        # then we can go through left and right
        # the result at the root the left height + right height
        # dfs tells us 
        # starting from this node, what is the longest downward height of this subtree?
        # Time O(n)
        # Space O(n)
        maxHeight = 0
        def dfs(root):
            nonlocal maxHeight
            if not root:
                return 0

            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)
            height = 1+max(leftHeight, rightHeight)
            maxHeight = max(leftHeight+rightHeight, maxHeight)
            return height
        dfs(root)
        return maxHeight