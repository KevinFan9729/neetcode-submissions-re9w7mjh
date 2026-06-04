class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # we know the group size
        # we know how many elements we have
        # so how many groups we must make?
        if len(hand) % groupSize != 0:
            return False
        numOfGroup = len(hand) // groupSize
        # will sorting help?
        # [1,2,2,3,3,4,4,5]
        # should we always start at the smallest element in start?
        # yes we should
        # we can use a hashmap to count how many of the each number we have
        # then we always start at the smallest element and try to make group
        # until we can make all groups
        # say the groupsize is m
        # n/m * m
        # Time O(number of group * group size) -> O(n/m*m) -> O(n+nlogn)
        # Space O(n)
        hand.sort()
        freqMap = {}
        for num in hand:
            if num not in freqMap:
                freqMap[num] = 0
            freqMap[num] += 1
        groupCount = 0
        def grow(start): # Time O(m)
            size = 1
            freqMap[start] -= 1
            # next item should be start+1
            while size != groupSize and freqMap.get(start+1, -1) >0:
                start = start+1
                freqMap[start] -=1
                size += 1
            if size == groupSize:
                return True
            return False
            
        group = 0
        for start in hand:
            if freqMap.get(start, -1)>0:
                res = grow(start)
                if res:
                    group += 1
                else:
                    return False
        if group == numOfGroup:
            return True
        return False

        
