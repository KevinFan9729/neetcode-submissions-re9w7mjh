class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers, left and right, sum of left and right number,
        # if sum > target, right --, if sum < target, left ++,
        # if sum == target, return [left, right]
        # this works becuase we have a sorted array, where the biggest value are on the right
        # and the smallest values are on the left.

        left, right = 0, len(numbers)-1
        while left < right: # left and right cannot be the same index in this question
            s = numbers[left] + numbers[right]
            if s > target:
                right -= 1
            elif s < target:
                left += 1
            else:
                return [left + 1, right + 1]
        return [left +1 , right + 1]


        