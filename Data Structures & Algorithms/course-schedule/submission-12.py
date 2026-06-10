class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # we can take courses that have zero preq right away
        # the idea is we will take those courses
        # and remove coureses that depend on those coureses
        # if we can take all courses then we are good

        # we need a map which is preq : [list of courses depend on preq]
        # we need a another map which courses: number of preq
        # Time O(V+E)
        # Space O(V+E)
        preqMap = {}
        preqCount = {}
        for course in range(numCourses):
            preqCount[course] = 0
        
        for course, preq in prerequisites:
            if preq not in preqMap:
                preqMap[preq] = []
            preqMap[preq].append(course)
            preqCount[course] += 1 # add preq count

        q = deque()
        # now want to collect all courses without any preq
        for course in preqCount:
            if preqCount[course] == 0:
                q.append(course)
        
        courseTaken = 0
        while q:
            courseToTake = q.popleft()
            courseTaken+=1
            for course in preqMap.get(courseToTake, []):
                # all those courses that previously depends on courseToTake
                # can have its dependency count -=1
                preqCount[course] -= 1
                if preqCount[course] == 0:
                    # no more preq, this course can be taken
                    q.append(course)
        if courseTaken == numCourses:
            return True
        return False