class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # we can do a nested loop to find the common prefix
        # for the nested loop solution, 
        # you just loop for the character of all string, 
        # if they all agree, then you add it to the result. 
        #  the time complexity of this will be O(n*m) 
        #  where n is number of stirng, m is 
        #  the length of the smallest string in the array. 
        #  I am wondering if there is a better way though
        # Time O(n*m)
        # Space O(m) where m is the length of the logest common prefix

        res = []
        count = defaultdict(int)
        idx = 0
        num_of_strs = len(strs)
        break_flag = False

        while True:
            for item_str in strs:
                if idx >= len(item_str):
                    return "".join(res) if res else ""
                candidate = item_str[idx]
                count[candidate] +=1
            if count[candidate] == num_of_strs:
                res.append(candidate)
            else:
                return "".join(res) if res else ""
            idx += 1
            del count[candidate]
        return "".join(res) if res else ""


                
                
