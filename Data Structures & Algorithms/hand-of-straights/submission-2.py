class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize !=0:
            return False
        # we can use a min heap
        # we also need to count the occurance of each distinct number
        # once we have that we will make a list of list [[number, occurance]]
        # we will turn that list of list into a min heap we will keep poping from the heap
        # compare the previous with the popped value,
        # if the previous is -1 (indicating the start of a new grop)
        # or previous +1 == popped value, then the popped value is valid, we can
        # count that value as a member of the group.
            # if conditions are not met, return False immediately 
        # we will decrement the occurance of that number, if the occurance is not equal to 0
        # store that pair in a temp storage 
        # continue until we made up a group
        # push back item from the tmp storage back to the heap before making a new group
        
        # O(n*log(n)) in time
        # O(n) space due to the hashmap and heap
        
        occurance_map = defaultdict(int)
        for num in hand: # O(n)
            occurance_map[num] += 1
        
        minHeap = []
        for num, occurance in occurance_map.items(): # O(n)
            minHeap.append([num,occurance])
        heapq.heapify(minHeap) # O(n)

        tmp = []
        while minHeap: # O(n/m) say groupsize is m
            prev = -1
            curr_size = 0
            while curr_size != groupSize: # O(groupsize) say groupsize is m so O(m)
                if minHeap:
                    pair = heapq.heappop(minHeap) #O(logn)
                    if prev == -1 or prev+1 == pair[0]:
                        curr_size+=1
                        prev = pair[0]
                        pair[1]-=1
                        if pair[1] >0:
                            tmp.append(pair)
                    else:
                        return False
                else:
                    return False # run out of number without forming the group completely
            while tmp: # repopulate the minheap with with numbers that are not used up O(m), tmp is at most size m
                pair = tmp.pop() 
                heapq.heappush(minHeap, pair) #O(logn)
        return True