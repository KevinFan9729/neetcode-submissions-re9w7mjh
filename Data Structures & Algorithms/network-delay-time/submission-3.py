class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # dijkstra algorithm
        # Building adjacency list: O(E)
        # Dijkstra: each edge can cause a heap push, so O(E log E)
        # Time O(ElogV)
        # Space O(v+e)
        adj = {}
        for src, dest, time in times:
            if src not in adj:
                adj[src] = []
            adj[src].append((time, dest))

        heap = [(0,k)] # this is our statring source
        shortest = {}
        while heap:
            currTime, currNode = heapq.heappop(heap)
            if currNode in shortest:
                continue
            shortest[currNode] = currTime
            if len(shortest) == n:
                return currTime # we reached the last node
            # loop through the nei of currNode
            for nei in adj.get(currNode, []):
                timeNeeded, nextNode = nei
                heapq.heappush(heap,(timeNeeded+currTime, nextNode))
        
        return -1