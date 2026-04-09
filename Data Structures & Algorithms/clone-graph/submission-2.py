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

        def dfs(node, visited):
            if node in visited:
                return
            if not node:
                return
            oldToNew[node] = Node(node.val)
            visited.add(node)
            for neighbor_node in node.neighbors:
                dfs(neighbor_node, visited)
        dfs(node, set())
        # make connections based on the mapping
        for old_node in oldToNew.keys():
            new_node = oldToNew[old_node]
            for old_neighbor_node in old_node.neighbors:
                new_node.neighbors.append(oldToNew[old_neighbor_node])

        return oldToNew[node]



