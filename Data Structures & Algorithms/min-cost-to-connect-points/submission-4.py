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
                src = points[i]
                dest = points[j]
                dist = abs(src[0]- dest[0]) + abs(src[1]- dest[1])
                if i not in adj:
                    adj[i] = []
                if j not in adj:
                    adj[j] = []
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        print(adj)
        visited = set()
        minHeap = []
        # lets start from the first point arbitrary choice
        for dist, nei in adj[0]:
            heapq.heappush(minHeap, [dist, 0, nei])
            visited.add(0)
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