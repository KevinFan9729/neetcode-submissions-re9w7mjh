from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        # Using a mapping for the opening and closing parentheses
        pair = {')': '(', '}': '{', ']': '['}
        stack = deque()
        
        for char in s:
            if char in pair.values():  # Check if it's an opening bracket
                stack.append(char)
            elif char in pair.keys():  # Check if it's a closing bracket
                if stack and stack[-1] == pair[char]:  # Match found
                    stack.pop()
                else:
                    return False
        return not stack  # True if stack is empty (all matched), False otherwise
