class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # to do O(1) space, we need to do voting
        # two pointer 
        # one is the majority pointer, candidate 
        # one is the voting pointer, counter
        # more than n/2 is majority
        # if we get the same candidate, counter+=1
        # if we get a different candidate counter-=1
        # if counter == 0, update the candidate to the new candidate
        # as majority occur more than n/2 times, it should survive all the cancellation
        # Time O(n)
        # Space O(1)
        candidate = nums[0]
        counter = 0
        for i in range(len(nums)):
            if counter == 0:
                candidate = nums[i]
                counter = 1
            else:
                if candidate == nums[i]:
                    counter+=1
                else:
                    counter-=1
        return candidate
