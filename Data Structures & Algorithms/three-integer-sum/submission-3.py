class Solution:
    def twoSum(self, nums: List[int], target: int, first_num: int) -> List[List[int]]:
        count = defaultdict(int)
        ans = []

        for i, val in enumerate(nums):
            diff = target - val
            if diff in count:
                if [first_num, val, diff] not in ans:
                    ans.append([first_num, val, diff])
            count[val] = i
        return ans

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # fix one number, then we have 2sum
        res = []
        nums.sort() # Sort to group duplicate start together
        history = set() # avoid starting at a duplicate number 
        for i in range(len(nums)):
            if nums[i] not in history:
                ans = self.twoSum(nums[i+1:len(nums)],0-nums[i], nums[i])
                history.add(nums[i])
                if ans:
                    res+=ans
        return res
