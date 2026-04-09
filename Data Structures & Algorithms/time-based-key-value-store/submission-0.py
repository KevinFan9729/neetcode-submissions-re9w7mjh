class TimeMap:

    def __init__(self):
        self._map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Time O(1)
        # Space O(n) due to the hashmap
        self._map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # Time O( O(logn))
        # O(1)
        if key in self._map:
            idx = self._binary_search_nearest(self._map[key], timestamp)
            if idx > -1:
                return self._map[key][idx][1]
        return ""

    def _binary_search_nearest(self, arr, target):
        left, right = 0, len(arr)-1
        while left <= right:
            mid = left + (right-left)//2
            if arr[mid][0] == target:
                return mid
            elif arr[mid][0] < target:
                left = mid +1
            else:
                right = mid - 1
        # if we are here, we did not find the exact recent item
        # check if the most recent item (next_best) satisfy the condition (next_best < target)

        # we are here iff right < left
        next_best = arr[right][0]
        if next_best < target:
            return right
        return -1
            