# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # bfs move in the tree level by level
        # update the result list when you are at the last node of that level!
        res = []
        if not root:
            return []
        def bfs(root):
            q = deque()
            q.append(root)
            while q:
                q_len = len(q)
                for i in range(q_len):
                    node = q.popleft()
                    if i == q_len -1:
                        res.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
        bfs(root)
        return res
        