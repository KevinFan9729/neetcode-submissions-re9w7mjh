# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # standard tree bfs
        # O(n)
        # O(w) width of the tree or the widest level
        res = []
        q = deque()
        q.append(root)
        if not root:
            return res
        while q:
            qLen = len(q) # here is one level
            curr = []
            for i in range(qLen):
                node = q.popleft()
                curr.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(curr)
        return res
        