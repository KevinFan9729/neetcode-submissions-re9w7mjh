class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # can we solve it recursively?
        # function takes two arguments index1 and index2
        # if we don't have a mistmatch
            # we will increment index1 and index2 without incrementing count
        # if we find a mismatch character we will do:
            # three operations
                # delete: increment index1, index2 stays the same
                # insert: index1 stays the same, increment index2
                # replace: increment index1 and index2
        # base case
            # if index1 >=len(word1) and index2 < len(word2) word1 run out of characters, but word 2 still has chracters
                # return len(word2) - index2 characters need to be inserted to word1 to make w1 and w2 equal
            # if index2 >=len(word2) and index1 < len(word1) word2 run out of characters, but word 1 still has chracters
                # return len(word1) - index1 characters need to be deleted from word1 to make w1 and w2 equal
            # if index1 >=len(word1) and index1 >= len(word1) both word runs out of characrers, both strings are the same
                # return 0
        
        # O(m*n) in time
        # O(m*n) in space, unique states are bounded by index1 and index2
        
        memo = {}
        def minCount(index1, index2):
            if ((index1, index2)) in memo:
                return memo[(index1, index2)]
            if index1 >=len(word1) and index2 < len(word2):
                return len(word2) - index2
            if index2 >=len(word2) and index1 < len(word1):
                return len(word1) - index1
            if index1 >=len(word1) and index1 >= len(word1):
                return 0
            if word1[index1] == word2[index2]:
                return minCount(index1+1, index2+1)
            
            deleteCount = minCount(index1+1, index2) +1
            insertCount = minCount(index1, index2+1) +1
            replaceCount = minCount(index1+1, index2+1) +1
            minMove = min(deleteCount, insertCount, replaceCount)
            memo[(index1, index2)] = minMove
            return minMove
        ans = minCount(0,0)
        return ans

        
            