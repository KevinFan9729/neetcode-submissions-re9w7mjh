class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # some kind of graph treversal
        # dfs?
        # keep searching a character
        # once we find a character, we see if we can complete this word or not
        # we need to have a visited set as we cannot repeatively reuse a character
        # dfs(r,c,i) 
        # i is the index of the next character we still need to find
        # we need to bracktrack on failed path
        # Time O(m * n * 4^L) <-exponetial L is the length of the word
        # Space O(m*n)
        ROW, COL = len(board), len(board[0])
        dirs = [[1,0], [0,1], [-1,0],[0,-1]]
        
        def dfs(r,c,i):
            # current node is visited
            visited.add((r,c))
            if i >= len(word):
                return True
            for dx, dy in dirs:
                newR = r + dx
                newC = c + dy
                if (newR < 0 or newC < 0 or newR>=ROW or newC >= COL) or (newR, newC) in visited:
                    continue
                if board[newR][newC] != word[i]:
                    continue
                else:
                    if dfs(newR, newC, i+1):
                        return True
                    # bracktrack, i is local, so no need to backtrack it explicitly
                    visited.remove((newR, newC))
            return False
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == word[0]:
                    # we have a start here
                    visited = set()
                    if dfs(r,c,1):
                        return True
        return False
                

