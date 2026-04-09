class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # n =2
        #[()()] [(())] 
        # valid means, we have matching opening and close brackets
        # also, the order or open and close brackets are important
        # natrually I am thinking of stack
        # at every step, dependings what we have on the stack
        # we can either include an open b or a close b
            # if there is no matching open b, cannot add close b
        # feels like recursion can help us?
        # gen(open_n, close_n)
        # if stack is empty, and close_n ==0, that is a valid solution
        # if stack is not empty, and close_n == 0, not valid, return
        # Stack only will hold (
        # it is not really needed here, just need to track open and close
        # invalid if open_n > close_n, this means we have ) n=2 close_n is 1 open_n is 2 
        # Time Depends on how many vaild stack we can generate * time to construct the string
        # Time O(#valid results * n)
        # Space O(n)

        res = []
        curr = []
        def gen(open_n, close_n):
            if open_n == 0 and close_n == 0:
                res.append("".join(curr))
                return
            if open_n > close_n:
                return
            if open_n < 0 or close_n < 0:
                return
            
            # we can either add a close or open here
            # include open
            curr.append("(")
            gen(open_n-1, close_n)
            # backtrack
            curr.pop()
            # include close
            curr.append(")")
            gen(open_n, close_n-1)
            # backtrack
            curr.pop()
        
        gen(n,n)
        return res