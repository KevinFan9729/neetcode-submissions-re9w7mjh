# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    # Two trees s and t are said to be identical if their root values are same and their 
    # left and right subtrees are identical.
    # we will use dfs to check 
        def isSame(node1, node2):
            if node1 == node2 == None:
                return True
            if node1 and node2 is None:
                return False
            if node2 and node1 is None:
                return False
            if node1.val != node2.val:
                return False

            leftCheck = isSame(node1.left, node2.left)
            rightCheck = isSame(node1.right, node2.right)
            if (leftCheck and rightCheck):
                return True
            return False
        def isSub(root, subRoot): # traverse in the tree 
            if not root:
                return False
            if isSame(root, subRoot):
                return True
            return isSub(root.left, subRoot) or isSub(root.right, subRoot)

        found = isSub(root, subRoot)

        return found
