class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Time O(n*m)
        # Space O(1)
        res = []
        index = 0
        while True:
            # use the first string as the reference 
            if index < len(strs[0]):
                target = strs[0][index]
            else:
                # first string is too short
                # no target
                break
            for item_idx in range(1, len(strs)):
                # once we have a mismatch here, we know
                # we have to stop
                if index>= len(strs[item_idx]):
                    # the item is too short
                    return "".join(res)
                if strs[item_idx][index] != target:
                    # a mistmatch
                    return "".join(res)
            # if we are here, the inner loop is done without
            # returning
            res.append(target)
            index +=1
        return "".join(res)


