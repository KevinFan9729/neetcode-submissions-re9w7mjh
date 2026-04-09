class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # quick select
        # worst case O(n^2) because you cannot guarantee that partition can be equal
        # after final swap
        # everything left to the partition p is less or equal to nums[p]
        # everything right to the partition p is greater than nums[p]
        # average is O(n)
        k = len(nums) - k
        def quickSelect(l,r):
            pivot = nums[r]
            p = l
            for i in range(l, r):
                if nums[i] <= pivot:#swap
                    nums[i], nums[p] = nums[p], nums[i]
                    p+=1
            nums[p], nums[r] = nums[r], nums[p] # swap pivot with nums[p]
            if k > p: #at right sub array
                return quickSelect(p+1, r)
            elif k <p:
                return quickSelect(l, p-1)
            else:
                return nums[p]
        return quickSelect(0,len(nums)-1)
                
        