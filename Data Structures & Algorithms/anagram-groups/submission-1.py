class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # m*O(n) where m is the length of token, and n is how many tokens we have in the input 
        # same logic as the sorting method, but here we use the one-hot
        # encoding to represent the sequence instead of actually sorting
        # the string
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        print(ans)
        return ans.values()
