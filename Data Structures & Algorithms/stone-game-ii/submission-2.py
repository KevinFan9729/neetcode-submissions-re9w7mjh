class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # oh you can only pick from the front
        # but now you can pick x stones from the front of the pile
        # x is bonded by 1<=x<=2m
        # hmmmm does it means we have x choices at every step???
        # recursion
        # play(i,m)
        # Time O(n*x^n)
        # Space O(n)
        # [1,2,3,4]
        # prefix
        # [1,3,6,10]
        # Time O(n^3)
        # Space O(n^2)
        prefix = []
        running_sum = 0
        for i in range(len(piles)):
            running_sum += piles[i]
            prefix.append(running_sum)
        memo ={}
        def play(i,m):
            if i >= len(piles):
                return 0
            if(i,m) in memo:
                return memo[(i,m)]
            alice_choice = 0 
            for x in range(1,min(2*m+1,(len(piles)-i)+1)):
                # sum(piles[i:i+x]) -> stones from i to i+x-1 ->prefix[i+x-1] - prefix[i-1]
                # sum(piles[i+x:]) -> i+x is the start til end -> suffix[i+x]  prefix[-1] - prefix[i+x-1]
                right = 0 if i+x-1 <0 else prefix[i+x-1]
                left = 0 if i-1 <0 else prefix[i-1]
                left2 = 0 if i+x-1 <0 else prefix[i+x-1]
                # alice_choice = max(sum(piles[i:i+x]) + sum(piles[i+x:]) - play(i+x, max(m,x)),alice_choice)
                # alice_choice = max(right - left + tilEnd - play(i+x, max(m,x)),alice_choice)
                alice_choice = max(right - left + prefix[-1] - left2 - play(i+x, max(m,x)),alice_choice)
            memo[(i,m)] = alice_choice
            return alice_choice
        
        res = play(0,1)
        return res
