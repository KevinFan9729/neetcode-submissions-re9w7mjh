class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # we can use frequency map to record the number of characters in t and in the window
        # use sliding window
        # we keep growing the window until say we have all characters inside of t
        # if we have all characters in t, this means we have a valid subtring canadiate
        # at this case we will shrink until we we no longer have a valid substring
        # then we keep growing
        # if say len s is smaller than length of t we can return immediately
        # Time: O(len(s) + len(t))
        # Space: O(len(s) + len(t))
        # OUZODYXXXAZV  XXYZ
        if len(s) < len(t):
            return ""
        
        window = {}
        tCount = {}
        need = 0
        for char in t:
            if char not in tCount:
                tCount[char] = 0
            tCount[char] += 1
        need += len(tCount)
        have = 0
        left, right = 0, 0
        minLen = float('inf')
        res = [-1, -1]
        while left <= right and right <= len(s)-1:
            if have != need:
                # we dont have a valid window yet
                # keep growing
                window[s[right]] = window.get(s[right], 0) + 1
                if s[right] in tCount and window[s[right]] == tCount[s[right]]:
                    # we have fullfill the need for one unique character 
                    have += 1
            
                while have == need:
                    winLen = right - left + 1
                    if winLen < minLen:
                        # we have found a shorter window
                        # that is valid
                        minLen = winLen
                        res[0] = left
                        res[1] = right
                    # shrink the window
                    window[s[left]] -= 1
                    if s[left] in tCount and window[s[left]] < tCount[s[left]]:
                        have -= 1
                    left +=1
                right+=1
        return s[res[0]:res[1]+1] if minLen != float('inf') else ""
                    