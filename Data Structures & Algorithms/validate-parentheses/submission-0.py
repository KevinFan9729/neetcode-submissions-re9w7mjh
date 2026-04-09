from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        # have a stack, push the stack if we have "[", "{", "(",
        # pop the stack if we see "]", "}" ,")" return false if
        # there is a mismatch parenthese pair, continue the check if there is not a mismatch
        # when the stack is empty and the str has no characters left, we return true
        stack = deque()
        for char in s:
            if char == "[" or char == "{" or char == "(":
                stack.append(char)
            if char == "]" or char == "}" or char == ")":
                if stack:
                    top_val = stack.pop()
                    if char == "]":
                        if top_val == "[":
                            continue
                        else:
                            return False
                    elif char == "}":
                        if top_val == "{":
                            continue
                        else:
                            return False
                    elif char == ")":
                        if top_val == "(":
                            continue
                        else:
                            return False
                else:
                    return False
        if stack: # if the stack has items, meaning there are mismatches
            return False
        return True


        