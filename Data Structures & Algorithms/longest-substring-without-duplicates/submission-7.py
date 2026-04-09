from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we should use a set?
        # one note is that the substring must be CONTIGUOUS
        # grow the substring while keep updating the set?
        # determining the new start of the substring is a problem? maybe use a hashmap to track the index as well?
        # the key is to determine the start of the substring
            # when encountering a unqiue character, easy,just update
            # when encountering a duplicate character
                # the shrinking logic needs to be like:
                    # check where what is the index of that duplicate character in the hashmap
                    # we cannot have that character in the substring when including this new duplicate character
                    # so the new start is the last_seen_indx +1 
        # you loop once and keep track of the max len of the substring
        # Time O(n)
        # Space O(m) where m is the size of the longest unqiue substring

        left = 0 # <= points to the start of the substring
        substring_map = defaultdict(int)
        max_len = 1
        if len(s)==0:
            return 0
        substring_map[s[0]] = 0

        for right in range(1, len(s)):
            # if we've seen this char and it's inside the current window
            if s[right] in substring_map and substring_map[s[right]] >= left:
                # move left to one past the last occurrence
                last_seen_idx = substring_map[s[right]]
                # new start of the substring
                left = last_seen_idx + 1
            # update the last seen index of this character
            substring_map[s[right]] = right
            max_len = max(max_len, right - left + 1)
        return max_len