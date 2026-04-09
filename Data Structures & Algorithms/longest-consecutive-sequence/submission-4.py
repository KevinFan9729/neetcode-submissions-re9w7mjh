class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # note that the start of a sequence has no left value
        # we can find the start of the sequence and the grow the sequence if possible
        # O(n) in time, even though we have a nested loop, we just go through each sequence once
        # O(n) in space due to the hashset
        hashSet = set(nums)
        longest = 0
        total = 0
        for num in nums:
            if num -1 not in hashSet:# not left neighbor, we found a start of a sequence
                start = num
                length = 1 # sequence with the start element has an initial length of 1
                while start+1 in hashSet:
                    length+=1
                    start +=1
                longest = max(longest, length)
                total+=length
            if total == len(nums): # break out early if we run through all numbers in nums
                break
        return longest
