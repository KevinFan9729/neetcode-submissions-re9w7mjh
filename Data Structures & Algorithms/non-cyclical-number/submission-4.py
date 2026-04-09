class Solution:
    def isHappy(self, n: int) -> bool:
        # two pointers?
        # two pointer can be used to detect cycle
            # fast and slow pointer
            # if fast meets slow this means there is a cycle
        # but, this is used for linked list
        # we do not have a linked list here
        # how to or can we still use this two pointer apporach?
        

        def splitAndSqSum(n):
            # %10 to get the last digit
            # //10 to get rid of a the last digit
            out = 0
            while n:
                lastDigit = n%10
                out += lastDigit ** 2
                n=n//10
            return out
        slow, fast = n, splitAndSqSum(n)
        while slow != 1 and fast!= 1: # if either is 1, return true
            # analogous to fast.next.next
            fast = splitAndSqSum(fast)
            fast = splitAndSqSum(fast)
            # analogous to slow.next
            slow = splitAndSqSum(slow)
            print(f"fast:{fast} slow:{slow}")
            if slow == fast:
                return False
        return True