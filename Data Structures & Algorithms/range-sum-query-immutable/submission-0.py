class NumArray:
    # Time O(n)
    # Space O(n)
    def __init__(self, nums: List[int]):
        self.nums = nums
        running_sum = 0
        self.prefix_sum = []
        for i in range(len(nums)):
            running_sum+=nums[i]
            self.prefix_sum.append(running_sum)
        
    # Time O(1)
    # Space O(1)
    def sumRange(self, left: int, right: int) -> int:
        if left -1 < 0:
            sub = 0
        else:
            sub = self.prefix_sum[left -1]
        return self.prefix_sum[right] - sub
        

# prefix sum
# sum of any subarray from i to j can be expressed as 
    # sub(i..j) = prefix[j] - prefix[i-1] if i-1<0 then prefix[i-1] == 0

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)