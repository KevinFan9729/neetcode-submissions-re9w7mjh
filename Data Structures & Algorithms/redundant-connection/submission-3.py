from typing import List
import copy
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # find n
        n = -1
        for pair in edges:
            n = max(n, pair[0], pair[1])
        # edges are possible options to remove, and we loop backword
        adj = {}

        for i in range(1, n+1):
            adj[i] = set()
        
        for pair in edges:
            adj[pair[0]].add(pair[1])
            adj[pair[1]].add(pair[0])

        def dfs(curr, prev):
            if curr in visited:
                return False
            visited.add(curr)
            for nei in adj[curr]:
                if nei == prev:
                    continue
                if dfs(nei, curr) == False:
                    return False
            return True 
        
        for target_index in range(len(edges) - 1, -1, -1):
            target = edges[target_index]
            adj[target[0]].remove(target[1])
            adj[target[1]].remove(target[0])
            visited = set()
            for i in range(1, n+1): # find starting point
                if adj[i] != set():
                    break
            if dfs(i, i-1) == True:
                break
            adj[target[0]].add(target[1]) # reset
            adj[target[1]].add(target[0])
        return target