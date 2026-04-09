from typing import List
import copy
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # find n
        n = -1
        for pair in edges:
            n = max(n, pair[0], pair[1])

        # edges are possible options to remove, and we loop backword

        adj_org = {}
        # adj_test = {}

        for i in range(1, n+1):
            adj_org[i] = []
            # adj_test[i] = []
        
        for pair in edges:
            adj_org[pair[0]].append(pair[1])
            adj_org[pair[1]].append(pair[0])

            # adj_test[pair[0]].append(pair[1])
            # adj_test[pair[1]].append(pair[0])

        print(adj_org)

        def dfs(curr, prev):
            if curr in visited:
                return False
            visited.add(curr)
            for nei in adj_test[curr]:
                if nei == prev:
                    continue
                if dfs(nei, curr) == False:
                    return False
            return True 
        
        for target_index in range(len(edges) - 1, -1, -1):
            adj_test = copy.deepcopy(adj_org) # reset adj_test
            target = edges[target_index]
            adj_test[target[0]].remove(target[1])
            adj_test[target[1]].remove(target[0])
            visited = set()
            for i in range(1, n+1): # find starting point
                if adj_test[i] != []:
                    break
            if dfs(i, i-1) == True:
                break
        return target