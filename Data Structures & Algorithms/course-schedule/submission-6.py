class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # find if there is a cycle in a directed graph
        # O(V+E) in time 
        # O(V+E) in space
        if not prerequisites:
            return True
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for pair in prerequisites:
            adj[pair[0]].append(pair[1])
        print(adj)
        visited = set() # global visit set to see which course we can take
        def dfs(node):
            # If node has been visited, we don't need to check it for cycles again
            # because that node is fully processed and safe. 
            if node in cycleSet:
                return False
            if node in visited:
                return True
            visited.add(node)
            cycleSet.add(node)
            for nei in adj[node]:
                if dfs(nei) == False: # if one false is detected, return False instantly
                    return False

            cycleSet.remove(node) # backtrack
            return True
        # courses are labeled from 0 to numCourses -1
        for i in range(numCourses):
            cycleSet = set() # cycle detection set that needs to be reset for each new start
            if dfs(i) == False:
                return False
        return True