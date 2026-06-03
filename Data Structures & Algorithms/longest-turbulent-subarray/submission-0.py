class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # return the max len turbulent subarray staring at i
        # Time O(n) as we have n*2 unique state 
        # space O(n)

        memo = {}
        def findMax(i, expectUp):
            if i >= len(arr)-1:
                # we are at the last element
                return 1
            if (i, expectUp) in memo:
                return memo[(i, expectUp)]
            
            curr = arr[i]
            nextItem = arr[i+1]
            extend = 0
            maxLen = 0
            if curr < nextItem and expectUp:
                # next check should compare smaller 
                extend += 1 + findMax(i+1, not expectUp)
            elif curr > nextItem and not expectUp:
                extend += 1 + findMax(i+1, not expectUp)
            else:
                # if the link is broken, new start length is 1
                return 1
            maxLen = max(maxLen, extend)
            memo[(i, expectUp)] = maxLen
            return maxLen
        res = 0
        for start in range(len(arr)):
            try1 = findMax(start,True)
            try2 = findMax(start,False)
            res = max(try1, try2, res)
        return res