class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # use a maxheap
        # Time O(klogn)
        # Space O(1)
        heap = nums # <- refer to same list, so mutating nums directly
        heapq.heapify_max(heap)
        ans = nums[0]
        while k:
            ans = heapq.heappop_max(heap)
            k-=1
        return ans