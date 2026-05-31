class Solution:
    def simplifyPath(self, path: str) -> str:
        # I am thinking of a stack?

        # Time O(n)
        # Space O(n)
        stack = []
        candidates = path.split('/')
        cleaned = []
        for element in candidates:
            if element != '':
                cleaned.append(element)
        print(cleaned)
        stack.append('/')
        for item in cleaned:
            if item == '..':
                stack.pop() # pop /
                if not stack:
                    stack.append('/')
                    continue
                stack.pop() # pop previous element
            elif item == '.':
                continue
            else:
                stack.append(item)
                stack.append('/')
            
        if len(stack) >1:
            if stack[-1] == '/':
                stack.pop()

        return "".join(stack)

                        