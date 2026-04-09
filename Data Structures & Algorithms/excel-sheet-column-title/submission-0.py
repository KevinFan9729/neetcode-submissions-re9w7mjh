class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # modulo 26?
        # Time O(n)
        # Space O(1)
        res = []
        while columnNumber > 0:
            columnNumber -= 1
            rem = int(columnNumber %26)
            res.append(chr(65+rem))
            columnNumber //= 26

        return "".join(res[::-1])