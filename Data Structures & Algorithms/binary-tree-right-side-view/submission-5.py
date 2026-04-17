# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # dfs
        # DFS with preorder-style traversal biased to the right
        # Time O(n)
        # Space O(h)
        res = []
        def dfs(root, level):
            if not root:
                return
            if len(res) < level: # add the first element of the level to res
                res.append(root.val)
            dfs(root.right, level+1)
            dfs(root.left, level +1)
        dfs(root, 1)
        return res