class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_set = set(nums)
        return not(len(check_set) == len(nums))
         