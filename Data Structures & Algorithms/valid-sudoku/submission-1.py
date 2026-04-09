from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # the 3 by 3 sub grid part is tricky
        # we can use a hashset to track numbers
            # we will use hash sets to track rows
            # hash sets to track columns
            # hash sets to track the the 3 by 3 grids???
        # ok to navigate, just use a nested loop
        # 9 row_sets 9 column sets and 9 square sets
        # for the grid, we needs to map the 3x3 grid indices to the 9x9 board
            # modulus is our friend!
            # the board row index % 3 == grid row index
            # the board column index %3 == grid column index
        # We also need to figure out a way to compute which grid we are on!
        # board_row//3 and board_col//3 can tell you which board you are on!
        # you will get label like 00, 01, 02, 10, 11, 12, 20...
        # Time O(n^2) but because we know we have a 9*9 fixed input size so its really O(1)
        # Space O(n^2) but again because we know its fixed O(1)
        row_check = defaultdict(set) # size 9
        col_check = defaultdict(set) # size 9
        grid_check =defaultdict(set) # size 9
        grid = [[0 for _ in range(3)] for _ in range(3)] # temp grid

        for board_row in range(len(board)):
            for board_col in range(len(board[1])):
                if board[board_row][board_col] in row_check[board_row] and board[board_row][board_col]!=".":
                    return False # row check failed
                if board[board_row][board_col] in col_check[board_col] and board[board_row][board_col]!=".":
                    return False # column check failed
                grid_row = board_row%3
                grid_col = board_col%3
                gird_label = (board_row//3, board_col//3)

                row_check[board_row].add(board[board_row][board_col])
                col_check[board_col].add(board[board_row][board_col])
                grid[grid_row][grid_col] = board[board_row][board_col] # <= grid will be a list of list 3x3
                if grid[grid_row][grid_col] in grid_check[gird_label] and grid[grid_row][grid_col]!=".":
                    return False # grid check failed
                grid_check[gird_label].add(grid[grid_row][grid_col])
        return True

