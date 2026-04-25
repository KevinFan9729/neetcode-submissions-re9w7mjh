# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Time O(n)
        # Space O(n)

        def deleteN(root, target):
            if not root:
                return
            if target > root.val:
                root.right = deleteN(root.right, target)
                return root
            elif target < root.val:
                root.left = deleteN(root.left, target)
                return root
            else:
                # found the target
                if not(root.left or root.right):
                    return None
                elif root.left and not root.right:
                    return root.left
                elif not root.left and root.right:
                    return root.right
                else:# the target node has 2 children
                    smallestFromRight = findSmallest(root.right)
                    root.right = deleteN(root.right, smallestFromRight.val)
                    root.val = smallestFromRight.val
                    return root 

        
        def findSmallest(root):
            if not root:
                return
            while root.left:
                root = root.left
            return root

        return deleteN(root, key)