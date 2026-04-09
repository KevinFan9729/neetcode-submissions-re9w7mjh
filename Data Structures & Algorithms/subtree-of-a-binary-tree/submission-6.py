# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # this problem is the sametree problem
        # but then you do that starting from all nodes?
        # this would be quite expensive though as it will be O(m*n) 
        # where m is the size of the subtree and n is the size of the tree
        # Time O(m*n)
        # Space O(h) of the highest tree
        if not subRoot:
            # an empty tree is a subtree of any tree
            return True

        def isSame(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 and root2:
                return False
            if not root2 and root1:
                return False
            if root1.val != root2.val:
                return False
            leftCheck = isSame(root1.left, root2.left)
            if not leftCheck:
                return False
            rightCheck = isSame(root1.right, root2.right)
            if not rightCheck:
                return False
            return leftCheck and rightCheck

        def dfs(root):
            # go through all nodes in tree
            if not root:
                return False
            if isSame(root, subRoot):
                return True
            return dfs(root.left) or dfs(root.right)

        ans = dfs(root)
        return ans
