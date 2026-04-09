class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # sorted is the important piece
        # if num1+num2 == targte, the result is found
        # if num1+num2 > target we need to reduce the sum
        # if num1+num2 < target we need to increase the sum
        # two pointers!
        # Time O(n)
        # Space O(1)

        left, right = 0, len(numbers)-1
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left+1, right+1] # 1-indexed
            elif curr_sum > target: # must reduce the sum
                right -= 1
            elif curr_sum < target: # must increase the sum
                left += 1
        
        return [left+1, right+1]

