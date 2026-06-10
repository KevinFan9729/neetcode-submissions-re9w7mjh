# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # it seems like we are counting number of nodes
        # we want to go deep so we use dfs
        # even tough I think we can also do bfs and count the level number
        # depth = 0

        q = deque()
        if root:
            q.append(root)
        else:
            return 0
        depth = 0
        while q:
            qLen = len(q)
            for _ in range(qLen):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth += 1
        return depth