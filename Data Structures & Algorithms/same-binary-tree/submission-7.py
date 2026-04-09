# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # the trees are the same if
            # their structure are the same
            # their tree node values are the same at the respective pos
        # Time O(n)
        # Space O(h)
        # dfs and bfs can all solve this problem
        q1 = deque()
        q2 = deque()
        q1.append(p)
        q2.append(q)

        while q1 and q2:
            node_count = len(q1)
            for _ in range(node_count):
                node1 = q1.popleft()
                node2 = q2.popleft()
                if not node1 and not node2:
                    continue # hanlde if node is null
                if not node1 and node2:
                    return False
                if node1 and not node2:
                    return False
                if node1.val != node2.val:
                    return False
                q1.append(node1.left)
                q2.append(node2.left)
                q1.append(node1.right)
                q2.append(node2.right)

        return not q1 and not q2