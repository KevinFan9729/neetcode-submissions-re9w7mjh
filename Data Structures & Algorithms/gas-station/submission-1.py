class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # we can compuete a diff and then perform the simulation with running sum of diff
        # say we start with a non negative diff pos and perfrom the simulation
        # say with this start index, we become negative somehow when traveling to j and j!=i,
        # this means i cannot be the start, and all stations betwenn i and j cannot be start
        # this bec, say j is very bad, none of the starting bewteen i and j will overcome this bad pos,
        # the next try must be j+1
        # globally, if we dont have enough gas, then we know it will not work
        # Time O(n) as we skip invalid starts
        # Space O(n)
        if sum(gas) < sum(cost):
            return -1
        # [-1,0,-1,3]
        # [-1, -1, 1]
        arrLen = len(gas)

        diff = []
        for i in range(arrLen):
            diff.append(gas[i]-cost[i])
        startIndex = 0
        while startIndex <= arrLen-1:
            if diff[startIndex] < 0:
                startIndex +=1
                continue
            tank = 0
            negFlag = False
            for j in range(arrLen):
                tank+= diff[(startIndex+j)%arrLen]
                if tank < 0:
                    startIndex = (startIndex+j)%arrLen +1
                    negFlag = True
                    break
            # if we have a round trip and never negative, then it is good
            if not negFlag:
                return startIndex

        return -1
