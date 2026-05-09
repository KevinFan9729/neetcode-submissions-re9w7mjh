class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers
        # left is at the beginning and right is at the end 
        # if sum is equal good, answer is found
        # if sum is smaller, left needs to be incremented to increase the sum
        # if sum is biggeer right needs to be decremented to decrease the sum
        # Time O(n)
        # Space O(1)
        left, right = 0, len(numbers) -1
        while left < right:
            currSum = numbers[left] + numbers[right]
            if currSum == target:
                return [left+1, right+1]
            elif currSum > target:
                right -= 1
            else:
                left += 1
        return [1, -1]