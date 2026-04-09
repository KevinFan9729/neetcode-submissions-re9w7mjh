class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # assume they play optimally
        # what does that mean?
        # do they play optimally locally?
        # lets see...
        # hmmm
        # [1,2,40,10]
        # alice takes 10
        # bob takes 40
        # alice takes 2
        # bob takes 1
        # aha, greedy does not work here!
        # so greedy is not optimal!

        # at each step, each player has 2 chocies
            # pick the front
            # pick the back
        # recursion?
        # best_pick(i,j) -> the maximum stones the current player can secure from i..j
        # i is pick the start j is pick the end?
        # if i > j then the game is over?
        # to pick front we do nums[i] + sum(piles[i+1:j+1]) - best_pick(i+1, j)
        # to pick the back we do nums[j] + sum(piles[i:j]) - best_pick(i, j-1)
        # Time O(n^2)
        # Space O(n^2)
        memo = {}
        prefix = []
        running_sum = 0
        for x in piles:
            running_sum += x
            prefix.append(running_sum)

        def range_sum(l, r):
            if l > r:
                return 0
            if l == 0:
                return prefix[r]
            return prefix[r] - prefix[l - 1]

        def best_pick(i, j):
            if i > j:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            pick_front = piles[i] + range_sum(i + 1, j) - best_pick(i + 1, j)
            pick_back = piles[j] + range_sum(i, j - 1) - best_pick(i, j - 1)

            memo[(i, j)] = max(pick_front, pick_back)
            return memo[(i, j)]

        alice_pick = best_pick(0, len(piles) - 1)
        bob_pick = prefix[-1] - alice_pick

        return alice_pick > bob_pick