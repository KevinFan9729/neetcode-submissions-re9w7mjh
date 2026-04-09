# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # The idea is that we use a special height function
    # this function will compute height at all nodes AND
    # it will return -1 if the tree is not balanced
        # left or right is marked at -1 (meaing sutree not balanced)
        # left-right > 1 (core condition for not balanced)
    # Time O(n)
    # Space O(h)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True
        def heightCheck(root):
            nonlocal ans
            if not ans:
                return -1
            if not root:
                return 0
            left = heightCheck(root.left)
            right = heightCheck(root.right)
            if left == -1 or right == -1:
                ans = False
                return -1
            if abs(left - right) > 1:
                ans = False
                return -1
            
            return 1 + max(left, right)
        heightCheck(root)
        return ans
            