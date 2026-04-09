class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # we need to detect if there is a cycle in the directed graph or not
            # if we detect a cycle we can stop immediately and return []
            # if we don't detect a cycle, we add it to a path array 
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for pair in prerequisites:
            adj[pair[0]].append(pair[1]) # course, preq
        
        cycleSet = set()
        visited = set()
        path = []
        print(adj)
        def dfs(node):
            # if node in cycleSet:
            #     return False
            if node in visited: # if a course is visited (taken) return instantly, no need to check
                return True
            visited.add(node)
            cycleSet.add(node)
            for nei in adj[node]:
                if nei in cycleSet:
                    return False
                if dfs(nei) == False:
                    return False
            cycleSet.remove(node)
            path.append(node) # no preq, we can take the course
            return True
        
        for i in range(numCourses): # loop through all courses
            if dfs(i) == False:
                return []
        return path