from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # breadth first
        res = []
        queue = deque()

        if root:
            queue.append(root)
        level = 0
        while len(queue) > 0:
            # print(level)
            level_ls = []
            # note this for loop run a pre-determined number of times, based on the CURRENT size of the queue, 
            # if we want a loop that dynamically adjust to changes in the iterable's size, use while loop instead
            for i in range(len(queue)): 
                node = queue.popleft()
                level_ls.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # level+=1
            res.append(level_ls)
        return res