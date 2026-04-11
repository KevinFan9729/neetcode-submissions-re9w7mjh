class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # each player have two chocies,
        # pick the front or pick the end
        # have a recursive function where define the optional stone this player can get
        # Time O(n^2)
        # Space O(n^2)

        running_sum = 0
        prefix = []
        for i in range(len(piles)):
            running_sum+=piles[i]
            prefix.append(running_sum)
        memo = {}
        def play(front, end):
            if front > end: # impossible, we run out of stones
                return 0
            if (front,end) in memo:
                return memo[(front, end)]
            # sum(piles[front+1:end+1]) subarray sum between front+1:end
            # prefix[end] - prefix[front]
            front_choice = piles[front] + prefix[end] - prefix[front] - play(front+1,end)
            # sum(piles[front:end]) subarray sum between front:end-1
            # prefix[end-1] - prefix[front-1]
            right = 0 if end -1 < 0 else prefix[end-1]
            left = 0 if front -1 < 0 else prefix[front-1]
            end_choice = piles[end] + right - left - play(front,end-1)
            memo[(front, end)] = max(front_choice, end_choice)

            return memo[(front, end)]

        alice = play(0,len(piles)-1)
        bob = sum(piles) - alice
        if alice > bob:
            return True
        return False
