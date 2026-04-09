class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # O(n^2) in time
        # O(n) in space
        def move(curr_index, curr_gas, visited_stations): #O(n)
            # If we've returned to the starting station and have visited all stations
            if visited_stations == len(gas):
                return curr_index
            
            # If we run out of gas before completing the loop
            if curr_gas <= 0:
                return -1
            
            # Calculate the next station index and gas after moving
            new_index = (curr_index + 1) % len(gas)
            new_gas = curr_gas - cost[curr_index]
            if new_gas < 0: # you cannot reach the next station!
                return -1
            new_gas += gas[new_index] # refuel at the new station

            # Recursively check the next station
            return move(new_index, new_gas, visited_stations + 1)
        
        # Try starting from each station
        for start in range(len(gas)): #O(n)
            result = move(start, gas[start], 0)
            if result != -1:
                return result

        return -1