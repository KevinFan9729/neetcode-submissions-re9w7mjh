# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # if we go to the left tree, all nodes inside of the left tree must be less than its ancestor
        # if we go to the right tree, all nodes inside of the righ tree must be MORE than its ancestor
        # Time O(n)
        # Space O(h)
        def validate(root, minVal, maxVal):
            if not root:
                return True
            if not (minVal < root.val < maxVal):
                return False
            checkLeft = validate(root.left, minVal, root.val)
            if not checkLeft:
                return False
            checkRight = validate(root.right, root.val, maxVal)
            return checkLeft and checkRight
        
        res = validate(root, float('-inf'), float('inf'))
        return res