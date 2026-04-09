from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        res = []
        if root:
            queue.append(root)
        level = 0
        while len(queue) > 0:
            node_count = len(queue)
            for i in range(node_count):
                node = queue.popleft()
                if node_count == 1: # there is only one node at the level
                    res.append(node.val) # include the only node
                elif node_count > 1: # there are more than one node at the level
                    if i == 0:
                        res.append(node.val) # only include the right most node
                if node.right: # right to left
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        return res