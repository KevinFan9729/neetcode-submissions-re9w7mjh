# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # we need a function to compute the height of the tree?
        # Time O(n) due to memo; no repeated work
        # Space O(h+n) as memo takes extra space
        memo = {}
        def height(root):
            if not root:
                return 0
            if root in memo:
                return memo[root]
            h = 1 + max(height(root.left), height(root.right))
            if root not in memo:
                memo[root] = h
            return h
        def checkBalanced(root):
            if not root:
                return True
            left_height = height(root.left)
            right_height = height(root.right)

            if abs(left_height - right_height) > 1:
                return False
            return checkBalanced(root.left) and checkBalanced(root.right)

        return checkBalanced(root)
            