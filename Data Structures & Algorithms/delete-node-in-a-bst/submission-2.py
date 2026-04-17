# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # finding the node is easy # as this is a bst
        # we need a function to return the new root of the possibly modifed tree (new head)
        # if say we find the root that needs to be deleted
        # we have a couple cases
            # 1 the node we want to delete have no children (leaf)
                # we just return None
            # 2 the node we want to delete has one child
                # we return that child
            # 3 the node we want to delete has 2 children
                # find the smallest node from the right subtree
                # that tree is the new replacement
                # delete that node from the right subtree
                # the smallest node from the right subtree is just the leftmost node in that subtree bec of bst structure
        
        def searchDel(root, target): # this func return the new (possibly modded tree's head)
            if not root:
                return None
            
            if root.val > target:
                root.left = searchDel(root.left, target)
                return  root
            elif root.val < target:
                root.right = searchDel(root.right, target)
                return root
            else: # we found the target node
                if not (root.left or root.right): # target is leaf
                    return None
                elif root.left and not root.right:
                    return root.left
                elif not root.left and root.right:
                    return root.right
                else: # two children
                    minNodeRight = findMinNode(root.right)
                    root.right = searchDel(root.right, minNodeRight.val)
                    minNodeRight.right = root.right
                    minNodeRight.left = root.left
                    return minNodeRight

        def findMinNode(root):
            minNode = root
            while root:
                if root.left:
                    root = root.left
                    minNode = root
                else:
                    return minNode
            return minNode

        return searchDel(root,key)
            