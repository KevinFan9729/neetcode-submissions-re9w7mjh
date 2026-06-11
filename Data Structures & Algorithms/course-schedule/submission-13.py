class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # we have a directed graph here
        # [0,1] ->[to, from]
        # we cannot have cycle
        # if we have cycle this means contradiction, and we cannot finish
        # we can finish when say we can treverse all couses without cycle
        # Time O(V+E)
        # Space O(V+E)
        adj = {}
        # construct the graph
        for to, f in prerequisites:
            if f not in adj:
                adj[f] = []
            adj[f].append(to)
        taken = set() # used for checking courses taken
        def dfs(course):
            if course in taken: # the course has already be verified to be safe and taken, return True
                return True
            if course in visiting:
                return False
            visiting.add(course)
            for nei in adj.get(course,[]):
                if not dfs(nei):
                    # if there is a cycle return
                    # otherwise keep exploring
                    return False
            visiting.remove(course)# after we are done with this path, backtrack
            taken.add(course) # course is fully explored and safe (no cycle)
            return True
        
        visiting = set()

        for i in range(numCourses):
            res = dfs(i)
            if not res:# there is a cycle
                return False
            else:
                if len(taken) == numCourses:
                    # we have finished all courses
                    return True
        return False