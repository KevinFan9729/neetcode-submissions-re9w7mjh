"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # we will have a hashmap that have key of old nodes and value of new nodes
    # we will first create all nodes
    # then we will take care of connections
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        visited = set()

        if not node:
            return None

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            new_node = Node(node.val)
            if node not in oldToNew:
                oldToNew[node] = new_node # make a new node and make an old to new mirror 
            for nei in node.neighbors:
                dfs(nei)
        dfs(node)

         # take care of connections
        for old in oldToNew.keys():
            for oldNei in old.neighbors:
                oldToNew[old].neighbors.append(oldToNew[oldNei])
        
        return oldToNew[node]

