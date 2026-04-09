class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacificSet = set()
        atlanticSet = set()
        # we will do dfs on the graph, and populate the pacificSet and atlanticSet
        # then we will find the intersection of both sets, that will be our answer
        # how to reach pacific?
            # you can move to a cell where r == 0 or c == 0
        # how to reach the atlantic?
            # you can move to a cell where r == len(heights)-1 or c == len(heights[0]) -1
        rows, cols = len(heights), len(heights[0])

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
            if (r,0) not in pacificSet:
                dfs(r, 0, pacificSet)
        for c in range(cols):
            if (0,c) not in pacificSet:
                dfs(0, c, pacificSet)
        
        # starting from the atlantic border (rows-1,n) and (n,cols-1), get all locations that can reach the atlantic
        for r in range(rows):
            if (r, cols-1) not in atlanticSet:
                dfs(r, cols-1, atlanticSet)
        for c in range(cols):
            if (rows-1, c) not in atlanticSet:
                dfs(rows-1, c, atlanticSet)
           

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacificSet and (r,c) in atlanticSet:
                    res.append([r,c])
        return res