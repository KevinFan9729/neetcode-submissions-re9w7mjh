class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # subarray sum (i to j) = prefix[j] - prefix[i-1]
        # we want k = prefix[j] - prefix[i-1]
        # prefix[i-1] = prefix[j] - k
        # seen stores how many times each prefix sum has occurred so far
        # a subarray ending at j has sum k if there exists an earlier prefix equal to prefix[j] - k
        # Time O(n)
        # Space O(n)

        seen = defaultdict(int)
        seen[0] = 1 # prefix sum : how many
        prefix = []
        currSum = 0
        for num in nums:
            currSum += num
            prefix.append(currSum)
        
        res = 0
        for j in range(len(nums)):
            sumNeeded = prefix[j] - k
            if sumNeeded in seen:
                res += seen[sumNeeded]
            seen[prefix[j]] += 1
        return res