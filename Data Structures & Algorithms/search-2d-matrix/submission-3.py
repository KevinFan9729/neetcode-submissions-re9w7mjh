class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # we can also use bfs to solve this problem
        # go through nodes level by levels
        # O(m*n) due to visited 
        # O(m*n) due to visited 
        rows, cols = len(matrix), len(matrix[0])
        def bfs():
            q = deque()
            visited = set()
            dirs = [[0,1],[0,-1],[1,0]] # don't need to move up
            q.append((0,0))
            visited.add((0,0))
            while q:
                q_len = len(q)
                for _ in range(q_len):
                    r,c = q.popleft()
                    if matrix[r][c] == target:
                        return True
                    for dx, dy in dirs:
                        move_x, move_y = r+dx, c+dy
                        if (min(move_x, move_y)< 0 or (move_x == rows or move_y == cols) or
                        (move_x, move_y) in visited):
                            continue
                        q.append((move_x, move_y))
                        visited.add(((move_x, move_y)))
            return False
        ans = bfs()
        return ans

        