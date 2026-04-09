class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # quick sort
        # worst case O(n^2) because you cannot guarantee that partition can be equal
        # after final swap
        # everything left to the partition p is less or equal to nums[p]
        # everything right to the partition p is greater than nums[p]
        # average is O(nlogn)
        k = len(nums) - k
        def quickSort(l,r):
            if l == r:
                return
            if l > r:
                return
            pivot = nums[r]
            p = l
            for i in range(l, r):
                if nums[i] <= pivot:#swap
                    nums[i], nums[p] = nums[p], nums[i]
                    p+=1
            nums[p], nums[r] = nums[r], nums[p] # swap pivot with nums[p]
            quickSort(p+1, r) # sort left average O(logn)
            quickSort(l, p-1) # sort right average O(logn)
        quickSort(0,len(nums)-1)
        return nums[k]
                
        