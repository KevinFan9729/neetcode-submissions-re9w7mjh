import heapq
import copy
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Time O(n)
        # Space O(n)
        self.k = k
        self.curr_heap = list(nums)
        heapq.heapify_max(self.curr_heap) #O (n) in time 
        self.k_lookup = None # this will be a deep copy of curr_heap for getting k largest by poping k times
        # self.k_lookup = copy.copy(self.curr_heap)
        # we can do it without the copy
        # but this means we need to pop then repush all elements

    def add(self, val: int) -> int:
        # Time O(klogn)
        # Space O(n)
        heapq.heappush_max(self.curr_heap, val) # O(logn) in time
        k = self.k
        res = -1
        self.k_lookup = copy.copy(self.curr_heap) # O(n) in time, O(n) in space
        while k: # O(klogn) in time
            res = heapq.heappop_max(self.k_lookup)
            k-=1
        return res
            
        
