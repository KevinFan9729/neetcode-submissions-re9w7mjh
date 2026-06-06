# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # the height of the left tree +
        # the height of the right tree
        # is the diameter
        # Time O(n)
        # Space O(h)
        diameter = 0
        def findHeight(root):
            nonlocal diameter
            if not root:
                return 0
            leftH = findHeight(root.left)
            rightH = findHeight(root.right)
            height = 1+max(leftH, rightH)
            diameter = max(diameter, leftH+rightH)
            return height
        findHeight(root)
        return diameter