from collections import defaultdict
import copy
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # hmmm hashmap?
        # permutation means s1 and s2 have the same characters. order does not matter
        # we always check if s2 contains a permutation of s1 (stated in the question)
        # but one detail of the question is that the s2's substring must contain permutation of s1
        # substring means the characters must be continous
        # sliding window?
        # now we know the window size needs to be the length of s1
        # just need to find the start of the window
            # the start of the window is left pointer pointing to a char in s2 that has a char in s1
            # then the window is s2[left: left+len(s1)]

        # TIme O(len(s1)* len(s2))
        # Space O(1) # only 26 characters

        s1_map = defaultdict(int)

        if len(s2) < len(s1):
            return False

        for char in s1:
            s1_map[char] += 1
        
        for left in range(len(s2)):
            if s2[left] in s1_map:
                s1_map_copy = copy.deepcopy(s1_map)
                window = s2[left: left+len(s1)]
                for char in window:
                    if char in s1_map_copy:
                        s1_map_copy[char] -= 1
                        if s1_map_copy[char] == 0:
                            del s1_map_copy[char]
                if not s1_map_copy:
                    return True

        return False