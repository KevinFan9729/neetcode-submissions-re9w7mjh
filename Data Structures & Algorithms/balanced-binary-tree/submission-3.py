# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # we need a function to compute the height of the tree?
        # Time O(n^2) as computing height is O(n) and it needs to be nested
        # Space O(h) at any moment, the max stack depth is essentially checkBalanced depth + one height depth,
        # which is still O(h)
        def height(root):
            if not root:
                return 0
            return 1 + max(height(root.left), height(root.right))
        def checkBalanced(root):
            if not root:
                return True
            left_height = height(root.left)
            right_height = height(root.right)

            if abs(left_height - right_height) > 1:
                return False
            return checkBalanced(root.left) and checkBalanced(root.right)

        return checkBalanced(root)
            