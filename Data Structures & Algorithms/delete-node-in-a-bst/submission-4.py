# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # deleting a node means finding the targte node
        # then remove the node
        # after finding the target node
        # if the node of interest is a leaf node
        # just remove
        # if node of interest has 1 child; prompte the child to replace that node
        # if the node of interest has 2 children
        # we need to replace this node with the smallest node the the right subtree
        # and remove the smallest node in the rght subtree
        # Time O(n)
        # Space O(h)
        def findSmallest(root):
            if not root:
                return
            if root.left:
                return findSmallest(root.left)
            else:
                # if we cannot find the left anymore
                # root is the smallest
                return root

        def deleteNode(root, key):
            if not root:
                return

            if key > root.val:
                root.right = deleteNode(root.right, key)
                return root
            elif key < root.val:
                root.left = deleteNode(root.left, key)
                return root
            else:
                # we have found the node to be deleted!
                if root.left == None and root.right == None:
                    # root to be deleted is a leaf node
                    root = None
                    return root
                elif root.left and not root.right:
                    return root.left
                elif root.right and not root.left:
                    return root.right
                else:
                    # node of interest has 2 children!
                    # find the smallest node in the right subtree:
                    smallest = findSmallest(root.right)
                    root.val = smallest.val
                    root.right = deleteNode(root.right, smallest.val)
                    return root
        
        node = deleteNode(root, key)
        return node
