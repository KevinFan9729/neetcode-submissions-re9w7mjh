class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # collsion can happen if
            # left is positive, and right is negative
        # if two rocks have the same sign, no collison
        # ir two right opposite direction, no collison (right rock (neg) goes left, left rock (pos) goes right)
        # if two rocks colliade, we need to make sure to handle chain collison
        # use a stack
        # Time O(n)
        # Space O(n)

        stack = []

        def willHit(rock1, rock2):
            if rock1 > 0 and rock2 <0:
                return True
            return False

        for rock in asteroids:
            if not stack:
                stack.append(rock)
                continue
            leftRock = stack[-1]
            rightRock = rock
            if not willHit(leftRock, rightRock):
                stack.append(rightRock)
                continue
            else:
                # collison
                if abs(leftRock) == abs(rightRock):
                    # pop the left rock
                    # no chain collison
                    stack.pop()
                elif abs(leftRock) > abs(rightRock):
                    # left rock stays
                    # right rock is gone
                    # no chain collison
                    continue
                else:
                    # left rock is gone
                    # need to check chain collison
                    stack.pop()
                    alive = True
                    while stack and willHit(stack[-1], rightRock) and alive:
                        if abs(rightRock) > abs(stack[-1]):
                            # chain collison
                            stack.pop()
                        elif abs(rightRock) == abs(stack[-1]):
                            alive = False
                            stack.pop()
                        else:
                            alive = False
                    if alive:
                        stack.append(rightRock)
        return stack