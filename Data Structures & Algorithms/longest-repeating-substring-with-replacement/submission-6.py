class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window?
        # in the current window, how many characters are not the most frequent one
        # we can know which letter to replace by finding the non-majority character in the window
        # we keep expanding the window when
            # we only have one class of character in the window
            # minority count is less or equal to k
        # we shrink the window when
            # minority count is more than k
        # use a min heap to find minority

        windowMap = defaultdict(int)
        maxHeap = []
        left, right = 0,0
        maxLen = 0
        needToReplace = -1

        while left <= right and right <= len(s)-1:
            if len(windowMap) <=1 or needToReplace <= k:
                # valid
                windowMap[s[right]]+=1
                heapq.heappush_max(maxHeap, (windowMap[s[right]], s[right]))
            else:
                # shrink the window
                while needToReplace > k:
                    if s[left] == majorityChar:
                        # majority needs to be updated
                        count, _ = heapq.heappop_max(maxHeap)
                        # heapq.heappush_max(maxHeap, (count-1, s[left]))
                    windowMap[s[left]]-=1
                    if windowMap[s[left]] == 0:
                        del windowMap[s[left]]
                    
                    majorityCount, majorityChar = maxHeap[0]
                    left+=1
                    string = s[left:right+1]
                    needToReplace = right-left+1 - majorityCount
                # at this point, the sequence is valid again
                # maxLen = max(maxLen, right-left+1)
            majorityCount, majorityChar = maxHeap[0]
            needToReplace = right-left+1 - majorityCount
            string = s[left:right+1]
            if needToReplace <= k:
                maxLen = max(maxLen, right-left+1)
                right+=1
            
        return maxLen
    