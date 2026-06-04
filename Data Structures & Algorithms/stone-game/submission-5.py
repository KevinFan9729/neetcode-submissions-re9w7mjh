class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # we can define a function which return the 
        # CURRENT player's max advantage
        # advantage is define as current player score - opposing player score
        # say A takes the front
        # A’s total is: piles[front] + A_remaining_score
        # B's total score B_remaining_score 
        # A_total - B_total = piles[front] + A_remaining_score - B_remaining_score
        # A_total - B_tota = piles[front] - (B_remaining_score - A_remaining_score)
        # (B_remaining_score - A_remaining_score) = maxAv(front+1, end)
        # A_total - B_total =  piles[front] - maxAv(front+1, end)


        # each step, the player has 2 choices
        # take from the front or take fron the back

        # Time O(n^2)
        # Space O(n^2)
        total = sum(piles)
        memo = {}
        def maxAv(front, end):
            if front == end:
                # only one stone left
                return piles[front]
            if (front, end) in memo:
                return memo[(front, end)]
            # current advantage is your immediate gain minus their future advantage
            takeFront = piles[front] - maxAv(front+1, end)
            takeEnd = piles[end] -  maxAv(front, end-1)
            maxVal = max(takeFront, takeEnd)
            memo[(front, end)] = maxVal
            return maxVal
        alice = maxAv(0, len(piles)-1)
        if alice >0:
            return True
        return False