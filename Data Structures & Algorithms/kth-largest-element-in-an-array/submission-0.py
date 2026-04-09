class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # use a max heap to solve this problem
        nums_neg = []
        for num in nums:
            heapq.heappush(nums_neg, -1*num)
        
        while k:
            max_val = heapq.heappop(nums_neg)
            k -= 1
        return -1* max_val
        