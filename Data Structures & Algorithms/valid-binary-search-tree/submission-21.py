# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # the condition is recursive
        # so say if we go the to either of the subtree
        # the conditions of the bst needs to hold
        # if we go into say the left subtree, we track an ancestor which must be greater than any nodes in the left
        # if we go into the right subtree, we track an ancestor which must be smaller than any nodes in the right
        # dfs(root, minVal, maxVal)
        # Time O(n)
        # Space O(n)

        def dfs(root,minVal, maxVal):
            if not root:
                return True
            
            if not minVal<(root.val)<maxVal:
                return False
            
            leftCheck = dfs(root.left, minVal, root.val)
            rightCheck = dfs(root.right, root.val, maxVal)
            return leftCheck and rightCheck

        res = dfs(root, float('-inf'), float('inf'))
        return res