class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # use a heap?
        # Time O(klogn)
        # Space O(n)
        maxHeap = []
        for num in nums:
            maxHeap.append(num)
        heapq.heapify_max(maxHeap)
        maxVal = nums[0]
        while k:
            maxVal = heapq.heappop_max(maxHeap)
            k-=1
        return maxVal