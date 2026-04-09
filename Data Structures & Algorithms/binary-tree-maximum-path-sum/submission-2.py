# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # for a path, we can have only one splitting node
        # we have a dfs function that return what is the max path sum WITHOUT splitting
        # O(n) in time as we just navigate all nodes once
        # O(h) in space
        maxSum = float("-inf")
        def dfs(node):
            nonlocal maxSum
            if not node:
                return 0
            leftPath = dfs(node.left)
            rightPath = dfs(node.right)
            leftPath = max(leftPath, 0)
            rightPath = max(rightPath, 0)

            # check WITH splitting, what is the pathsum 
            maxSum = max(maxSum, node.val + leftPath + rightPath)

            # return WITHOUT splitting, what is the pathsum
            return node.val + max(leftPath, rightPath)
        dfs(root)
        return maxSum