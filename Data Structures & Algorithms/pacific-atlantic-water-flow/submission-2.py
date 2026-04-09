from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows, cols = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(r, c, reachable_set):
            reachable_set.add((r, c))
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (nr, nc) not in reachable_set and (0 <= nr < rows) and (0 <= nc < cols) and (heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, reachable_set)

        # Perform DFS from the Pacific Ocean's border
        for r in range(rows):
            dfs(r, 0, pacific_reachable)
        for c in range(cols):
            dfs(0, c, pacific_reachable)

        # Perform DFS from the Atlantic Ocean's border
        for r in range(rows):
            dfs(r, cols - 1, atlantic_reachable)
        for c in range(cols):
            dfs(rows - 1, c, atlantic_reachable)

        # Find all cells that can reach both oceans
        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific_reachable and (r, c) in atlantic_reachable:
                    result.append([r, c])

        return result
