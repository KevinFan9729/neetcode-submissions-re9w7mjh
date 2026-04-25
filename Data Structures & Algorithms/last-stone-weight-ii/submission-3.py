class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # stones can really be split into two groups
        # so the smashing and picking can be expressed as a series of + - 
        # say we have [2,4,1,5,6,3] we can do 2 and 4 4-2 = 2; then 2 and 3, 
        # so 3-2 = 1 and 1 -1 =0 and 5-6 =1 which is 3-(4-2)-1+(5-6)
        # = 3-4+2-1+5-6= 3+5+2-4-1-6 = (3+5+2)- (4+1+6)
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
        halfSum = totalSum /2
        memo = {}
        def finalSubsetSum(i, currSum): # return the best final diff (best is 0)
            if i == len(stones):
                return currSum
            if (i, currSum) in memo:
                return memo[(i, currSum)]
            
            include = finalSubsetSum(i+1, currSum + stones[i])
            skip = finalSubsetSum(i+1, currSum)
            includeDiff = abs(halfSum - include)
            skipDiff = abs(halfSum - skip)
            if includeDiff < skipDiff:
                bestSum = include
            else:
                bestSum = skip
            memo[(i, currSum)] = bestSum
            return bestSum

        bestSubSum  = finalSubsetSum(0,0)
        res = abs(totalSum - 2*bestSubSum)
        return res
