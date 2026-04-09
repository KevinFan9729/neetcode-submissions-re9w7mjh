from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # fixed hashmap of size 26 
        # as we learn from the question the input will be lower case English character only
        # O(n) time
        # O(1) space, as we have a fixed at max 26 characters in the map
        count_map = defaultdict(int) # <- this map will be at max size 26
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            count_map[(s[i])] += 1
            count_map[(t[i])] -= 1
        if any(count_map.values()) != 0:
            return False
        return True
