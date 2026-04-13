# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # valdiation of bst is recursive
        # like all subtrees need to satisfy the bst structure
        # on the left tree, we need to keep track of a upper and no tree node should be more than this upper
            # need to tighten the upper bound with min(current, upper)
        # on the left tree, we need to keep track of a lower and no tree node should be less than this lower
            # need to tighten the lower bound with max(current, lower)
        # Time O(n)
        # Space O(n)
        def dfs(root, lower, upper):
            if not root:
                return True

            if not(lower < root.val < upper):
                return False
            # as we go to the left, left node must be smaller than upper
            leftCheck = dfs(root.left, lower, min(upper, root.val))
            # as we go to the right, right node must be bigger than lower
            rightCheck = dfs(root.right, max(lower, root.val), upper)
            
            return leftCheck and rightCheck
        
        res = dfs(root, -1001, 1001) # as -1000 <= Node.val <= 1000 
        return res
                