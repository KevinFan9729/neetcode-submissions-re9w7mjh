class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # we need to construct the map incrmenetally
        # after adding an edage run a dfs to check if adding this edge form a cycle
        # if adding this edge form an cycle, then that is the redundant edge
            # things to note
                # 1. bec the graph is undirected, we need to track the parent node for detecting loop
                # i.e. if we find a nei is in the visited set AND the it is not equal to the parent node, then there is a cycle
                # 2. bec we go through edges from left to right, the first edge that form the duplicate will apper last in the input
        # Per DFS: O(V + E)
        # Repeated E times: O(E * (V + E))
        # Time O(E * (V + E))
        # Space O(V+E)
        adj = {}
        def dfs(node, parent, adj):
            visited.add(node)
            for nei in adj[node]:
                if nei in visited and nei!= parent:
                    return True
                elif nei in visited:
                    continue
                cycle = dfs(nei, node, adj)
                if cycle:
                    return True
            return False

        for src, dest in edges:
            if src not in adj:
                adj[src] = []
            if dest not in adj:
                adj[dest] = []
            adj[src].append(dest)
            adj[dest].append(src)
            visited = set()
            cycle = dfs(src,-1,adj)
            if cycle:
                return [src, dest]
        return [-1,-1]