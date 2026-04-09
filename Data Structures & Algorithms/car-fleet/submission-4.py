class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # we can compute the time to reach (ttr)
        # (target - current pos) / speed = ttr
        # one thing is becaue the this is only one line
        # fast car that are behind cannot go over the slow car ahead
        # we will have this tuple for each car (pos, ttr)
        # we will sort based on the pos in descending order 
        # Time O(nlogn) due to sorting
        # Space O(n) due to the array
        car_items = []
        for car_idx in range(len(position)):
            ttr = (target - position[car_idx])/speed[car_idx]
            car_items.append((position[car_idx], ttr))
        car_items.sort(reverse=True) # sort based on pos

        fleet_count = 1 # a car by itself is a fleet
        max_time_to_reach = car_items[0][1] # initialize to the ttr of the car closest to the target
        for car_idx in range(1, len(car_items)):
            if max_time_to_reach < car_items[car_idx][1]:
                # behind car is slower than the ahead car
                # never catch up, a NEW fleet is formed
                fleet_count+=1
                max_time_to_reach = car_items[car_idx][1]

        return fleet_count