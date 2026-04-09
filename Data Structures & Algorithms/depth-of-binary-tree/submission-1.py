from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        level = 0
        if root:
            queue.append(root)
        else:
            return level
        while queue:
            # important to have this loop so 
            # we processes all nodes at the current level before moving to the next level
            # but if keeping track of level is not important, we don't need this inner for loop
            for i in range(len(queue)):
                node = queue.popleft()
                # print(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1 # done with all nodes in a level, increment level counter by 1 
        return level
        