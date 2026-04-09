import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we can use a hashmap to compute the frequency of each number in the array
        # the problem now is how do you get the top k most frequent element out based on the hashmap
        # maybe a heap can help?
        # max heap where the root always has the max value
        # heap push and pop max is O(logn) in time
        # making a heap from an array is O(n)
        # the element we are going to push to the heap is (occurrence, num)
        # Time O(klogn) as we need to pop max heap k times
        # Space O(n) as we need a hashmap and a heap

        count_map = defaultdict(int)
        # count occurrence of num
        for i in nums:
            count_map[i] += 1
        
        elements = []
        for num, occurrence in count_map.items():
            elements.append([occurrence, num])
        
        heapq.heapify_max(elements) # O(n) time to make a max heap

        res = []
        for i in range(k): # run k times
            top = heapq.heappop_max(elements) # O(logn)
            res.append(top[1])
        return res