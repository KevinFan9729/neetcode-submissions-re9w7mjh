class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 is shorter or equal to s2 for s2 to have a permutation of s1
        # if this is not true, we can return instantly
        # in the length window/chunk of len(s1)
        # we can check if say s2 has a window such that it has all characters in s1
        # sliding window of fixed size of len of s1
        # hash set is not good idea <-we may duplicate characters
        # hashmap is probably good?
        # we can build the hashmap in s2 gradually and compare
        # say n is length of s1, m is length of s2
        # Time(m*n)
        # Space O(n)
        if len(s1) > len(s2):
            return False

        s1Map = {}
        for char in s1:
            if char not in s1Map:
                s1Map[char] = 0
            s1Map[char] += 1
        s2Map = {}
        for i in range(len(s1)):
            if s2[i] not in s2Map:
                s2Map[s2[i]] = 0
            s2Map[s2[i]] += 1
        # check the first window
        if s1Map == s2Map:
            return True
        left = 0
        for right in range(i+1, len(s2)): # o(m) 
            s2Map[s2[left]]-=1
            if s2Map[s2[left]] == 0:
                del s2Map[s2[left]]
            left+=1
            if s2[right] not in s2Map:
                s2Map[s2[right]] = 0
            s2Map[s2[right]] += 1
            # now a new window is complete, check
            if s1Map == s2Map: # O(n)
                return True
        # check the last window
        if s1Map == s2Map:
            return True
        return False