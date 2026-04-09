# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs to traverse the tree level by level
        res = []
        if not root:
            return []

        def bfs(root):
            q = deque()
            q.append(root)

            while q:
                q_len = len(q)
                temp = []
                for _ in range(q_len):
                    node = q.popleft()
                    temp.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                res.append(temp)
        bfs(root)
        return res

            
        