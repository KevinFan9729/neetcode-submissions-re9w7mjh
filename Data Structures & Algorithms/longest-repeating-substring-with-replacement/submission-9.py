class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # need to find the most frequent chracter
        # if the count of the most freq character is less than the sequence length
        # then the num of replacement is  seq length - most freq char count
        # as s only contain upper case char, the size is fixed
        # hash map with sliding window
        # Time O(n)
        # Space O(1)
        count = defaultdict(int)
        left = 0
        maxLen = 0
        def findMaxCount(count):
            return max(count.values())
        for right in range(len(s)):
            count[s[right]] += 1
            seqLen = right - left + 1
            mostFreq = findMaxCount(count)
            replaCount = seqLen - mostFreq
            while replaCount > k:
                # shrink the window
                count[s[left]]  -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left +=1
                seqLen = right - left + 1
                mostFreq = findMaxCount(count)
                replaCount = seqLen - mostFreq
            # at this point, the sequece is valid, we try to update the max length
            maxLen = max(maxLen, right - left + 1)
        return maxLen