class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # since they all move in the same speed
        # if they all have the same sign no collision
        # they will only collade iff
            # signs are different 
            # they are heading towards each other pos, neg
        # maybe we need to consider two candidates at a time?
        # use a stack
        # Time O(n)
        # Space O(n)

        def _get_sign(num):
            if num>=0:
                return "pos"
            else:
                return "neg"
        res = []

        for item in asteroids:
            res.append(item)
            while len(res) >= 2: # while loop is needed for chained collisons
                # we have enough candidates to check for collisons
                candidate2 = res.pop()
                candidate1 = res.pop()
                candidate1_sign = _get_sign(candidate1)
                candidate2_sign = _get_sign(candidate2) 
                if candidate1_sign == "pos" and candidate2_sign == "neg":
                    if abs(candidate1) > abs(candidate2):
                        res.append(candidate1)
                    elif abs(candidate1) < abs(candidate2):
                        res.append(candidate2)
                    # the else is where they have the same weight
                    # this means they both get destroyed
                else:
                    # they will not collide
                    # either the same sign(direction)
                    # or moving away
                    res.append(candidate1)
                    res.append(candidate2)
                    break
        return res
            
    