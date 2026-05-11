class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use a hashmap to construct an occurance map
        # Time O(k*log*m) m being number of unique element in nums
        # Space O(n)
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        heap = []
        for key, val in count.items():
            heap.append((val, key))
        
        heapq.heapify_max(heap)

        res = []
        while k:
            res.append(heapq.heappop_max(heap)[1])
            k-=1
        return res

        