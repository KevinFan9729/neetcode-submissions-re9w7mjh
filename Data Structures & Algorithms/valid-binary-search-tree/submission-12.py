# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # the key here is to make sure those validities are recursive
        # we need to make sure that every subtrees are valid
        # naturally we will do this with dfs?
        # Time O(n)
        # Space O(h)
        def dfs(root, min_bound, max_bound, ):
            if not root:
                return True
            if not(min_bound < root.val < max_bound):
                return False
            # Going left
            # If you go to root.left, 
            # every value in that left subtree must be:
            # < root.val (BST rule)

            # Going right
            # If you go to root.right, 
            # every value in that right subtree must be:
            # > root.val (BST rule)
            # samp;e of a bad tree
            #  5
            # / \
            # 1   7
            #     /
            #     4
            # when we are at node 4, it will return False as the min_bound is 5

            return dfs(root.left, min_bound, root.val) and dfs(root.right, root.val, max_bound)
        ans = dfs(root, float('-inf'), float('inf'))
        return ans
        