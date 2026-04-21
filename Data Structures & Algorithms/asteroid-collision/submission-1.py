class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # feel like this is a simulation problem
        # we can use a stack?
        # we push the item in the stack
            # check the top and the current
        # Time O(n)
        # Space O(n)
        stack = [0] # pad a zero weight asteroid
        for item in asteroids:
            itemSurvived = False # this flag will take account say the asteroid survived and no more collisions 
            top = stack[-1]
            # willCollide
                # top moves toward right, item moves towards left
            willCollide = top >0 and item <0
            if not willCollide: #  if not colliding
                stack.append(item)
            else:
                while willCollide:
                    if abs(top) == abs(item):
                        itemSurvived = False # item did not survive
                        stack.pop()
                        break #  chain reaction not possible
                    elif abs(top) < abs(item):
                        stack.pop() #  old top is destoryed
                        top = stack[-1]
                        itemSurvived = True
                        if top == 0: # run out of 
                            itemSurvived = False # already added 
                            stack.append(item)
                            break
                    else: # the else case is top is bigger, item is destroyed and top remains
                        itemSurvived = False # item did not survive 
                        break
                    willCollide = top >0 and item <0
                if itemSurvived:
                    stack.append(item)

        return stack[1:]