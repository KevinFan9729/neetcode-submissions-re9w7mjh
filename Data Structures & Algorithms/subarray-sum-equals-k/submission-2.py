class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix sum
        # [2,-1,1,2]
        # prefix sum
        # [2,1,2,4]
        # sum bewteen i and j equals to prefixSum[j] - prefixSum[i-1]
        # we are looking for prefixSum[j] - prefixSum[i-1] = k
        # we know k, we can lock j in a loop (loop through the array for all possible j)
        # so prefixSum[i-1]= prefixSum[j] - k
        # use a hashmap to store frequency of prefix sum so far
        # if prefixSum[j] - k exists in the hashmap, we know there are subarray that add to k
        # Time O(n)
        # Space O(n)
        seen = defaultdict(int)
        res = 0
        prefixSum = 0
        seen[0] = 1# prefix sum of 0 occurs once (to counter say at the begining, we have a subarray that equals to k)
        for j in range(len(nums)):
            prefixSum += nums[j]
            res += seen[prefixSum - k]
            seen[prefixSum]+=1
        return res
        
