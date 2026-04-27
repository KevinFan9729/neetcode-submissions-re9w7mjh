class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # the way that defines effort is odd
        # we need to be careful of say big differences while navigating
        # local decision will not help here
        # we may need to actually get all paths?
        # very expensive though?
        # every step we have four directions
        # 4^n?
        # The answer is some number between 0 and max height difference.
        # Instead of trying all paths, I can guess an effort limit X.
        # Given X, I can use BFS/DFS to check whether the destination 
        # is reachable while only taking moves whose height difference <= X.
        # Because if X works, any larger X also works, and if X fails, 
        # any smaller X also fails, I can binary search the minimum working X.
        # Time O(m * n * log K)
        # Space O(m*n)
        sys.setrecursionlimit(2000)
        maxVal, minVal = max(map(max, heights)), min(map(min, heights))
        ROWS, COLS = len(heights), len(heights[0])
        left, right = 0, abs(maxVal - minVal)
        def dfs(r,c): # O(m * n) as each cell only get visited once
            nonlocal maxWeight
            seen.add((r,c))
            if r == ROWS - 1 and c == COLS - 1:
                return True
            dirs = [[0,1],[0,-1],[1,0],[-1,0]]
            for d in dirs:
                newR = r+d[0]
                newC = c+d[1]
                if (newR <0 or newR >=ROWS or newC <0 or newC >=COLS or (newR, newC) in seen
                or abs(heights[newR][newC] - heights[r][c]) > maxWeight):
                    continue
                ans = dfs(newR, newC)
                if ans == True:
                    return ans
                # No seen.remove(): this is reachability, not path enumeration.
                # Once a cell is reachable under maxWeight, revisiting it via another path is unnecessary.
                # seen.remove((newR, newC))
            return False
        minWeight = float('inf')
        while left <= right:
            maxWeight = left + (right-left)//2
            seen = set()
            canReach = dfs(0,0)
            if not canReach:
                # weight assigned is too low
                # cannot reach, increase the allowed weight
                left = maxWeight + 1
            else:
                # weight assigned can be reached,
                # we may have found the best weight, or even less weight can do
                minWeight = min(minWeight, maxWeight)
                right = maxWeight -1
        return minWeight
