# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case
            # if the node we have is None, we need to stop
        if not root:
            return None
        tmp = root.left # original left tree
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(tmp)  # revert the original left tree
        
        return root