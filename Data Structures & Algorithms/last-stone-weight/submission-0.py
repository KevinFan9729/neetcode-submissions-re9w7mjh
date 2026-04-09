class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # use a max heap
        # python by defualt only have min heap
        # we will make all values negative to get a max heap
        stone_neg = []
        for stone in stones:
            stone_neg.append(-1*stone)
        heapq.heapify(stone_neg) # Transform list x into a heap, in-place, in linear time
        while len(stone_neg) >=2:
            heavy1 = -1*heapq.heappop(stone_neg) #O(log n)
            heavy2 = -1*heapq.heappop(stone_neg)
            res = abs(heavy1 - heavy2)
            if res !=0 :
                 heapq.heappush(stone_neg, -1*res) #O(log n)
        if not stone_neg:
            return 0
        return -1 * stone_neg[0]