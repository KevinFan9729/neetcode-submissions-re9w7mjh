# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def findLCA(curr, p, q):
            if not curr or curr.val == p.val or curr.val == q.val:
                return curr
            left = findLCA(curr.left, p, q)
            right = findLCA(curr.right, p,q)
            if left and right: # if left and right are not null, we have found the middle!
                return curr
            # if l is null it means p and q are on the right subtree, return r
            if not left:
                return right
            # if r is null it means p and q are on the left subtree, return l
            if not right:
                return left
        
        ans = findLCA(root, p, q)
        return ans