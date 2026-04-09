class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # with a hashset
        # we know that a hashet cannot have duplicate values
        # we are only to utilize this feature in the hashset data structure
        # O(n) time, creating a set from a list will use O(n) time
        # O(n) space, we are using a set that may has the same length as the input array
        dup_check_set = set(nums)
        return len(dup_check_set) != len(nums)
