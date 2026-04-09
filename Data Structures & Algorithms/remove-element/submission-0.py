class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # two pointers
        # one pointer points to valid num to write
        # one pointer find the non val target
        # Time O(n)
        # Space O(1)
        wirte = 0
        k = 0
        for find in range(len(nums)):
            if nums[find] != val:
                nums[wirte] = nums[find]
                wirte+=1
                k+=1
        return k