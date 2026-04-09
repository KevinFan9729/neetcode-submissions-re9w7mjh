from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # maybe dfs but right to left?
        # res have the right node at one level if available
        # actually res just needs to get the first element in the level in this setup
        # Time O(n)
        # Space O(n)
        res = []
        def dfs(root, depth):
            nonlocal res
            if not root:
                return
            if depth == len(res): # we are at the first of the level
                res.append(root.val)
            # we prioritize going to he right
            dfs(root.right, depth+1)
            dfs(root.left, depth+1)
        dfs(root,0)
        return res
            
