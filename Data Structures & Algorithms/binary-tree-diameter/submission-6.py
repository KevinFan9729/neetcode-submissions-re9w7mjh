# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter is equal to max path length
        # would be easy if the path must all include route
        # for any node, the longest path is that PASSES through it is the sum
        # of hight of left and right tree
        # use dfs
        # the key is that the question 
        # Total nodes on full path: leftHeight + 1 + rightHeight (the 1 is root)
        # Edges on a path = nodes − 1
        # (leftHeight + 1 + rightHeight) − 1 = leftHeight + rightHeight
        # Time O(n)
        # Space O(h)
       
        maxLen = 0
        def height(root):
            nonlocal maxLen
            if not root:
                return 0

            leftHeight = height(root.left)
            rightHeight = height(root.right)

            maxLen = max(maxLen, leftHeight+rightHeight)

            # return the height of the tree
            # the height of the tree is the max path 
            return 1+max(leftHeight, rightHeight)

        height(root)
        return maxLen


