class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # len(nums) = n + 1
        # values are all in [1, n]
        # nums = [1, 2, 3, 2, 2]
        # index:  0  1  2  3  4
        # nums = [1, 2, 3, 4, 4]
        # index:  0  1  2  3  4
        # [1, 3, 4, 2, 2]
        #  0  1  2  3  4
        # bec values are all in [1,n] and we have n+1 int we can correspond value and index togather
        # we will start at an index and use the value as the next pointer
        # this is like a linked list and duplicate will cause cycles
        # we can use a fast and slow pointer to find the cycle 
        # Time O(n)
        # Space O(1)
        i = 0
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
            # there is a cycle
            # we now need to find the beginning of the cycle
            #
            # let:
            # x = distance from start to cycle entrance
            # y = distance from cycle entrance to the first meeting point
            #
            # when slow and fast first meet:
            # slow has travelled x + y steps
            # fast has travelled 2 * (x + y) steps
            #
            # the extra distance fast travelled, x + y, must be a whole number of cycles
            # this implies that walking x steps from the meeting point
            # will also land at the cycle entrance
            #
            # so:
            # - reset one pointer to the start
            # - keep the other at the meeting point
            # - move both one step at a time
            # they will meet at the cycle entrance
                fast = 0
                while fast!= slow:
                    slow = nums[slow]
                    fast = nums[fast]
                return slow
        return slow
