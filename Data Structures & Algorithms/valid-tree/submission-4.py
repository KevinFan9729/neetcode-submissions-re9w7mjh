class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # this question is asking us if the undirected graph is 
        # fully connected and has no cycle
        # construct the graph
        adj = {}
        for i in range(n):
            adj[i] = []
        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)
        visited = set()
        def dfs(node, parent):
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    if dfs(nei, node):
                        return True
                elif nei != parent:
                    return True
            return False
        cycle = dfs(0, -1)
        if cycle:
            return False
        return len(visited) == n