from collections import defaultdict
class Solution:
    def find_most_freq_char_count(self, count_map):
        max_val = 0
        for val in count_map.values():
            if val > max_val:
                max_val = val
        return max_val


    def characterReplacement(self, s: str, k: int) -> int:
        L, R = 0, 0
        max_len = 0
        count_map = defaultdict(int)
        for c in s[L:R+1]:
            count_map[c] += 1
        while L <= R and R < len(s):
            most_frequent_count_in_window = self.find_most_freq_char_count(count_map)
            wind_len = R - L +1 
            num_char_to_replaced = wind_len - most_frequent_count_in_window
            if num_char_to_replaced <= k: #window is valid
                max_len = max(max_len, wind_len)
                R += 1 # expand the window
                if R < len(s):
                    count_map[s[R]] +=1
            else: #window is not valid
                if L < len(s):
                    count_map[s[L]] -=1
                L += 1 # shrink the window
        return max_len