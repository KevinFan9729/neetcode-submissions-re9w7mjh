# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # bst defination is recursive
        # left subtree needs to be smaller than root
        # right subtree needs to be bigger than root
        # Time O(n)
        # Space O(n)
        def valid(root, lowerBound, upperBound):
            if not root:
                return True
            if not (lowerBound < root.val < upperBound):
                return False
            
            leftCheck = valid(root.left, lowerBound, root.val)
            rightCheck = valid(root.right,  root.val, upperBound)

            return leftCheck and rightCheck

        res = valid(root, float('-inf'), float('inf'))
            
            
        return res