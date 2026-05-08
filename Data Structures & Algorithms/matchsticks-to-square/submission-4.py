class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # we need to have four equal sides
        # at the start, we have [0,0,0,0]
        # at every step, can this stick fit in this position?

        total = sum(matchsticks)
        if total % 4 !=0:
            return False
        length = total // 4 # required size for a side
        if max(matchsticks) > length:
            return False # we cannot break sticks
        sides = [0,0,0,0]
        def square(i):
            # at index i, what side should i goes to?
            count = 0
            for side in sides:
                if side == length:
                    count +=1
            if count == 4:
                return True
            
            for pos in range(4):
                stick = matchsticks[i]
                if sides[pos]+ stick > length:
                    continue # this stick cannot fit in this pos
                sides[pos]+=stick
                canForm = square(i+1)
                if canForm:
                    return True
                sides[pos]-=stick #path failed, backtrack

            return False

        res = square(0)
        return res 