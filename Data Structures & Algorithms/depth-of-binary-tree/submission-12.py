# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # it seems like we are counting number of nodes
        # we want to go deep so we use dfs
        # even tough I think we can also do bfs and count the level number
        # depth = 0

        def dfs(root):
            # nonlocal depth
            if not root:
                return 0 

            depth = 0
            left = 1+ dfs(root.left)
            right = 1+ dfs(root.right)

            depth = max(left, right)
            return depth

        res = dfs(root)
        return res