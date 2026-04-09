# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # we can just do an indorder treversal and to generate a sorted list
        # then the k-1 indexed item will be the answer
        sorted_ls = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            sorted_ls.append(root.val)
            if len(sorted_ls) == k:
                return
            dfs(root.right)
        
        dfs(root)
        return sorted_ls[k-1]