class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # backtracking
        # choose the next valid larger number to append at each step
        # Time O(C(n, k)*k) n choose k combinations and each recursion depth is k
        # Space O(n)
        res = []
        def dfs(start, curr):
            if len(curr) == k:
                res.append(curr[:])
                return
            for i in range(start, n+1):
                curr.append(i)
                # we cannot reuse the number less than the current num
                dfs(i+1, curr)
                curr.pop()
        dfs(1,[])
        return res