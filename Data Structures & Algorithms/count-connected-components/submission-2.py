class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # we need to track a visited set
        # loop through 0 to n-1
        # if a node is not found in the visited set, then ans+=1
            # run dfs on that node till the end
        # Each vertex is fully processed once.
        # Each edge is examined at most twice in an undirected graph
        # Time: O(V + E)
        # Space: O(V + E)
        visited = set()
        adj = {}
        ans = 0
        # bec the node can be disconnected (so some nodes can be isolated, so no edges)
        # we need to make sure adj contains all nodes
        for i in range(n):
            adj[i] = []

        for src, dest in edges:
            # undirected graph
            adj[src].append(dest)
            adj[dest].append(src)

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neg in adj[node]:
                dfs(neg)
            
        for i in range(n):
            if i not in visited:
                ans+=1
                dfs(i)
        return ans
