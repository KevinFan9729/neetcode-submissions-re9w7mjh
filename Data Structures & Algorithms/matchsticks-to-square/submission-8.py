class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # a square has 4 sides
        # and all 4 sides must be equal
        # for each match, the match can go to any of the side (choices)
        # we can define a function that tell us if we can form a square or not
        # backtracking
        # Time O(4^n)
        # Space O(n)
        sides = [0,0,0,0]

        # we need to compute the size of a side
        total = sum(matchsticks)
        if total % 4 !=0:
            # we cannot make all sides equal
            return False
        
        size = total // 4

        n = len(matchsticks)
        def canForm(i):
            nonlocal sides
            if i >= n:
                # we run out of matches
                count = 0
                for side in sides:
                    if side == size:
                        count+=1
                if count == 4:
                    return True
                return False
            seen = set()
            for j in range(4):
                if sides[j]+ matchsticks[i] > size:
                    continue
                if sides[j] in seen:
                    continue
                seen.add(sides[j])
                sides[j] += matchsticks[i]
                res = canForm(i+1)# move on to the next match
                if res:
                    return res
                sides[j] -= matchsticks[i]
            return False
        
        ans = canForm(0)
        return ans
