class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix sum
        # [0,2,1,2,4]
        # any subarray can be expressed as prefix sum
        # we pad the zero to avoid handling edge cases 
        # subarraySum(l, r) = prefix[r + 1] - prefix[l]
        # example 
        # [2,-1,1,2] we want the subarray sum of 0 to 2 [2.-1,1]
        # r =2, l = 0
        #prefix[2+1] = prefix[3] = 2
        #prefix[0] = 0
        # we want subarraySum(l, r) = k
        # we can use a loop to fix an index say r
        # then we are doing
        # k = prefix[r+1] - prefix[l]
        # numNeeded = prefix[r+1] - k
        # use a hashmap to store prefix sums we have seen so far, and how many times each one occurred
        # Time O(n)
        # Space O(n)
        seen = defaultdict(int)
        n = len(nums)
        prefix = [0]* (n+1)
        currSum = 0
        for i in range(n):
            currSum += nums[i]
            prefix[i+1] = currSum
        
        seen[0] += 1 # prefix of 0 exists
        # Fix r as the right endpoint.
        # Current prefix = prefix[r + 1].
        # We need a previous prefix prefix[l] such that:

        # prefix[r + 1] - prefix[l] = k
        count = 0 
        for r in range(n):
            numNeeded = prefix[r+1] - k
            if numNeeded in seen:
                count += seen[numNeeded] # we have this many ways to make subarrays equal to k
            seen[prefix[r+1]]+=1 # prefix sum seen so far
        return count
