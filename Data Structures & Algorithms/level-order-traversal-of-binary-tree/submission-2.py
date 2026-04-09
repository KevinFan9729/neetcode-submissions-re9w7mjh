# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # dfs to traverse the tree level by level
        res = []
        def dfs(root, level):
            if not root:
                return
            if len(res) == level:
                res.append([]) # we hit a new level, res neeed to grow to record all nodes!
            res[level].append(root.val)
            dfs(root.left, level+1)
            dfs(root.right, level+1)
        dfs(root,0)
        return res

            
        