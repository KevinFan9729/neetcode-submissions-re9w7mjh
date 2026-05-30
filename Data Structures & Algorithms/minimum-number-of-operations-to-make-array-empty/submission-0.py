class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # hmmm should I construct an occurance map
        # each time I can delete 2 elements or 3 elements
        # lets use a recursion method?
        # each step, for each num, we can remove 2 duplicates or 1 duplciate
        # actually for each number, we need to figure out what is the min steps to reduce it to zero
        # define a recursive function findMin(count) count is the current occurance of this target number
        # this function return the min number of operations to reduce this number's occurance to 0
        # Time O(m+n) number of unique state is bounded by count which is the max of occurance, say m; and each state is computed once
        # Space O(m+n)
        occurrenceMap = {}
        memo = {}
        for num in nums: 
            if num not in occurrenceMap: 
                occurrenceMap[num] = 0 
            occurrenceMap[num] +=1
        
        def findMin(count):
            if count < 0:
                # invalid
                return float('inf')
            if count == 0:
                # valid
                return 0
            if count in memo:
                return memo[count]
            
            remove2 = 1 + findMin(count-2)
            remove3 = 1 + findMin(count-3)

            minVal = min(remove2, remove3)
            memo[count] = minVal
            return minVal
        total = 0
        for _, count in occurrenceMap.items():
            operations = findMin(count)
            if operations == float("inf"):
                return -1
            total+=operations
        return total