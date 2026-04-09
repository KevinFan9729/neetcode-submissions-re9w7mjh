from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurance_map = defaultdict(int)
        for i in range(len(nums)):
            occurance_map[nums[i]] += 1
        pairs = []
        for key, value in occurance_map.items():
            # number, occurance
            pairs.append([key, value])
        #nlogn
        pairs_sorted = sorted(pairs, key=lambda x:x[1], reverse= True)
        res = []
        for i in pairs_sorted[0:k]:
            res.append(i[0])
        return res

        