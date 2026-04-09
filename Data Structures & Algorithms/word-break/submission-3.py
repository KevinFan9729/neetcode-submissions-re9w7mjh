class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def canBreak(s: str) -> bool:
            # Base case: If the string is empty, we've successfully segmented it
            if not s:
                return True
            if s in memo:
                return memo[s]
            
            # Try each word in the dictionary
            for word in wordDict:
                # If the string starts with the word
                if s.startswith(word):
                    # Recursively check the remaining string
                    if canBreak(s[len(word):]):
                        memo[s] = True
                        return True
            
            # If no word fits, return False
            memo[s] = False
            return False
        
        # Start the recursive check
        return canBreak(s)