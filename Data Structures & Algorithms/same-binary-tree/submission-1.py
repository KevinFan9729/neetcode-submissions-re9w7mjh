# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 and root2:
            return False
        if  root1 and not root2:
            return False
        
        if root1.val != root2.val:
            return False
        left_check = self.isSameTree(root1.left, root2.left)
        right_check = self.isSameTree(root1.right, root2.right)

        return left_check and right_check