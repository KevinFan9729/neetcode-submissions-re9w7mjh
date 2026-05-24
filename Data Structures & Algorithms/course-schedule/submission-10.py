class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # we have a directed graph here
        # [0,1] ->[to, from]
        # we cannot have cycle
        # if we have cycle this means contradiction, and we cannot finish
        # we can finish when say we can treverse all couses without cycle
        # think like this
            # if a course have zero prerequisites, it can be taken right away
            # if a course has prerequisites; prerequisites needs to be taken
            # if we take all prerequisites, and the course has no more dependenices, course is safe
            # if at the end we cannot take some of the courses that means there are cycle
            # when we finish a course, we remove its dependency effect from other courses.
        # Time O(v+e)
        # space O(v+e)

        
        prerequisiteMap = {}
        courseCount = {} # number of prerequisites for each course
        for course in range(numCourses):
            courseCount[course] = 0
        for course, preq in prerequisites:
            if preq not in prerequisiteMap:
                prerequisiteMap[preq] = []
            prerequisiteMap[preq].append(course)
            courseCount[course] += 1 # compute how many prerequisies each course needs 

        finish = 0
        q = deque()
        for course in range(numCourses):
            if courseCount[course] == 0:
                # courses with no prerequisites can be taken
                q.append(course)

        while q:
            courseToTake = q.popleft()
            finish+=1
            # if courseToTake is prerequisites of any courses;
            # remove courseToTake
            for course in prerequisiteMap.get(courseToTake, []):
                # we now have courses depending on courseToTake
                if courseCount[course] > 0:
                    courseCount[course]-=1 # remove course dependency on courseToTake
                    if courseCount[course] == 0:
                        # course now has zero dependency 
                        q.append(course)
        if finish == numCourses:
            return True
        return False 
            