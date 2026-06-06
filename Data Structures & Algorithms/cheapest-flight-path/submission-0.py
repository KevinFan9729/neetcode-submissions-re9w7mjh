class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # src to dest, weight
        # I am thinking maybe we can find all paths which we can each dest withink k stop
        # if they are paths; then we will return to the min cost path
        # this is going to be a bit expensive though bec we like backtracking usually means
        # that our solution would be exponetial in time
        # we can kinda like use a dijkstra like algo to find the cheapest value and path
        # but we have a constrint where we can have at most k stop from src to reach dest
        # so regular dijkstra does not work
        # but if we modify dijkstra where the heap takes in (cost, city, stop)
        # and we discard path where say stop > k (i.e. to pushing them back to the heap) then it should work!
        # Time O(VlogV)
        # Space O(V+E) # at most heap will hold and adj
        adj = {}
        for sr, dest, cost in flights:
            if sr not in adj:
                adj[sr] = []
            adj[sr].append((dest, cost))
        # our graph now is constructed

        heap = [(0, src, 0)] # cost, city, stop
        shortest = {}

        while heap:
            currCost, currCity, currStop = heapq.heappop(heap)
            if (currCity, currStop) in shortest:
                continue
            shortest[(currCity, currStop)] = currCost

            # go through the nei of the currCity
            for nei in adj.get(currCity, []):
                nextCity, nextCost = nei[0], nei[1]
                if nextCity != dst:
                    nextStopCount = currStop + 1
                else:
                    nextStopCount = currStop
                if nextStopCount >k:
                    # discard this path; no longer valid!
                    nextStopCount = currStop
                    continue 
                nextCost += currCost
                heapq.heappush(heap, (nextCost, nextCity, nextStopCount))
        cheapest = float('inf')
        for key, val in shortest.items():
            city, stop = key
            if city == dst and stop<=k:
                cheapest = min(cheapest, val)

        return -1 if cheapest == float('inf') else cheapest
