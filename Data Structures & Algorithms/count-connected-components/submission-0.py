class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #dfs to count if we can travel to all nodes in a graph
        #build the undirected graph
        adj = {}
        for i in range(n):
            adj[i] = []
        for pair in edges:
            adj[pair[0]].append(pair[1])
            adj[pair[1]].append(pair[0])
        
        print(adj)
        visited = set()
        travel_all = False
        def dfs(curr, prev):
            nonlocal travel_all
            if curr in visited:
                return # avoid infinite loop back 
            visited.add(curr)
            for nei in adj[curr]:
                if prev == nei:
                    continue
                dfs(nei, curr)
            if len(visited) == n:
                travel_all = True
                return
        connection = 1
        dfs(0, -1)
        while travel_all == False:
            connection += 1
            max_connected_node = max(visited)
            dfs(max_connected_node+1, max_connected_node)
        
        return connection


            

