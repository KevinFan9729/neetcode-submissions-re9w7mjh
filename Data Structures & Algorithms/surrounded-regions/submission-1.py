class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # find a "o"
        # determine this "o" is surrounded or not
        
        rows, cols = len(board), len(board[0])
        def markIsland(r,c):
            nonlocal clearSet
            if ((min(r,c)<= 0 or (r == rows -1 or c == cols -1)) 
                and board[r][c] == "O"): # o that are on borders will never be surrounded
                clearSet = True # mark the set as invalid
                visited.add((r,c))
                return
            if ((min(r,c)< 0 or (r == rows or c == cols) or 
            ((r,c) in visited))):
                return
            if board[r][c] == "X": # hit an x 
                return
            visited.add((r,c))
            islandSet.add((r,c))
            dirs = [[0,1],[0,-1],[1,0],[-1,0]]
            for dx, dy in dirs:
                markIsland(r+dx, c+dy)
        visited = set()
        islandSet = set()
        for r in range(rows):
            for c in range(cols):
                if ((board[r][c] == "O") and ((r,c) not in visited)):
                   clearSet = False
                   markIsland(r,c)
                   if clearSet:
                       islandSet.clear()
                   while islandSet:
                        pos_x, pox_y = islandSet.pop()
                        board[pos_x][pox_y] = "X"