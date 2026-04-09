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
        # then we can solve two sum with O(n) time and O(1) space 
        
        # Time O(n^2)
        # Space O(1)

        nums.sort() # inplace sort
        def twoSum(nums: List[int], skipped_idx: int, target:int):
            # O(n)
            res = []
            left, right = 0, len(nums) -1
            while left < right:
                if left == skipped_idx:
                    left += 1
                    continue
                if right == skipped_idx:
                    right -= 1
                    continue
                curr_sum = nums[left] + nums[right]
                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    res.append([nums[left], nums[right], nums[skipped_idx]])
                    left += 1
                    right -= 1
            return res

        res = set() #<- part of the output, does not count in complexity
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue  # same value as previous i, skip
            target = -nums[i]
            temp = twoSum(nums, i, target)
            prev_target = target
            if not temp:
                continue
            for item in temp:
                res.add(tuple(sorted(item))) # sort is O(nlogn) but we always only have 3 elements so O(1) in time
        return [list(item) for item in res ]