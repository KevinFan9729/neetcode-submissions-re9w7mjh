class Solution:
    def twoSumSorted(self, nums: List[int], first_num: int) -> List[List[int]]:
        ans = []
        # target is 0
        left, right = 0, len(nums) - 1
        while left < right:
            total_sum = first_num + nums[left] + nums[right]
            if total_sum < 0:
                left += 1
            elif total_sum > 0:
                right -= 1
            else:
                if [first_num, nums[left], nums[right]] not in ans:
                    ans.append([first_num, nums[left], nums[right]]) 
                left += 1
        return ans

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # fix one number, then we have 2sum
        res = []
        nums.sort() # Sort to group duplicate start together
        history = set() # avoid starting at a duplicate number 
        for i in range(len(nums)):
            if nums[i] not in history:
                ans = self.twoSumSorted(nums[i+1:len(nums)], nums[i])
                history.add(nums[i])
                if ans:
                    res+=ans
        return res
