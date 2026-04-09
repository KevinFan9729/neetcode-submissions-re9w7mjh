class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # find a dist array

        dist_sq_ls = []
        index_map = {}
        for i in range(len(points)):
            dist_sq = points[i][0]**2 + points[i][1]**2
            dist_sq_ls.append(dist_sq)
            if dist_sq not in index_map:
                index_map[dist_sq] = []
            index_map[dist_sq].append(i)
        dist_sq_ls.sort()
        res = []
        count = 0
        while count < k:
            closet_dist = dist_sq_ls[count]
            indexs = index_map[closet_dist]
            if len(indexs) == 1:
                index = indexs[0]
                res.append(points[index])
                count +=1
            else:
                for index in indexs:
                    res.append(points[index])
                    count +=1
        return res

        