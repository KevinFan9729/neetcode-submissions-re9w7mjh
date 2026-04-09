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
        # step2, define the bfs function to detect cycle
        def bfs(node):
            q = deque()
            q.append((node, -1)) # node, parent
            visited.add(node)
            while q:
                qLen = len(q)
                for i in range(qLen):
                    node, parent = q.popleft()
                    for nei in adj[node]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append((nei,node))
                        elif nei != parent: # the node is visisted and it is not the parent node
                            return True # has cycle
            return False # no cycle

        hasCycle = bfs(0)
        if hasCycle:
            return False # has cycle
        if len(visited) != n:
            return False # not fully connected
        return True