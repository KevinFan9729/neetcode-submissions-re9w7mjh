from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs
        # Time O(n)  need to loop through all nodes
        # Space O(n) due to the queue (storing the widest level w, which is n/2 -> n)
        q = deque()
        q.append(root)
        res = []
        if not root:
            return res
        while q:
            q_len = len(q)
            level_res = []
            # we need a for loop here to actually go through a level
            for _ in range(q_len):
                node = q.popleft()
                level_res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level_res) # we are done with a level
        return res