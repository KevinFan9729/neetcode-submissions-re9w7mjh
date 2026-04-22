class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # ok when is num the start of the sequence???
            # it is a start of a sequence only when num-1 does not exist
        # once we found a start of sequnce, we can loop and check if the next exist and find the sequence length
        # this will be O(n) in time as we do not do any repeated work
        # Time O(n)
        # Space O(n)

        numSet = set(nums)
        maxLen = 0
        for num in numSet:
            if num -1 in numSet:
                # not a start num, skip
                continue 
            # at this point we know num is a start
            nextNum = num+1
            length = 1
            while nextNum in numSet:
                length +=1
                nextNum += 1
            maxLen = max(maxLen,length)
        return maxLen