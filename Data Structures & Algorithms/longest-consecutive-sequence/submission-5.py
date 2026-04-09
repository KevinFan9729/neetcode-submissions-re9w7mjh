class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # hashset? as lookup is O(1)?
        # maybe have a hashmap where key stores end, and value stores length, say countMap
        # countMap will be useful to save us repeated work
        # say if we find a non_zero value (length of the start), we will just use this value (no looping again to find the length)
        # we have nested loop here but; we do not do repeated work
        # Time O(n) we loop through nums and do not do repeated work
        # space O(n) we use extra memory
        count_map = {}
        for num in nums:
            count_map[num] = 1 # default is length of 1 (single number has a length of 1)
        lookup_set = set(nums)
        nums = list(lookup_set) # remove duplicates
        max_len = 0
        for num in nums:
            prev = num - 1
            if count_map.get(num + 1, 0) >1: # if the next is a non default value
                count_map[num] = count_map[num + 1] - 1 # current can be computed directly
                max_len = max(max_len, count_map[num])
                continue
            if count_map.get(prev, 0) > 1: # if the previous is a non default value
                count_map[num] += count_map[prev]  # current can be computed directly
                max_len = max(max_len, count_map[num])
                continue
            while prev in lookup_set:
                count_map[num] += 1
                prev -= 1
            max_len = max(max_len, count_map[num])
        print(count_map)
        return max_len