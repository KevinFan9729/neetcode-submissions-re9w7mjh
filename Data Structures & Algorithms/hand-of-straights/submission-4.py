class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # rearrange?
        # hmmmm
        # maybe use a hash table to track how many of digits we have for each?
        # then we can try to find groups starting at each number?
        # we need to have len(hand) // groupSize groups
        # if len(hand) % groupSize != 0 we can return False directly
        # [1,2,4,2,3,5,3,4]
        # [1,2,2,3,3,4,4,5]
        # minimum should be the start of the group?
        # across the whole algorithm: amortized O(n) total for all findSmallest calls combined
        # Time O(nlogn)
        # Space O(n)
        if len(hand) % groupSize != 0:
            return False
        group_num = len(hand) // groupSize
        freq_map = defaultdict(int)
        for num in hand:
            freq_map[num] += 1
        hand_sorted = sorted(hand, reverse = True) # sort array once

        # this is worst case O(n)
        # across the whole algorithm: amortized O(n) total for all findSmallest calls combined
        def findSmallest(freq_map):
            hand_sorted_len = len(hand_sorted)
            for _ in range(len(hand_sorted)):
                if hand_sorted[-1] in freq_map:
                    return hand_sorted[-1]
                else:
                    hand_sorted.pop() # this min is no longer valid 

        # O(m*s) -> O(n/s*s) = O(n)
        for i in range(group_num): # O(m) say group_num = m
            start = findSmallest(freq_map)
            freq_map[start] -= 1
            if freq_map[start] == 0:
                del freq_map[start]
            for _ in range(groupSize-1): # O(s) say group_size = s
                start += 1
                if start in freq_map:
                    freq_map[start] -= 1
                    if freq_map[start] == 0:
                        del freq_map[start]
                else:
                    return False
        return True