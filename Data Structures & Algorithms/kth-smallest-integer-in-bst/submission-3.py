# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # becuase this is a bst
        # the values are sorted
        # Time O(n)
        # Space O(n)
        count = 0
        ans = -1
        def dfs(root):
            nonlocal count, ans
            if not root:
                return
            dfs(root.left)
            if count == k:
                return
            ans = root.val
            count +=1
            if count == k:
                return
            dfs(root.right)
        
        dfs(root)
        return ans