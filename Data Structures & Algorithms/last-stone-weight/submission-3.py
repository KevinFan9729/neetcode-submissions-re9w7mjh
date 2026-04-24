class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # use max heap
        # Time O(nlogn)
        # Space O(n)
        maxHeap = []

        for stone in stones:
            maxHeap.append(stone)
        
        heapq.heapify_max(maxHeap)
        
        while len(maxHeap) > 1:
            if maxHeap:
                stone1 = heapq.heappop_max(maxHeap)
            if maxHeap:
                stone2 = heapq.heappop_max(maxHeap)
            diff = abs(stone1 - stone2)
            if diff >0:
                heapq.heappush_max(maxHeap, diff)
        
        if maxHeap:
            return maxHeap[0]
        return 0
            