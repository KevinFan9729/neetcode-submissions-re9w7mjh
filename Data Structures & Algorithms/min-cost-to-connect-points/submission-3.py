class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # we must generate a graph that is fully connected first
        # this graph is undirected
        # O(ElogV) in time
        # O(E) in space

        if len(points) == 1: # we only have one point
            return 0
        # first let's generate the fully connected graph!
        adj = {}
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                src = tuple(points[i])
                dest = tuple(points[j])
                dist = abs(src[0]- dest[0]) + abs(src[1]- dest[1])
                if src not in adj:
                    adj[src] = []
                if dest not in adj:
                    adj[dest] = []
                adj[src].append([dist, dest])
                adj[dest].append([dist, src])
        
        print(adj)
        visited = set()
        minHeap = []
        # lets start from the first point arbitrary choice
        src = tuple(points[0])
        for dist, nei in adj[src]:
            heapq.heappush(minHeap, [dist, src, nei])
            visited.add(src)
        minCost = 0
        while minHeap:
            dist, src, node = heapq.heappop(minHeap)
            if node in visited:
                continue # node is visted, we skip this node and continue the loop
            visited.add(node)
            minCost += dist
            for neiDist, nei in adj[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, [neiDist, node, nei])
        return minCost