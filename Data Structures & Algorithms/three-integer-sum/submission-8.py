from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums[i] + nums[j] + nums[k] == 0
        # nums[i] + nums[j] == 0-nums[k] where -nums[k] is the target
        # now we can do a two sums where -nums[k] is the target
        # two sum can be solved with O(n)
        # now the not having the duplicate part
        # so -1,0,1 and 0,1,-1 are considered as duplicates
        # we can sort
        # can we have a set to check or remove duplciates?
        # Time O(n^2)
        # Space O(n) due to the hashmap 
        
        # 2 sum
        def twoSum(nums: List[int], skipped_idx: int, target:int):
            # O(n)
            res = set()
            diff_map = defaultdict(int)
            for i in range(len(nums)):
                if i == skipped_idx:
                    continue
                diff = target - nums[i]
                diff_map[diff] = i
            for i in range(len(nums)):
                if i == skipped_idx:
                    continue
                if nums[i] in diff_map:
                    if i != diff_map[nums[i]]: # make sure we do not have duplicate indices
                        max_canadaite = max([nums[i], nums[diff_map[nums[i]]]])
                        min_canadaite = min([nums[i], nums[diff_map[nums[i]]]])
                        res.add(tuple([min_canadaite, max_canadaite]))
            return res
        res = set()
        for i in range(len(nums)):
            target = -nums[i]
            temp = twoSum(nums, i, target)
            if not temp:
                continue
            for item in temp:
                item_ls = list(item)
                item_ls.append(nums[i])
                res.add(tuple(sorted(item_ls))) # sort is O(nlogn) but we always only have 3 elements so O(1) in time
        out = []
        for item in res: # convert to output type
            out.append(list(item))
        return out

            