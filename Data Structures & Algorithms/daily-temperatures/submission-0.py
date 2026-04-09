class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)
        stack.append((temperatures[0], 0))
        for i in range(1, len(temperatures)):
            top = stack[-1]
            while top and temperatures[i] > top[0]:
                output[top[1]] = i - top[1]
                stack.pop()
                if stack:
                    top = stack[-1]
                else: 
                    top = None
            stack.append((temperatures[i], i)) # (temperature, its index)
        return output