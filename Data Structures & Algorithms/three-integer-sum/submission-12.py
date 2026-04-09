class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums[i] + nums[j] + nums[k] == 0
        # nums[i] + nums[j] == 0-nums[k] where -nums[k] is the target
        # now we can do a two sums where -nums[k] is the target
        # two sum can be solved with O(n)
        # now the not having the duplicate part
        # so -1,0,1 and 0,1,-1 are considered as duplicates
        # we can sort
        # can we have a set to check or remove duplciates?
        # we can sort the array first
        # do 2Sum only on the elements to the right of i
        # then we can solve two sum with O(n) time and O(1) space 
        
        # Time O(n^2)
        # Space O(1)

        nums.sort() # inplace sort

        res = [] #<- part of the output, does not count in complexity
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue  # same value as previous i, skip
            left, right = i + 1, len(nums) -1
            target = -nums[i]
            while left < right:
                curr_sum = nums[left] + nums[right]
                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    res.append([nums[left], nums[right], nums[i]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]: # skip duplicate as we are sorted
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
            
        return res