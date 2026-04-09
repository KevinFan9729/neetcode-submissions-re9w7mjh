class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # O(V + E)
        # hash map to store our course index as the key and the course prerequisite as 
        # the values?
        course_map = {}
        for course_index in range(numCourses):
            course_map[course_index] = []
        for pair in prerequisites:
            course_map[pair[0]].append(pair[1])
        print(course_map)
        # directional graph, cannot have self loop
        self_loop = False
        def dfs(course_index):
            nonlocal self_loop
            if course_index in visited:
                self_loop = True
                return 
            visited.add(course_index)
            for nei in course_map[course_index]:
                dfs(nei) # naviagte to neighbors
            visited.remove(course_index) # back track
            # improves performance by reducing redundant work. Once a course has been fully explored, 
            # and it's determined that it can be completed without forming a cycle, 
            # its prerequisites are cleared. This prevents the DFS from re-exploring the 
            #same nodes multiple times, especially in large and complex graphs.
            course_map[course_index] = [] # important remove all prerequisites for the current course to remove redundant work
            return
        for node in course_map.keys():
            visited = set()
            dfs(node)
            if self_loop:
                return False
        return True