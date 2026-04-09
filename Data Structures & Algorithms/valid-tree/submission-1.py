
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # build the adjacency list
        adj = {}
        for i in range(n):
            adj[i] = []
        # undirected
        for pair in edges:
            adj[pair[0]].append(pair[1])
            adj[pair[1]].append(pair[0])
        print(adj)
        visited = set()
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
        if dfs(0, -1) and len(visited) == n: # len(visited) == n to check disconnected node
            return True 
        return False