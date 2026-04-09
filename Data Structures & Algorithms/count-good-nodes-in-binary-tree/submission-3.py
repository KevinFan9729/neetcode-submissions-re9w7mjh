# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # we do need to go through all Paths
        # in the path you consider the node is good
        # if the node is the highest in the path so far
        # so say in the path 1->2->2->1->5 we should have 
        # 4 good nodes
        # we should use dfs here since we need to go through 'paths'
        # dfs(root, pathMax) where pathMax tells you the running max in the path
        # time O(n)
        # Space O(n)
        def dfs(root, pathMax):
            if not root:
                return 0
            if root.val >= pathMax:
                pathMax = max(pathMax, root.val)
                return 1 + dfs(root.left, pathMax) + dfs(root.right, pathMax)
            return dfs(root.left, pathMax) + dfs(root.right, pathMax) 
        ans = dfs(root, float('-inf'))
        return ans
            
        