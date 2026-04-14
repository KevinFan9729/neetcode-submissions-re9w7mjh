class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # prefix[j+1] - prefix[i] = sub sum between i and j
        # binary search
        prefix = [0]
        runningSum = 0
        for num in nums:
            runningSum += num
            prefix.append(runningSum)

        minLen = float("inf")
        n = len(nums)

        for i in range(n):
            left, right = i + 1, n
            ans = -1

            while left <= right:
                mid = left + (right - left) // 2
                subSum = prefix[mid] - prefix[i]

                if subSum >= target:
                    ans = mid
                    right = mid - 1
                else:
                    left = mid + 1

            if ans != -1:
                minLen = min(minLen, ans - i)

        return minLen if minLen != float("inf") else 0