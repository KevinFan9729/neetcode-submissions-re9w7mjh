# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # delete should return the new root of this subtree
        # three cases
        # the target node has no children
        # return None
        # the target node has one child
        # retunr the child 
        # the target node has two children
        # find the smallest node in the right tree
        # or find the largest node in the left tree
        # Time O(n)
        # Space O(n)

        def searchDelete(root, target):
            # search and delete
            if not root:
                return
            if root.val == target:
                # return new subtree root/delete logic
                if not (root.left or root.right):
                    return None
                elif root.left and not root.right:
                    return root.left
                elif root.right and not root.left:
                    return root.right
                else:
                    # two chidren
                    # find the smallest node in the right tree
                    smallestRight = findSmallest(root.right)
                    root.val = smallestRight.val
                    root.right = searchDelete(root.right, smallestRight.val)
                    return root
            if target > root.val:
                root.right = searchDelete(root.right, target)
                return root
            elif target < root.val:
                root.left = searchDelete(root.left, target)
                return root

        def findSmallest(node):
            while node.left:
                node = node.left
            return node

        new = searchDelete(root, key)
        return new