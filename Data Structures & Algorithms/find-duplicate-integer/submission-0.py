class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # we can sort the array so duplicate will be grouped together
        # but sorting usually takes O(nlogn) in time and space can be O(n)
        # hmmm... can we do better?
        # easiest method is to use a hashmap to count occurance
        # we can also use a set to check the set length and the list length
        # that would be Time O(n) and Space O(n)
        # not bad but can we do better?
        # ok we know that the numbers are in the range of [1, n] inclusive
        # can we use this info somehow
        # bucket sort? since n is bounded? 
        # but that is still O (n) in space?
        # think of this array as a directed graph
        # the question is set up so that
            # I can jump to nums[i] without going out of bounds
            # values are valid indices
        # Each index is a node, and it has exactly one outgoing edge to nums[index]
        # so i -> nums[i]
        # in this case duplicate means a cycle
        # for cycle detection, use floyd's fast slow pointer 
        # i.e. slow move one step and fast goes two steps
        # then the slow pointer is inside of the cycle
        # use a new slow pointer and where they (slow and slow2) meet is the entry of the cycle
        
        # we know that we MUST have a cycle here
        # Time O(n)
        # Space O(1)
        fast, slow = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if fast == slow:
                # slow is somewhere in the cycle now
                # and we know we have a cycle
                break

        # phase 2: find the cycle entry (duplicate)
        # From start 0 to cycle entry is distance μ.
        # When slow/fast meet, slow is k steps into the cycle.
        # Resetting one pointer to start and moving both 1 step lines them up 
        # so they meet exactly at the entry after μ steps
        slow2 = 0
        while slow2 != slow:
            slow2 = nums[slow2]
            slow = nums[slow]
        return slow