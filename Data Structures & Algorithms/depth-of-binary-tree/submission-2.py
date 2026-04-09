from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # bfs appoarch (count the level)
        if not root:
            return 0
        def bfs(node):
            queue = deque()
            level = 0
            queue.append(node)
            while queue:
                queue_len = len(queue)
                for _ in range(queue_len):
                    curr = queue.popleft()
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                level +=1
            return level
        depth = bfs(root)
        return depth
                
        