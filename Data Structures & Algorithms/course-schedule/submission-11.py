class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # if a course has no preq, then this course can be taken safely
        # we will construct a hashmap where we store how many preq each course needs
        # and we will have a hashmap that store preq: [a list of courses that take this as preq]
        # we start with all courses that have no preq,
        # and remove that course from all courses' preq list
        # Time O(V+E) # at worst we need to trverse the entire graph
        # Space O(V+E)
        preqMap = {}
        coursePreqCount = {}
        for c in range(numCourses):
            coursePreqCount[c] = 0
        for course, preq in prerequisites:
            if preq not in preqMap:
                preqMap[preq] = []
            preqMap[preq].append(course)
            coursePreqCount[course] += 1 # add one preq count
        q = deque()
        for c in coursePreqCount:
            # collect courses that have no preq
            if coursePreqCount[c] == 0:
                q.append(c)
        
        courseTaken = 0
        while q:
            courseToTake = q.popleft()
            courseTaken+=1
            for c in preqMap.get(courseToTake, []):
                # courses here depends on courseToTake
                # remove courseToTake as a dependency
                if coursePreqCount[c] > 0:
                    coursePreqCount[c] -=1
                    if coursePreqCount[c] == 0:
                        # we have a new course that becomes preq free
                        q.append(c)
        if courseTaken == numCourses:
            return True
        return False
