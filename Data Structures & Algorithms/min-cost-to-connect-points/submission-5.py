class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(pt1, pt2):
            x1,y1 = pt1
            x2,y2 = pt2
            return abs(x1-x2) + abs(y1-y2)
        
        # all points must be connected
        # there must be no cycle
        # each point is a node
        # edge cos the the manhattan distance
        # For every unconnected point, what is the cheapest cost currently known to connect it to any point already in the tree?

        # a set of connected points, an array of cheapest known connection costs, and a running total
        # minCost[i] = cheapest known way to connect point i to the current tree
        # Time: O(n²)
        # Space: O(n)
        connected = [points[0]]
        minCost = [float('inf')] * len(points)
        for i in range(1,len(minCost)):
            minCost[i] = distance(points[0], points[i])
        print(minCost)
            
        totalCost = 0
        while len(connected) != len(points):
            cost = min(minCost)
            # find the unconnected point with the lowest cost
            pointToConnectIdx = minCost.index(cost)
            pointToConnect = points[pointToConnectIdx]
            # add the cost
            totalCost += cost
            # mark the point connected
            connected.append(pointToConnect)
            minCost[pointToConnectIdx] = float('inf')
            # update the cost array
            for i in range(len(points)):
                if minCost[i] == float('inf'):
                    # skip connected points
                    continue
                minCost[i] = min(minCost[i],distance(pointToConnect, points[i]))

        return totalCost