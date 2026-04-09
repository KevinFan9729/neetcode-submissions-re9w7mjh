from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # if two strings are anagram, they have the same set of characters, and the same frequency for each char
        # we can compute the count_ls (hash array of character frequency) then we use this as the key (convert to tuple as key, lists are not hashable) of a hashmap
        # the hashmap key is tuple(count_ls), the value is a list of all substring that has the same key
        # lists are not hashabe as they are mutable
        # Time O(n*m), n is the length of the list, and m is the length of the substring
        # Space O(n)

        def count_freq(s):
            # we only have lower case engish characters
            # we can use a hash array to count occurance
            # Time O(m) say m is the length of the string, we need to loop through all char in the string
            # Space is O(1), fixed 26 characters
            count_ls = [0]*26
            for char in s:
                count_ls[ord(char) - ord("a")] +=1
            return tuple(count_ls)
        group_map = defaultdict(list)
        for s in strs:
            key = count_freq(s)
            group_map[key].append(s)
        res = []
        for value in group_map.values():
            res.append(value)
        return res
