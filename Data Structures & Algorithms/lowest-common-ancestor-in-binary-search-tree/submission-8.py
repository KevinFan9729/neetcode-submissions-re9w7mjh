# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # this is a bst, so it has this ordered structure
        # lca is bewteen p and q
        # in a BST, the LCA is the first node whose value lies between p.val and q.val inclusive.
        # Time O(n)
        # Space O(1)

        if p.val > q.val:
            p,q = q,p
        curr = root
        while curr:
            if p.val <= curr.val <= q.val:
                return curr
            elif curr.val < p.val:
                curr = curr.right
            elif curr.val > q.val:
                curr = curr.left

        return curr