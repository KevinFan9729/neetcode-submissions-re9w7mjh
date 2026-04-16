class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # I am thinking I can compute the distance linearly respect to x, 
        # while I am computing that distance, I keep track of the minimum distance's index, 
        # once I am done, I can use that index as the starting points, and use two pointer to compare distance, 
        # whichever pointer give me the smallest distance, I add that number to result, just need to worry about  
        # |a - x| == |b - x| and boundary.
        # Time O(n)
        # Space O(n)
        dist = []
        minDist = float('inf')
        minIndex = 0
        for i in range(len(arr)):
            d = abs(arr[i] - x)
            dist.append(d)
            if minDist > d:
                minIndex = i
                minDist = d
        # [4,2,1,2]
        res = deque()
        res.append(arr[minIndex])
        left, right =  minIndex-1, minIndex+1
        while len(res) < k:
            if left <0:
                for i in range(right, len(arr)):
                    res.append(arr[i])
                    if len(res) == k:
                        return list(res)
            elif right>len(arr)-1:
                for i in range(left, -1, -1):
                    res.appendleft(arr[i])
                    if len(res) == k:
                        return list(res)
            else:
                if dist[left] < dist[right]:
                    res.appendleft(arr[left])
                    left -= 1
                elif dist[left] > dist[right]:
                    res.append(arr[right])
                    right += 1
                else:
                    res.appendleft(arr[left])
                    left -= 1
        
        return list(res)
