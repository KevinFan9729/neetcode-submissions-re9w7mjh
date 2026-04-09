class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # slding window?
        # in the window, we need to compute the most frequent character
        # the number of characters need to be replaced in the window is len(window) - frequency of the most frequent character 
        # if number of characters need to be replaced is less or equal to k, good 
            # we can continue to grow the window
        # if numeber of characters need to be replaced is more than k, no
            # we need to shrink the window
        # to get the occurance of the window
            # we can use a hash map 
        # we probably need a halper function to learn which character is the most frequent
            # this would be a linear search in the frequence hash map 
            # thanks fully, we will only have uppercase english characters so we will at most search 26 times
            # so this is O(26) which is constant 
        
        #O(n) in time
        #O(1) in space due to the hashmap being O(26)
        
        freqMap = defaultdict(int)
        def findMostFreq(freqMap):
            maxFreq = -1
            for value in freqMap.values():
                maxFreq = max(maxFreq, value)
            return maxFreq
        left, right = 0, 0
        maxLen = 0
        while left <= right and right <= len(s) - 1:
            freqMap[s[right]] +=1
            length = right - left + 1
            replaceCount = length - findMostFreq(freqMap)
            while replaceCount > k:
                freqMap[s[left]] -=1
                if freqMap[s[left]] == 0:
                    del freqMap[s[left]]
                left +=1
                length = right - left + 1
                replaceCount = length - findMostFreq(freqMap)
                
            maxLen = max(maxLen, length)
            right+=1
        return maxLen