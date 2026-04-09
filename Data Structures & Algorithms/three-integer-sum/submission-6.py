class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # if we can lock one digit, then we have two sum!
        nums.sort()# group all duplicate together
        res = []
        history =set()
        def twoSum(fixedNumIdx):
            # print(fixedNumIdx)
            target = 0 - nums[fixedNumIdx]
            diffMap = {}
            for i in range(fixedNumIdx+1, len(nums)): # we should not include the fixedNumIdx thus we start at fixedNumIdx+1
                diff = target - nums[i]
                if diff in diffMap:
                    if (nums[fixedNumIdx], nums[i], diff) not in history:
                        res.append([nums[fixedNumIdx], nums[i], diff])
                        history.add((nums[fixedNumIdx], nums[i], diff))
                diffMap[nums[i]] = i
        i=0
        while i < len(nums):
            print(i)
            while i - 1 >= 0 and i < len(nums) and nums[i - 1] == nums[i]: # skip duplicate starting points
                i+=1
            if i < len(nums):
                twoSum(i)
            i+=1
        return res