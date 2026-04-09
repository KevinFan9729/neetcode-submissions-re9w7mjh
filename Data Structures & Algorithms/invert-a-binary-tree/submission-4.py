# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # we want to left node to become the right node and vice versa
        # needs a tmp to store the assigned
        # Time O(n) we need to go through all n nodes
        # Space O(h) depth of the tree
        def reverse(root):
            if not root:
                return
            temp = root.left
            root.left = root.right
            root.right = temp
            reverse(root.left) # reverse the left tree
            reverse(root.right) # reverse the right tree
        reverse(root)
        return root