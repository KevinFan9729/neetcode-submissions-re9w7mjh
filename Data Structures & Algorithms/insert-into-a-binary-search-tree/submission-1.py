# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # we need to naviagte to the point of insertion
        # find a leaf pos to do the insertion
        # Time O(n)
        # Space O(1)
        if not root:
            root = TreeNode(val)
            return root
        curr = root
        while curr:
            if curr.val > val:
                if curr.left:
                    curr = curr.left
                else:
                    # we found a leaf pos
                    curr.left = TreeNode(val)
                    return root
            else:
                if curr.right:
                    curr = curr.right
                else:
                    # we found a leaf node
                    curr.right = TreeNode(val)
                    return root
        return root