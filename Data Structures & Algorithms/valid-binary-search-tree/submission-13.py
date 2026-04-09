# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # the key here is to make sure those validities are recursive
        # we need to make sure that every subtrees are valid
        # naturally we will do this with dfs?
        # we can also do this with bfs, we just need to record bounds
        # Time O(n)
        # Space O(w)
        # another thing for a bst is that if we do
        # In-order traversal (Left -> Root -> Right)
        # values will be strictly increasing,
        # this can be used to check if the bst is valid or not as well
        q = deque()
        # (node, min_bound, max_bound)
        q.append([root, float('-inf'), float('inf')])
        while q:
            node, min_bound, max_bound = q.popleft()
            if not(min_bound < node.val < max_bound):
                return False
            if node.left:
                # we we go to the left subtree
                # we need to make sure no values in the left tree
                # is bigger than the ancestor
                # we update the max bound
                q.append([node.left, min_bound, node.val])
            if node.right:
                q.append([node.right, node.val, max_bound])
        return True