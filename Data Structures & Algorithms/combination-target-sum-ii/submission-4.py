class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # we can do backtracking to generate all pairs
        # use sort to group duplicate togather
        # at the same recursion level, we do not want duplicate number to start new branches
        # i represents the start of this recursion level
        # each element can only be chosen once!
        # do we need a used set to track which one is used? no in combo, we dont consider element passed i index
        # Time(num of combo * n)
        # Space (n) not considering output

        candidates.sort()
        res = []
        curr = []
        def gen(i,currSum):
            if currSum == target:
                res.append(curr[:])
                return
            # in combination, we will not consider
            # elements passed i index
            for j in range(i, len(candidates)):
                if currSum + candidates[j] > target:
                    break
                if j > i and candidates[j-1] == candidates[j]:
                    continue
                curr.append(candidates[j])
                gen(j+1, currSum+candidates[j]) # element can only be used once
                curr.pop()
        gen(0,0)
        return res