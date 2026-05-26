class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # I am thinking of some sort of graph treversal
        # but also regions are boarder are not considered surrounded
        # so I am thinking if a region "o" that is not connected with a boarder "o" is considered as surronded
        # I am thinking say I can start from a border "O" and say grow the boder "O" so that they and mark those regions as "N"
        # those "N" slot cannot be marked as surroned, then I just loop through the graph and flip all "O" into "X", and flip back
        # all "N" into "O" again
        # 0,0; 0,1; 0,2; 0,3
        # 1,0; 1,1; 1,2; 1,3
        # 2,0; 2,1; 2,2; 2,3
        # 3,0; 3,1; 3,2; 3,3
        # first row
        # r == 0 c is all
        # last row
        # r == ROW-1 c is all
        # first col
        # c ==0  and r is all,
        # last col
        # c == COL -1, and r is all
        # Time O(m*n)
        # Space O(m*n)
        ROW, COL = len(board), len(board[0])
        # we are starting from a boarder "O" and wants to grow the region
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        def grow(r,c):
            board[r][c] = "N" # mark as not surronded region
            for dx, dy in dirs:
                newR = r + dx
                newC = c + dy
                if newR < 0 or newR >= ROW or newC < 0 or newC >= COL:
                    continue
                if board[newR][newC] == "O":
                    grow(newR, newC)

        # first and last row
        for r in [0,ROW-1]:
            for c in range(COL):
                if board[r][c] == "O":
                    grow(r,c)
        # first and last col:
        for r in range(1,ROW-1):
            for c in [0, COL-1]:
                if board[r][c] == "O":
                    grow(r,c)

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "N":
                    board[r][c] = "O"

        