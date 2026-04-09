class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # we can navigate starting at one node and we can try to navigate
        # the graph with dfs
        # if we finish treversing and the visited set length is equal to n
        # then we can return the connected component count 
        # length is not reaching n, this means we still have node left
        # O(V+E) in time, we will treverse the entire graph
        # O(V+E) in space for making the graph

        # first, construct the undirected graph
        adj = {}
        for i in range(n):
            adj[i] = []
        
        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)
        
        def dfs(node):
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)
        visited = set()
        count = 0
        for i in range(n):
            if len(visited) == n:
                return count
            if i not in visited:
                count += 1
                dfs(i)
        return count
