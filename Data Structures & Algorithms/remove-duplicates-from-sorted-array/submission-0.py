class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # oh they are all sorted 
        # meaning all duplicates are grouped together
        # remove duplicates in-place
        # I dont know how to cleanly remove items inside of a list effienctly, with remove(i) function? but that is very slow
        # two pointer
        # slow and fast
        # If nums[fast] == nums[slow] → it’s a duplicate of the last unique → do nothing
        # If nums[fast] != nums[slow] → we found a new unique element
        # we want [0..slow] to be unique
        # so when we see a duplicate do nothing
        # if we a unqiue slow+=1, and copy value of fast to slow so we bubble up the unqiue value
        # Time O(n)
        # Space O(1)
        if len(nums)<2:
            return len(nums)
        slow, fast =0,1
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow+=1
                nums[slow] = nums[fast]
            fast+=1
        return slow+1
