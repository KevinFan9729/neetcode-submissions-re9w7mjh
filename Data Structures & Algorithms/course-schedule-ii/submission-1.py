class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # O(V + E)
        # hash map to store our course index as the key and the course prerequisite as 
        # the values?
        # toplogical sort
        course_map = {}
        for course_index in range(numCourses):
            course_map[course_index] = []
        for pair in prerequisites:
            course_map[pair[0]].append(pair[1])
        print(course_map)
        # directional graph, cannot have self loop

        cycle_set, visited_set = set(), set()
        res = []

        def dfs(course_index):
            if course_index in cycle_set:
                return False
            if course_index in visited_set: # don't need to continue, course is already visited and added to the res
                return True
            cycle_set.add(course_index)
            for nei in course_map[course_index]:
                if dfs(nei) == False:
                    return False # cycle detected, return immediately!
            cycle_set.remove(course_index) # back track
            visited_set.add(course_index)
            res.append(course_index)
            return True
        for course_index in course_map.keys():
            if dfs(course_index) == False:
                return []
        return res



