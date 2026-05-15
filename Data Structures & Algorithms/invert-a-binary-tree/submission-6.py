# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # we can do this recursively 
        # just need to make sure that we track the original connection with tmp
        # Time O(n)
        # Space O(n)
        def dfs(root):
            if not root:
                return
            
            orgLeft = root.left
            root.left = root.right
            root.right = orgLeft

            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return root