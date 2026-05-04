class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # sentor always want to ban the ealy opponet
        # why
        # bec a early oppposing senator can ban you
        # maybe have a R queue and D queue
        # say RRDDD
        # R queue:  0, 1
        # D queue:  2, 3, 4
        
        # check R and D front,
        # R is smaller than D, R becomes curr+len(senate) goes to the back of the R queue
        # D's front is deleted (as it was banned)
        # then we have 1 vs 3, 3 is removed(banned), etc
        # until say one queue is empty
        
        # we can just use curr+len(senate) to simulate stepping back to the queue as we only care about relative order
        # we dont care about actual order (otherwise every update needs to update all element as the overall length is shorter)

        # Banned senators are effectively removed from future turns.
        # Instead of physically maintaining a shrinking circular list,
        # use curr + n to place the surviving senator after one full original cycle.
        # This preserves the relative turn order among remaining active senators.
        # Time O(n)
        # Space O(n)

        r = deque()
        d = deque()
        num = len(senate)
        for i in range(num):
            if senate[i] == "R":
                r.append(i)
            else:
                d.append(i)

        while r and d:
            rFront = r.popleft()
            dFront = d.popleft()
            if rFront < dFront:
                r.append(rFront + num) # back to the line 
            else:
                d.append(dFront + num)

        if r:
            return "Radiant"
        return "Dire"