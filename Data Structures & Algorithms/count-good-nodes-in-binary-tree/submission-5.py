# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # we need dfs as we need to go deep?
        # along a path, we track a running max,
        # if a node is bigger than or eqaul to the running max +=1 in ans, update the running max in the path
        # each path must have their running max, and they should not interfere with each other
        # root is always good
        # k, so root is only counted once as we call from root but then only go to the left and right of root and never revisit root again
        # Time O(n)
        # Space O(h)
        ans = 0
        def dfs(root, pathMax):
            nonlocal ans
            if not root:
                return
            if root.val >= pathMax:
                pathMax = root.val
                ans+=1
            dfs(root.left, pathMax)
            dfs(root.right, pathMax)
        dfs(root, root.val)
        return ans