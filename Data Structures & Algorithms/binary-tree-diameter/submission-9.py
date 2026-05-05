# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # we need to find the height of the subtree
        # diameter OF through a node root is the left height + right height
        # global diameter is the max of all
        # Time O(n)
        # Space O(n)
        diameter = 0

        def findHeight(root):
            nonlocal diameter
            if not root:
                return 0

            leftH = findHeight(root.left)
            rightH = findHeight(root.right)

            diameter = max(diameter, leftH +rightH)
            
            return 1 + max(leftH, rightH)
        findHeight(root)
        return diameter