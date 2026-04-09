from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # kmO(n), k is constant, mO(n)
        # we can have a hash map that stores occurrence as such
        # key: number value: occurrence
        # we have a helper function which help us to find the most frequent key
        # once we the most frequent key is found, we store that value and mark its occurrence as -1
        # we will repeat this helper function k times
        
        # say the length of the nums list is n
        # the number of unique elements in the list is m
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        result = []
        while k > 0:
            key = self.find_max_key(count)
            result.append(key)
            k -= 1
            # mark the occurrence as -1, effectively not considering the key 
            count[key] = -1
        return result 
    
    def find_max_key(self, count_dict):
        max_occurrence = 0
        target_key = None
        for key, value in count_dict.items():
            if value > max_occurrence:
                max_occurrence = value
                target_key = key
        return target_key
