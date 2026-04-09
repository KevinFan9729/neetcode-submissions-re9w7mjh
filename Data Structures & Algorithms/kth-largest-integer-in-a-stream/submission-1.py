import heapq
import copy
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Time O(n)
        # Space O(n)
        self.k = k
        self.curr_heap = list(nums)
        heapq.heapify_max(self.curr_heap) #O (n) in time 
        # we need to pop then repush all elements

    def add(self, val: int) -> int:
        # Time O(klogn)
        # Space O(k)
        heapq.heappush_max(self.curr_heap, val) # O(logn) in time
        k = self.k
        res = -1
        restore = []
        while k: # O(klogn) in time
            res = heapq.heappop_max(self.curr_heap)
            restore.append(res)
            k-=1
        for item in restore:
            heapq.heappush_max(self.curr_heap, item)
        return res
            
        
