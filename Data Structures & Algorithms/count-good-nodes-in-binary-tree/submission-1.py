# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # dfs to traverse all routes?
        # dfs check if the current node is a good node
        # a node is a good node if it has no previous value or its previous max value is smaller than itself
        # if a node is good, count +=1
        # if a node is not good, does not increase count
        # dfs should be dfs(curr_node, prev_max_val)?
        def dfs(curr_node, prev_max_val):
            if not curr_node:
                return 0
            if curr_node.val >= prev_max_val:
                count = 1
            else:
                count = 0
            new_max_val = max(prev_max_val, curr_node.val)
            count += dfs(curr_node.left, new_max_val)
            count += dfs(curr_node.right, new_max_val)
            return count
        
        ans = dfs(root, float('-inf'))
        return ans
            