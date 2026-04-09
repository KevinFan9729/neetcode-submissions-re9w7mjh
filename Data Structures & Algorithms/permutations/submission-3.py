class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # O(n*n!) 
        res = []
        pers = []
        freqMap = defaultdict(int)
        for num in nums:
            freqMap[num] += 1
        def dfs(): 
            if len(pers) == len(nums):
                res.append(pers.copy()) 
                return

            for num in freqMap.keys():
                if freqMap[num] >0:
                    freqMap[num]-=1
                    pers.append(num)
                    dfs()
                    pers.pop() # backtrack
                    freqMap[num]+=1 # backtrack
    
        dfs()  

        return res 