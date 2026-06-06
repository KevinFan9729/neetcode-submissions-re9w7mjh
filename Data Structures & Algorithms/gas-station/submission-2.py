class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # we can compute a diff array
        
        # [-1,-1,1]
        # scan left to right;
        # if current candidate start fails at i,
        # then every station from start to i is impossible;
        # next possible start is i + 1
        # think about it, if you fail along the path, this means staring anywhere in that path will also become negative
        # bec the start to the mid should be not negative, otherwise we would fail ealier 

        # we can ue the diff map to do the simulation
        # diff map is basically net gas after payment
        # if we can start at some index, and if we can reach start-1 and tank is still non-negative, then start is the answer
        # [-1,0,-1,3]
        # Time O(n) as invlaid starts are skipped
        # Space O(n)
        if sum(gas) < sum(cost):
            # total gas is smaller than total cost
            return -1
        n = len(gas)
        diff = []
        for i in range(n):
            diff.append(gas[i]-cost[i])

        start = 0

        while start <= n-1:
            tank = diff[start]
            if tank < 0:
                start += 1
                continue
            i = (start+1)%n # start from the next index
            count = 0 
            while count <n: # loop through a cycle
                tank += diff[i]
                if tank < 0:
                    start = (i+1)%n
                    break
                if i == (start - 1)%n and tank >=0:
                    return start
                count+=1
                i+=1
                i = i%n

        return -1

