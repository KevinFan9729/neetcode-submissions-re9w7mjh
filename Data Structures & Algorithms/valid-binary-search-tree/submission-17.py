# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # valdiating the bst must be recursive
        # like every subtrees need to satisfy the structure of bst
        # Time O(n)
        # Space O(n)

        def dfs(root, minVal, maxVal):
            if not root:
                return True
            if root.val <= minVal or root.val >= maxVal:
                return False

            # check the left tree, nodes in the left tree must be smaller than maxVal (curr)
            leftCheck = dfs(root.left, minVal, root.val)
            if not leftCheck: # if left is false stop checking
                return False
            # check the right tree, nodes in the left tree must be lager than minVal (curr)
            rightCheck = dfs(root.right, root.val, maxVal)
            
            return leftCheck and rightCheck
        

        return dfs(root, -float("inf"), float("inf"))