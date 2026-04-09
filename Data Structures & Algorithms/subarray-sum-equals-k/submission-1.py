class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # sub-array must be contiguous
        # brute force is to have a nested loop?
        # keep checking the sum of the array is equal to k or not and count subarrays
        # this is expensive though
        # O(n^2) in time
        # anything better?
        # like a sliding window apporch?
        # hmmm the array is unsorted so 
        # there is no clear condition to grow/decrease the window
        # prefix sum?
        # compute the prefix sum at every index?
        # sum of subarray (from i to j) = prefix_sum at j - prefix_sum at i
        # we want the sum of subarray to be k
        # say prefix_sum at j is the current (which we will know)
        # prefix_sum_at_i = prefix_sum_at_j - k
        # previous_sum = current_sum -k
        # every time we find a 'previous' prefix sum 
        # equal to current_sum - k, 
        # it means the sequence of numbers between that old index 
        # and our current index adds up exactly to k
        # Time O(n)
        # Space O(n)
        count = defaultdict(int)
        count[0] = 1 # empty prefix (empty array)
        # key prefix sum
        # value number of occurance where this sum is encountered
        ans = 0
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum-k in count:
                ans+=count[curr_sum-k]
            count[curr_sum] += 1

        return ans