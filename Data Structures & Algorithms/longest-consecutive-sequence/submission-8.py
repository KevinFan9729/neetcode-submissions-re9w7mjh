class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # order does not matter 
        # check if the number is a start of a consective sequence
        # how do you check if a number is a start of the consective sequence?
        # you do so by checking if num -1 exist
            # if it exist then num is not a start
            # if it does not exist, then yes; it is a start
        # use a hash set for existence checking
        # once we found a start, we can grow the sequence and check length
        # Time O(n)
        # Space O(n)
        check = set(nums)
        maxLen = 0
        for num in check:
            seqLen = 1
            if num -1 not in check:
                # num is a start
                start = num
                while start+1 in check:
                    seqLen +=1
                    start +=1
            maxLen = max(maxLen,seqLen)

        return maxLen