class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # Dijkstra's to find the shortest path weight
        # Dijkstra is like store the inital weight/effort of the source in a minheap
        # if the shortest path weight is not set, set it in a hashmap
        # travel all of the neighbors
        # push neibors weight to the heap
        # continue until the heap is empty or when we have found the target pos's weight
        # Time: O(m * n * log(m * n))
        # Space: O(m * n)
        ROW, COL = len(heights), len(heights[0])
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        shortest = {}
        # starting from the 0,0 weight is 0
        # use a minheap
        minheap = [(0, (0,0))] # effort, pos

        while minheap:
            effort, pos = heapq.heappop(minheap)
            if pos in shortest:
                continue
            shortest[pos] = effort
            if pos[0] == ROW-1 and pos[1] == COL-1:
                return shortest[pos]
            # loop through pos's neighbor now
            for dx, dy in dirs:
                newR = pos[0] + dx
                newC = pos[1] + dy
                if newR < 0 or newR >=ROW or newC < 0 or newC >=COL:
                    # OUT OF BOUND
                    continue
                if (newR, newC) in shortest:
                    # visisted
                    continue
                newEffort = max(
                    effort,
                    abs(heights[pos[0]][pos[1]] - heights[newR][newC])
                )
                heapq.heappush(minheap, (newEffort, (newR, newC)))
