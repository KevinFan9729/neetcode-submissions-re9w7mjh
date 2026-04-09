class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # solution demands to have O(1) space
        # thus we cannot use a diff hashmap
        # two pointers
        # the array is SORTED
        # maybe we need to start from two ends?
        # if the sum is larger than target
            # we need to reduce the sum i.e. right-=1
        # if the sum is less than the target
            # we need to increase the sum i.e left +=1
        # Time O(n)
        # Space O(1)
        left, right = 0, len(numbers)-1
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left+1, right+1]
            elif curr_sum > target:
                right -= 1
            else:
                left +=1
        return []