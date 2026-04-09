# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # the trees are the same if
            # their structure are the same
            # their tree node values are the same at the respective pos
        # Time O(n)
        # Space O(h)
        # dfs and bfs can all solve this problem
        def dfs(tree1, tree2):
            if not tree1 and not tree2:
                return True
            if tree1 and not tree2:
                return False
            if tree2 and not tree1:
                return False
            if tree1.val != tree2.val:
                return False
            # check left tree
            left_check = dfs(tree1.left, tree2.left)
            # check right tree
            right_check = dfs(tree1.right, tree2.right)
            return left_check and right_check
        ans = dfs(p,q)
        return ans