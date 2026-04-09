from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # oh the key word is bineary 'search' tree
        # meaning that left nodes are smaller than current
        # right nodes are biiger than current
        # there are no equal nodes as all node values are unqiue (stated in the question)
        # current node is the LCA if it is between p and q (we will go through depth)
        # I guess we can solve with dfs and bfs?
        # Time O(n)
        # Space O(1)
        if p.val > q.val:
            p, q = q, p # swap if p.val is smaller than q.val
        node = root # we can do this as we just care about one node at the time
        # our logic will ensure that go to the correct subtree
        while True:
            if p.val <= node.val <= q.val:
                return node
            elif p.val > node.val:
                if node.right:
                    node = node.right
            elif q.val < node.val:
                if node.left:
                    node = node.left
        return