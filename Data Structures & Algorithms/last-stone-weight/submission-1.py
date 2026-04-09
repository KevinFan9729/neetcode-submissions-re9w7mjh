class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # use a max heap to find the top two
        # then follow the simulation
        # Time O(nlogn)
        # Space O(n)
        heapq.heapify_max(stones) #O(n)
        while len(stones) >= 2:
            stone1 = heapq.heappop_max(stones) #O(logn)
            stone2 = heapq.heappop_max(stones)
            diff = abs(stone1 - stone2)
            if diff != 0:
                heapq.heappush_max(stones, diff)
        if len(stones) == 1:
            return stones[0]
        return 0

