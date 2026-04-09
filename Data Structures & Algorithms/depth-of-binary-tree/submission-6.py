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
        # the idea is we keep a global max length variable called depth
        # go through all path in the tree
        # update the depth as we go
        # Time O(n)
        # Space O(h)
        depth = 0
        def dfs(root, curr_depth):
            nonlocal depth
            if not root:
                # we finished one path
                depth = max(depth, curr_depth) 
                return
            # go one level deeper
            dfs(root.left, curr_depth+1)
            dfs(root.right, curr_depth+1)
        
        dfs(root, 0)
        return depth
        