class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # ok now input may have duplicate
        # we need to avoid duplicates in the output
            # we can do so by sorting the input
            # after sorting all duplicate input elements are grouped
            # we can skip neighbouring grouped duplicate 
        # each step we decide include and not include
        # Time O(2^n)
        # Space O(n)

        candidates.sort()
        res = []
        def dfs(i, curr, curr_sum):
            if curr_sum == target:
                res.append(curr[:])
                return
            if curr_sum > target or i >= len(candidates):
                return
            for j in range(i, len(candidates)):
                if candidates[j] == candidates[j-1] and j>i:
                    continue # skip duplicate start
                    # At the current recursion level, 
                    # if this value is the same as the previous one, skip it 
                    # unless it is the first candidate 
                    # we are considering at this level.
                # include the target 
                curr.append(candidates[j])
                curr_sum+=candidates[j]
                dfs(j+1, curr, curr_sum)

                pop_num = curr.pop() # backtrack
                curr_sum-=pop_num

                # not include is handled by the loop by moving to j
                # the loop decide what to include
        dfs(0,[],0)
        return res