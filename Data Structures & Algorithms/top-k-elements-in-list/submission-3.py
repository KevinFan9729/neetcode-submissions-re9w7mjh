import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we can se bucket sort
        # for bucket sort, we have a array which the index will of the array will be occurrence
        # and the array value will be the num or a list or nums (many nums can have the same occurance)
        # we can do this becuase the nums input array has a fixed size
        # to get the top k, we just need to loop through the bucket sort array in reverse order k steps!
        # time is O(n)
        # space is O(n)
        bucket = [[] for _ in range(len(nums)+1)]

        count_map = defaultdict(int)
        # count occurrence of num
        for i in nums:
            count_map[i] += 1
        
        for num, occurrence in count_map.items():
            bucket[occurrence].append(num)
        
        res = []

        for i in range(len(bucket)-1, 0, -1):
            if bucket[i] != []: # we have some values in this bucket
                for j in range(len(bucket[i])):
                    if len(res) != k:
                        res.append(bucket[i][j])
                    else:
                        break
                if len(res) == k:
                    break
        return res
        