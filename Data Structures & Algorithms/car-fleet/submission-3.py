import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # we can sort the all cars based on their starting pos first
            # this is important, as a fast car can be blocked by a slow car 
            # if a fast car that is behind the slow car catch up to the slow car
                # the fast car and the slow car becomes a fleet
                # and this fleet will travel at the same speed as the slow car
            # we can compute for each car, how much time it needs to reach the target
            # if a car that is behind needs a smaller required time to reach the target
            # than a car that is ahead of it
                #then those two car will form a car fleet

            # if the car behind and the car ahead both need the same time to reach the target
                # they will form a car fleet
            
            # if the car behind needs more time than the car ahead, then the slow car will never
            # catch up to the faster car
                # they will NOT form a car fleet

            # we say initally we have n car fleets (indiviual cars as their own fleet)
            # we will loop through all cars linearly to see if we can decrement the car fleet counts
                # we can decrement the car fleet count because cars can join and become a single feet
        # O(n) in time 
        # O(n) in space due to the array
        cars = []
        carNum = len(position)
        for i in range(carNum):
            initialPos = position[i]
            carSpeed = speed[i]
            timeReachTarget = ((target - initialPos)/float(carSpeed))
            target - position[i]
            cars.append([initialPos, timeReachTarget])
        cars.sort(key= lambda pair: pair[0], reverse = True)

        fleetCount = carNum

        for i in range(carNum-1):
            behindReachTime = cars[i+1][1]
            aheadReachTime = cars[i][1]

            if behindReachTime <= aheadReachTime:
                fleetCount -= 1 # they can join as a fleet
                cars[i+1][1] = aheadReachTime # set the behind car reach time to the slower ahead car's
        
        return fleetCount