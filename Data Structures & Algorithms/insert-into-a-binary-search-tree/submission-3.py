# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # ok it is a bst, this means we need to maintain the bst struecture after insertion
        # can we just treverse the tree until we arrive at the correct leaf node
        # the insertion point may be a missing child of a non-leaf node
        # Time O(n) # at worst we can treverse all nodes
        # Space O(h)
        def dfs(root):
            if not root:
                return TreeNode(val)
            if val > root.val:
                if root.right:
                    # if right exists
                    # go to the right tree
                    dfs(root.right)
                else:
                    root.right = TreeNode(val=val)

            else:
                if root.left:
                    dfs(root.left)
                else:
                    root.left = TreeNode(val=val)
        
        res = dfs(root)
        return res if res else root
            