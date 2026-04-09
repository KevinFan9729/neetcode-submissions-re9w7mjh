import heapq
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # slding window
        # we need to count the occurance of characters inside of the window
        # we need to know the most frequet character inside of a window
        # to get the most frequet efficently, we will needs to use a max heap
        # why do we need to most frequent character
            # bec inside of a window you can replace up to k characters
            # you will need to replace len(window) - occurance of most frequent
            # if k is sufficently large, then we can keep this window
            # if not, we will have to shrink the window 
        # Time O(nlogn)
        # Space O(n)
        if not s:
            return 0
        occ_map = defaultdict(int)
        left = 0
        occ_map[s[left]] = 1
        max_heap = []
        heapq.heappush_max(max_heap, (1, s[left]))
        max_len = 1
        for right in range(1, len(s)):
            win_len = right-left+1
            occ_map[s[right]] += 1
            heapq.heappush_max(max_heap, (occ_map[s[right]], s[right]))
            most_freq_len = max_heap[0][0]
            char_len_to_replace = win_len - most_freq_len
            if char_len_to_replace > k:
                # must shrink the window
                while char_len_to_replace > k and left < right:
                    occ_map[s[left]] -= 1
                    occ, freq_char = max_heap[0]
                    # make sure the top is updated
                    # max_heap[0] is the most frequnet item
                    # we will make sure max_heap[0] is fresh
                    while max_heap and max_heap[0][0] != occ_map[max_heap[0][1]]:
                        heapq.heappop_max(max_heap)
                    most_freq_len = max_heap[0][0]
                    left+=1 # shrink the window
                    win_len = right-left+1
                    char_len_to_replace = win_len - most_freq_len
            win_len = right-left+1
            max_len = max(max_len, win_len)
        
        return max_len
