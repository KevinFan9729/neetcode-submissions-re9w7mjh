from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # slding window
        # we need to count the occurance of characters inside of the window
        # we need to know the most frequet character inside of a window
        # to get the most frequet, we can just search in the occ map
        # the trick is... we only have Upper case characters
        # so we know for a fact that the size of the occ_map  is at max 26 characters
        # why do we need to most frequent character
            # bec inside of a window you can replace up to k characters
            # you will need to replace len(window) - occurance of most frequent
            # if k is sufficently large, then we can keep this window
            # if not, we will have to shrink the window 
        # Time O(n)
        # Space O(1) -> occ_map can only be O(26) at max which is O(1)
        if not s:
            return 0
        occ_map = defaultdict(int)
        left = 0
        occ_map[s[left]] = 1
        max_len = 1
        for right in range(1, len(s)):
            win_len = right-left+1
            occ_map[s[right]] += 1
            # looks like O(n) but no, this is O(1) in time as occ_map has at max 26 characters
            most_freq_len = max(occ_map.values())
            char_len_to_replace = win_len - most_freq_len
            if char_len_to_replace > k:
                # must shrink the window
                while char_len_to_replace > k and left < right:
                    occ_map[s[left]] -= 1
                    if occ_map[s[left]] == 0:
                        del occ_map[s[left]]
                    most_freq_len = max(occ_map.values())
                    left+=1 # shrink the window
                    win_len = right-left+1
                    char_len_to_replace = win_len - most_freq_len
            win_len = right-left+1
            max_len = max(max_len, win_len)
        
        return max_len
