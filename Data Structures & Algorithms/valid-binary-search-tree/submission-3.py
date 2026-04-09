# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # dfs to check if the tree is valid
        # dfs(curr_node, lower_bound, upper_bound) is the signature
        # what if curr_node is None? return True

        def dfs(curr_node, lower_bound, upper_bound):
            if not curr_node:
                return True
            if upper_bound is not None and curr_node.val >= upper_bound:
                    return False
            if lower_bound is not None and curr_node.val <= lower_bound:
                    return False
            leftCheck = dfs(curr_node.left, lower_bound, curr_node.val)
            rightCheck = dfs(curr_node.right, curr_node.val, upper_bound)
            return leftCheck and rightCheck
        ans = dfs(root, None, None)
        return ans