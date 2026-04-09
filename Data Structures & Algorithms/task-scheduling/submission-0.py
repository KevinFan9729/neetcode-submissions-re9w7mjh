class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # O(n)
        q = deque()
        taskHeap = []
        occurance = {}
        for task in tasks:
            if task not in occurance:
                occurance[task] = 0
            occurance[task] += 1
        for value in occurance.values():
            taskHeap.append(value*-1)
        
        heapq.heapify(taskHeap) # turn into a max heap
        time = 0
        while taskHeap or q: # this is bounded by O(26) we have 26 distinct characters
            if taskHeap:
                exec_task_freq = heapq.heappop(taskHeap)
                time += 1 # simulate that the task is executed
                idle_time = time + n # the time where this task needs to wait until the next execution
                exec_task_freq += 1 # negative to resemeble a max heap so we add 1 to 'decrement' to 0
                if exec_task_freq != 0:
                    q.append((exec_task_freq, idle_time))
            else:
                time += 1 # simulate that the cpu is idle
            if q and q[0][1] == time:
                freq, _ = q.popleft()
                heapq.heappush(taskHeap, freq)
            
        return time