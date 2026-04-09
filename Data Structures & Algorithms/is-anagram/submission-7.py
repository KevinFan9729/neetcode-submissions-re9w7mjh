class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # order does not matter
        # we can sort and compare or use a hash map
        # the hash map way we will need two passes
        # lets do the sort way
        # Time O(nlogn)
        # Space O(n) sort plus creating new string
        return "".join(sorted(s)) == "".join(sorted(t))
        