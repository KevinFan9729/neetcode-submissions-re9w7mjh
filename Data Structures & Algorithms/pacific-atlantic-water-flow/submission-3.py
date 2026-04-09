class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # O(M∗N)
        pacificSet= set()
        atlanticSet = set()
        rows, cols = len(heights), len(heights[0])
        res = []

        def dfs(r, c, reachableSet):
            reachableSet.add((r, c))
            dirs = [[0,1],[0,-1],[1,0],[-1,0]]
            for dx, dy in dirs:
                move_x = r + dx
                move_y = c + dy
                if ( ((move_x, move_y) not in reachableSet) and
                (0<=(move_x)<rows) and 
                (0<=(move_y)<cols) and 
                (heights[move_x][move_y]>=heights[r][c]) ):
                    dfs(move_x, move_y, reachableSet)
        
        # starting from the pacific border (0,n) and (n,0), get all locations that can reach the pacific
        for r in range(rows):
            dfs(r, 0, pacificSet)
        for c in range(cols):
            dfs(0, c, pacificSet)
        
        # starting from the atlantic border (rows-1,n) and (n,cols-1), get all locations that can reach the atlantic
        for r in range(rows):
            dfs(r, cols-1, atlanticSet)
        for c in range(cols):
            dfs(rows-1, c, atlanticSet)

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacificSet and (r,c) in atlanticSet:
                    res.append([r,c])
        return res