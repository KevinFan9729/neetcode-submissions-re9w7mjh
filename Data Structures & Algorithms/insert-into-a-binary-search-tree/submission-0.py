# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # just navigate the tree and find a leaf node position
        # Time O(h)
        # Space O(h)

        def dfs(root): # return the current node
            if not root: # when current node is None we need to insert
                return TreeNode(val)
            if root.val < val:
                root.right = dfs(root.right)
            elif root.val > val:
                root.left= dfs(root.left)
            return root
        res = dfs(root)
        return res