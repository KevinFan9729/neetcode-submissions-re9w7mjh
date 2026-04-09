from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # maybe bfs but right to left?
        # res have the right node at one level if available
        # actually res just needs to get the first element in the level in this setup
        # Time O(n)
        # Space O(n)
        q = deque()
        res = []

        if not root:
            return res
        q.append(root)
        while q:
            q_len = len(q)
            for i in range(q_len):
                node = q.popleft()
                if i == 0:
                    res.append(node.val)
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        return res