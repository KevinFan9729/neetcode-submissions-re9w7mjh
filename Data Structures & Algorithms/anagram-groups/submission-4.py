class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # I can use a hashmap to store the result
        # I can sort the string and use that as the key
        # and the value of the hashmap is the original string
        # Time O(n*mlogm)
        # Space O(n * m)
        res = {}
        for item in strs:
            key = tuple(sorted(item))
            if key not in res:
                res[key] = []
            res[key].append(item)
        return list(res.values())