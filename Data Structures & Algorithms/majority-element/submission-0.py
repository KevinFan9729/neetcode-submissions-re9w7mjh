class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # easiest way is just use a counter
        # but that will be O(n) in space
        # how to do this in O(1) space?
        # majority means the number appear more than n/2 times
        # loop through the element
        # canadaite to track the current leader
        # count to track the vote
        # if we encounter the same number vote ++1
        # if we encounter a different number vote --1
        # if vote becomes 0, candaite is updated
        # candaite will be majority as other numbers are less than half
        # so other numbers will be cancelled out by the majority
        # Boyer-Moore Voting Algorithm
        # this algo can be used to find majoirty when you cannot
        # fit all data in memory (particularly in network communication)
        # O(n)
        # O(1)
        canadiate, vote = nums[0], 1
        for i in range(1, len(nums)):
            if vote == 0:
                canadiate = nums[i]
                vote = 1
                continue
            if canadiate == nums[i]:
                vote +=1
            else:
                vote -=1
        return canadiate
            