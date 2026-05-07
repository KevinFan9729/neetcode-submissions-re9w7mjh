class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # graph question
        # we have one judge
        # the graph is directional
        # if we have one node that has no outgoing edge (trust no one)
        # and all other nodes go to that node
        # then that node is the judge node
        # the judge is the terminal node
        # Time:  O(V + E) we will navigate the entire graph
        # Space: O(V + E)
        adj = {}
        for i in range(n):
            adj[i+1] = []
        for src, dest in trust:
            adj[src].append(dest)

        visited = set()
        def findTerminal(node, adj):
            if not node:
                return -1
            if adj[node] == []:
                return node
            visited.add(node)
            for nei in adj[node]:
                if nei in visited:
                    continue # don't visit the same node again
                terminal = findTerminal(nei, adj)
                if terminal != -1:
                    return terminal
            return -1    
        
        potential = findTerminal(1, adj)
        print(potential)
        if potential == -1:
            return -1
        
        trustCount = 0
        for i in range(1, n+1):
            if i != potential:
                for nei in adj[i]:
                    if nei == potential:
                        trustCount+=1
        if trustCount == n-1:
            # the potential have all trusts
            return potential
        return -1




            