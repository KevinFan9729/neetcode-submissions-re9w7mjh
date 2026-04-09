# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxLength = 0
        def findLongestPathLen(root: Optional[TreeNode]):
            nonlocal maxLength
            if not root:
                return 0
            leftHeight = findLongestPathLen(root.left)
            rightHeight = findLongestPathLen(root.right)
            #       A
            #      / \
            #     B   C
            #    / \
            #   D   E

            # height of D, E, C are 0
            # hight of B is height of max(D and E) + 1 
            maxLength = max(leftHeight+rightHeight, maxLength)
            return max(leftHeight, rightHeight) + 1 # Compute the height of the current node based on the max of left and right subtree 
        findLongestPathLen(root)
        return maxLength


