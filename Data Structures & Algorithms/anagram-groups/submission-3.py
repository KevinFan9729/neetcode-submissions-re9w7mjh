class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use a hashmap
            # key is the sorted(string)
            # value is a list of strings
        # Time O(n) as str[i] size is constrained so sort can be O(100) which is O(1)
        # Space O(n) due to the extra hashmap 

        anagram_map = defaultdict(list)

        for item in strs:
            key = sorted(item)
            anagram_map[tuple(key)].append(item)
        res = []
        for val in anagram_map.values():
            res.append(val)
        
        return res