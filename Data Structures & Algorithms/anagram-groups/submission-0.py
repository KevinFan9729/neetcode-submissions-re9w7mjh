from collections import defaultdict
class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # n* mlog(m) m is the length of tokens, n is number of tokens
        # characters of anagrams are the same if they are sorted,
        # keys sorted characters of the string, value: list of anagrams
        str_map = defaultdict(list)

        for token in strs:
            sorted_token = ''.join(sorted(token))
            # here the hash map will take care of the grouping
            # as tokens with the same character sequence will be bounded
            # with the same key
            str_map[sorted_token].append(token)        
        res = []

        for val in str_map.values():
            res.append(val)
        return res

        