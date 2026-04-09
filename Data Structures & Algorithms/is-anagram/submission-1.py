from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(n) solution with hash map 
        # key: str, value: int
        hash_map = defaultdict(int)

        # if the length of two strings are different, not anagram
        if len(s) != len(t):
            return False

        # hashmap to count number of characters in input s
        for char in s:
            hash_map[char] += 1
        
        # check the character in input t
        for char in t:
            # if the character of t is not in the hashmap, not anagram
            if char not in hash_map:
                return False
            hash_map[char] -= 1
            # if the character of t occur in dffierent frequency, not anagram 
            if hash_map[char] < 0:
                return False
        return True
        