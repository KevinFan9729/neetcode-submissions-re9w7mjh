from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmap
        # we can use a hashmap to count how many characters we have
        # we then decrement item from that hashmap
        # we we ever go under 0, that means we can return false early
        # if after looping through the other string, we still have non-zero item
        # we will return false
        # if we encounter a character that is not inside of our count_map
        # we will return false
        # if all those conditions are not met
        # we return true
        # time O(n) as we loop through strings
        # space O(n) as we use additional hashmap

        count_map = defaultdict(int)
        # increment the map
        for char in s:
            count_map[char] += 1
        # decrement the map
        for char in t:
            if not(char in count_map.keys()):
                return False
            count_map[char] -= 1
            if count_map[char] < 0:
                return False
        if any(count_map.values()) > 0:
            return False
        return True