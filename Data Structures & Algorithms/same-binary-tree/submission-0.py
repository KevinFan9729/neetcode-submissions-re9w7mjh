# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 and root2:
                return False
            if  root1 and not root2:
                return False
            
            if root1.val != root2.val:
                return False
            left_check = dfs(root1.left, root2.left)
            right_check = dfs(root1.right, root2.right)

            return left_check and right_check
        ans = dfs(p,q)
        return ans