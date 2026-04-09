# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # inorder treversal dfs and get an array of node value
        # in a valid bst, the array is sorted in increasing order
        array = []
        def dfs(node):
            if not node:
                 return
            dfs(node.left)
            array.append(node.val)
            dfs(node.right)
        
        dfs(root)
        left = 0
        right = 1
        while left < right and right < len(array):
             if array[right] <= array[left]:
                  return False
             left +=1
             right +=1
        return True