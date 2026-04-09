class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # we wants the minimum tim eit takes for ALL of the nodes to receive the signal
        # so we need to find out the min time for a sigal starting from k to all nodes
        # then we will find the max time in that collection to find the minium time to send a signal from node k to all nodes
        # we will use a hashmap to sore our result and act as the visited reference
        # before we return, we must check if the len(hasmap) == n, if that is not true, 
        # this means the graph is not fully connected! and we must return -1 
        # use Dijkstra's Algorithm
        # O(ElogV) in time
        # O(V+E) in space

        adj = {}
        for i in range(1,n+1):
            adj[i] = []
        
        for src, target, weight in times:
            adj[src].append([weight, target])
        
        shortest = {}
        minHeap = [[0,k]]
        while minHeap:
            weight, node = heapq.heappop(minHeap)
            # if the node is already in shortest, this means we already found a shortest path for the node we are on
            if node in shortest: 
                continue
            shortest[node] = weight
            for nei_weight, nei_node in adj[node]:
                if nei_node not in shortest:
                    heapq.heappush(minHeap, [weight+nei_weight, nei_node])
        if len(shortest) == n:
            return max(list(shortest.values()))
        return -1 

            