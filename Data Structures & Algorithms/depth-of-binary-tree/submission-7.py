# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # as we are going deep
        # we need dfs
        # Time O(n)
        # Space O(h)
        depth = 0
        def dfs(root):
            nonlocal depth
            if not root:
                return 0
            # depth is 1+ the max(depth of the left tree and right tree)
            depth = 1 + max(dfs(root.left), dfs(root.right))
            return depth
        
        dfs(root)
        return depth
        