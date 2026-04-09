class Solution:
    def isValid(self, s: str) -> bool:
        # ah this is a stack problem
        # the idea is that we push open brackets into the stack
        # when facing a close barket, check the top, if match pop, if not return False
        # one thing to be aware of is we have a close barket at the beginning
            # in this case, we just return false as this can never be valid
            # why do we need to check this case? Becuase we push open brackets only; having a closing bracket at the beginning casue index issues
            # this check needs to be applied throughout 
        # Time O(n)
        # Space O(n) due to the stack

        # fixed size hashmap used as a lookup tabel for clarity
        # key is close br and value is open br
        br_map = {")":"(", "]":"[", "}":"{"}

        check_stack = []
        for br in s:
            if br in br_map.values(): # barket is openning
                check_stack.append(br)
            elif br in br_map.keys(): # barket is closing
                if len(check_stack) > 0:
                    if check_stack[-1] != br_map[br]:
                        return False
                    else:
                        check_stack.pop()
                else:
                    # if we are here it means we have have a closing barket,
                    # but we have no matching openning barket as the stack is empty
                    return False
        
        return len(check_stack) == 0