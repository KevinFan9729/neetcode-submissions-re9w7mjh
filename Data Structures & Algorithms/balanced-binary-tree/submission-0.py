# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)

            if abs(leftHeight - rightHeight) >1:
                res = False
            return max(leftHeight, rightHeight) + 1 # compute the height of the current node
        dfs(root)
        return res