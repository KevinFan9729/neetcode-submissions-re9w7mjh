class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # use a min heap we can solve this problem
        minHeap = []
        for x, y in points:
            dist_sq = (x**2 + y**2)
            heapq.heappush(minHeap, (dist_sq, [x,y])) # O(log(n))
        res = []
        while k:
            min_item = heapq.heappop(minHeap) # O(log(n))
            res.append(min_item[1])
            k-=1
        return res
        