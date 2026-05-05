"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # we need to navigate through all nodes and create the new nodes?
        # we should use a hashmap to construct a mapping of oldToNew
        # we need to make all vertices first then worry about the edges later
        # bec if we do everything in one go, say you are making node 1 which is connected to 2 and 10
        # if you make node 1, the new node 2 and 10 do not exist
        # use bfs to treverse the adj list
        # Time O(V+E)
        # space O(V+E)
        oldToNew = {}
        q = deque()
        if node == None:
            return None
        q.append(node)
        visited = set()
        visited.add(node)
        while q:
            curr = q.popleft()
            oldToNew[curr] = Node(curr.val)
            for neg in curr.neighbors:
                if neg not in visited:
                    visited.add(neg)
                    q.append(neg)
        q = deque()
        q.append(node)
        visited = set()
        visited.add(node)
        while q:
            curr = q.popleft()
            for neg in curr.neighbors:
                if neg not in visited:
                    visited.add(neg)
                    q.append(neg)
                # create edges for the cloned graph
                oldToNew[curr].neighbors.append(oldToNew[neg])
        return oldToNew.get(node, None)
  