class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # ok the array is sorted
        # we compute the distance to x linearly?
        # smaller the dist the better
        # [2,4,5,8] x=6
        # [4,2,1,2]
        # use a min heap?
        # (dist, num) as element?
        # the return must be ordered, that is tricky
        # Time O(n +klogn)
        # Space O(n)
        dist_num_pairs = []
        for num in arr:
            dist_num_pairs.append((abs(num-x), num))
        import heapq

        heapq.heapify(dist_num_pairs)# O(n) in time
        res = []
        while k: # <- TIme O(klogn)
            target = heapq.heappop(dist_num_pairs)
            res.append(target[1])
            k-=1
        return sorted(res) # <- time O(klogk)
