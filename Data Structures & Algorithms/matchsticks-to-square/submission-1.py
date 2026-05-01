class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # a square has 4 equal length shapes
        # it means we need to make 4 sides that have the same length
        # this means we need to know 2 things
            # a what should be the length of the square
            # b if the matchsticks we have can make this square or not
        # a must be totalSum // 4
        # we cannot break sticks

        # ok now how do check if I can make the square with my matches?
        # sides = [0, 0, 0, 0]
        # we can place matches in 4 slots
        # canFrom(i):
            # place matchsticks[i] into one of the 4 sides
        # use recursion
        # for all matches try to say put match on side 1?
        # put match on side 2 etc 
        # if all sides equal to the desired length then we are good


        # why pruning helps
        # say sides = [0, 0, 0, 0]
        # curr = 5
        # target = 10
        # without pruning we would try placing curr to all pos
        # put 5 on side 0 -> [5, 0, 0, 0]
        # put 5 on side 1 -> [0, 5, 0, 0]
        # put 5 on side 2 -> [0, 0, 5, 0]
        # put 5 on side 3 -> [0, 0, 0, 5]

        # Time O(4^n)
        # Space O(n)
        if len(matchsticks) < 4:
            return False
        totalLen = sum(matchsticks)
        if totalLen %4 != 0:
            return False
        sqLen = totalLen // 4
        matchsticks.sort(reverse=True)
        if max(matchsticks) > sqLen:
            return False
        sides = [0,0,0,0]
        def canFrom(i):
            if i == len(matchsticks):
                count = 0
                for side in sides:
                    if side == sqLen:
                        count+=1
                if count == 4:
                    return True
                return False
            seen = set() # each call frame gets their own seen set
            for pos in range(4):
                # Prune: if we already tried putting curr on a side # with this same current length, skip it
                # like [4,4,7,8] curr 4 puting 4 and the first index or the second index is the same 
                if sides[pos] in seen:
                    continue
                if sides[pos] + matchsticks[i] <= sqLen:
                    seen.add(sides[pos])
                    sides[pos] += matchsticks[i]
                    ans = canFrom(i+1)
                    if ans:
                        return True
                    sides[pos] -= matchsticks[i] # backtrack
            return False
        res = canFrom(0)

        return res
        