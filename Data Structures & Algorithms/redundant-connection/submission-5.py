class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # need to identify which edge created the cycle
        # we need to build the graph while checking if say adding this edge will create a cycle or not
        # if adding this edge create the cycle, then we know that that edge is the redundant edge
        # how do we detect a cycle in an undirected graph???
        # track the parent node you came from. If you see a visited neighbor that is not your parent, then you found a cycle.
        # we build the graph from left to right so we will natrually return the last redundant edge
        # adj
        # 1:[2,3]
        # 2:[1,4]
        # 3:[1,4]
        # 4:[3,2]
        # Time O(E * (V + E))
        # Space O(V+E)
        def hasCycle(node, parent, adj, visited):
            if node in visited:
                return True
            visited.add(node)
            ans = False
            for neighbor in adj[node]:
                # if neighbor is the parent, skip, do not want to revisit the parent
                if neighbor == parent:
                    continue
                ans = hasCycle(neighbor, node, adj, visited)
                if ans:
                    return ans
            return ans

        adj = {}
        for src, dest in edges:
            if src not in adj:
                adj[src] = []
            if dest not in adj:
                adj[dest] = []
            # add this edge
            adj[src].append(dest)
            adj[dest].append(src)
            cycle = hasCycle(src, -1, adj, set())
            if cycle: # adding this edge causes the cycle
                return [src, dest]
