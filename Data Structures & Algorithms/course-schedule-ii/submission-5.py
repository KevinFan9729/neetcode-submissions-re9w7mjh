class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # this is a directed graph
        # needs to figure about dependency
        # think like this
            # for all courses without prerequisites they can be taken\
            # once those courses are taken, any courses depending on those courses can remove those dependenices
            # we can repeat this process until we completed all courses
            # if we cannot complete all courses then, it is impossible to take all coures
        # Time O(V+E)
        # Space O(V+E)
        prerequisiteMap = {}
        courseCount= {}
        for course in range(numCourses):
            courseCount[course] = 0
        for course, preq in prerequisites:
            if preq not in prerequisiteMap:
                prerequisiteMap[preq] = []
            prerequisiteMap[preq].append(course)
            courseCount[course] +=1 # on this course, we count up one needed prerequisite
        
        q = deque()
        for course in courseCount.keys():
            # these courses have no dependency
            if courseCount[course] == 0:
                q.append(course)
        res = []
        while q:
            courseToTake = q.popleft()
            # we are taking courseToTake
            res.append(courseToTake)
            for course in prerequisiteMap.get(courseToTake, []):
                # now we have courses depending on courseToTake
                # we can remove courseToTake in those courses' prerequisites
                if courseCount[course] > 0:
                    courseCount[course] -= 1 # remove one dependency
                    if courseCount[course] == 0:
                        # this course also have zero preq now
                        q.append(course)

        if len(res) == numCourses:
            return res
        return []