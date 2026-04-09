class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # this question is actually asking
        # given an undirected graph
        # is it:
            # fully connected
            # has no cycle
        # if both conditions are true, then the tree is valid
        # fasle otherwise

        # O(V+E) in time
        # O(V+E) in space

        # step1, construct the undirect graph first
        adj = {}
        for i in range(n):
            adj[i]= []
        for pair in edges:
            adj[pair[0]].append(pair[1])
            adj[pair[1]].append(pair[0])
        visited = set()
        # step2, define the dfs function to detect cycle
        def dfs(node, parent):
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    if dfs(nei, node):
                        return True
                elif nei != parent:
                    return True # as cycle
            return False # no cycle

        hasCycle = dfs(0,-1)
        if hasCycle:
            return False # has cycle
        if len(visited) != n:
            return False # not fully connected
        return True