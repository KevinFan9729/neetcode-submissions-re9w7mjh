# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # use dfs or bfs can all solve this question
        # say we want to use dfs
        # navigate through both trees at the same time 
        # if there is a difference bewteen the tree node, return False immediately
            # difference can occur if nodes values are different
            # if one node has value and other node is None
        
        def dfs(node1, node2):
            if node1 == node2 == None:
                return True
            if not node1 or not node2: # only one node is null
                return False
            if node1.val != node2.val:
                return False
            left_check = dfs(node1.left, node2.left)
            right_check = dfs(node1.right, node2.right)
            return left_check and right_check
        
        isSame = dfs(p, q)
        return isSame


        