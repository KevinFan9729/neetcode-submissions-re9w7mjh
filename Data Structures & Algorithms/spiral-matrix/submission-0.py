class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # can we use a visited set to prevent going through the same index?
        # use dfs, as dfs go as deep as possible
            # early return when we have the correct output size (m*n)
        # directions are important! must do right down left up
        # O(m*n) in time 
        # O(m*n) in space
        rows, cols = len(matrix), len(matrix[0])
        output = []
        visited = set()
        def dfs(r,c, prevDir):
            if len(output) == rows*cols:
                return

            visited.add((r,c))
            output.append(matrix[r][c])

            dirs = [[0,1],[1,0],[0,-1],[-1,0]] # right, down, left, up

            dx, dy = prevDir
            move_x, move_y = r+dx, c+dy
            if not (min(move_x, move_y)<0 or (move_x == rows or move_y == cols) or (move_x, move_y) in visited):
                dfs(move_x,move_y, prevDir)# use the previous direction
            else:
                for dx, dy in dirs: # need to search a new direction
                    if len(output) == rows*cols:
                        return
                    move_x, move_y = r+dx, c+dy
                    if (min(move_x, move_y)<0 or (move_x == rows or move_y == cols) or (move_x, move_y) in visited):
                        continue
                    dfs(move_x,move_y, [dx, dy])
        dfs(0, 0, [0,1])
        return output