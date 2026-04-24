class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # stones can really be split into two groups
        # a and b
        # total sum = T
        # subset A sum = s
        # subset B sum = T - s
        # final leftover is sum b - sum a 
        # T-s -s = T- 2s
        # our objective is to find a subset sum that is closest to Sum(total)/2
        # close to half” means minimizing:
        # T/2 - s
        # notice T-2s and T/2-s are proptional
        # why sum(total)/2? bec the absolute best is 0 weight (nothing left)
        # two choices at each step
        # include current to set a, sum of a + curr
        # skip the current for set a sum of a does not change
        # Time O(n*totalSum)
        # Space O(n*totalSum)
        totalSum = sum(stones)
        memo = {}
        def finalDiff(i, currSum): # return the best final diff (best is 0)
            if i == len(stones):
                return abs(totalSum - 2*currSum)
            if (i, currSum) in memo:
                return memo[(i, currSum)]
            
            include = finalDiff(i+1, currSum + stones[i])
            skip = finalDiff(i+1, currSum)

            bestDiff = min(include, skip)
            memo[(i, currSum)] = bestDiff
            return bestDiff

        res = finalDiff(0, 0)
        return res
