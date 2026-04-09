class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # at each cell, you have four driections
            # you reach the pacific if you are at row 0 or column 0 
            # you reach the atlantic if you are at row row_count -1 or column column_count -1 
        # for each cell, check if you can reach the pacific AND atlantic
            # if so include it into the answer
            # if not, don't include it into the answer 

        res = []
        rows, cols = len(heights), len(heights[0])
        def canReachPacific(r,c,visited):
            if r == 0 or c == 0:
                return True
            up = False
            left = False
            down = False
            right = False
            visited.add((r,c))
            if (r - 1) >=0 and heights[r][c] >= heights[r-1][c] and (r-1,c) not in visited:
                up = canReachPacific(r-1,c,visited) # move up
                if up:
                    return up
            if (c - 1) >=0 and heights[r][c] >= heights[r][c-1] and (r,c-1) not in visited:
                left = canReachPacific(r,c-1,visited) # move left
                if left:
                    return left
            if (r + 1) < rows and heights[r][c] >= heights[r+1][c] and (r+1,c) not in visited:
                down = canReachPacific(r+1,c,visited) # move down
                if down:
                    return down
            if (c + 1) < cols and heights[r][c] >= heights[r][c+1] and (r,c+1) not in visited:
                right = canReachPacific(r,c+1,visited) # move right
                if right:
                    return right
            visited.remove((r,c))
            return up or left or down or right

        def canReachAtlantic(r,c, visited):
            if r == rows -1 or c == cols -1:
                return True
            up = False
            left = False
            down = False
            right = False
            visited.add((r,c))
            if (r - 1) >=0 and heights[r][c] >= heights[r-1][c] and (r-1,c) not in visited:
                up = canReachAtlantic(r-1,c,visited) # move up
                if up:
                    return up
            if (c - 1) >=0 and heights[r][c] >= heights[r][c-1] and (r,c-1) not in visited:
                left = canReachAtlantic(r,c-1,visited) # move left
                if left:
                    return left
            if (r + 1) < rows and heights[r][c] >= heights[r+1][c] and (r+1,c) not in visited:
                down = canReachAtlantic(r+1,c,visited) # move down
                if down:
                    return down
            if (c + 1) < cols and heights[r][c] >= heights[r][c+1] and (r,c+1) not in visited:
                right = canReachAtlantic(r,c+1,visited) # move right
                if right:
                    return right
            visited.remove((r,c))
            return up or left or down or right

        for r in range(rows):
            for c in range(cols):
                pacific = canReachPacific(r,c, set())
                atlantic = canReachAtlantic(r,c, set())
                if pacific and atlantic:
                    res.append([r,c])
        return res