class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_set = set()
        # this method is a bit better than comparing set length with the list length
        # as it do early stopping when a duplicate is detected. However, it is still
        # O(n) time wise
        for n in nums:
            if n in check_set:
                return True
            check_set.add(n)
        return False
         