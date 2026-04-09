"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # O(V+E)
        if not node:
            return None
        oldToNew ={} #map old node to new node
        queue = deque()
        visted = set()
        queue.append(node)
        visted.add(node)
        # bfs to navigate all nodes and create a old to new node mapping
        # note here we create all the new nodes based on the old node
        # but we do not make connections yet
        while queue:
            curr_node = queue.popleft()
            new_node = Node(curr_node.val)
            oldToNew[curr_node] = new_node
            for neighbor_node in curr_node.neighbors:
                if neighbor_node not in visted:
                    queue.append(neighbor_node)
                    visted.add(neighbor_node)
        
        # make connections based on the mapping
        for old_node in oldToNew.keys():
            new_node = oldToNew[old_node]
            for old_neighbor_node in old_node.neighbors:
                new_node.neighbors.append(oldToNew[old_neighbor_node])
        
        return oldToNew[node]



