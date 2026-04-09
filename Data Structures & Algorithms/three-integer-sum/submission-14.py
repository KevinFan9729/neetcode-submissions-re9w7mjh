class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums[i] + nums[j] + nums[k] == 0
        # nums[i] + nums[j] = -nums[k]
        # now we have 2sum where the target is -nums[k]
        # basically we can fix one number and pick two more
        # Time O(n^2)
        # Space O(n)
        nums.sort()
        def twoSum(nums, target):
            # return two number than add up to target
            diff_map = {}
            res = set()
            for i in range(len(nums)):
                diff = target - nums[i]
                if nums[i] in diff_map:
                    tmp = [diff, nums[i], -target]
                    res.add(tuple(tmp))
                diff_map[diff] = i
            return res
        res = []
        seen = set()
        for i in range(len(nums)):
            fixed = nums[i]
            if fixed in seen:
                continue
            twoSum_res = twoSum(nums[i+1:], -fixed)
            if len(twoSum_res)>0:
                for item in twoSum_res:
                    res.append(list(item))
            seen.add(fixed)
        return res
