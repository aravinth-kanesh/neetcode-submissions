class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # use a heap to decide which task to execute
        # execute the task that appears the most times
        # inherently a max heap problem

        # count the frequency of each task
        task_freq = Counter(tasks) # {"A": 3, "B": 4} for example

        # add all the tasks to the heap
        heap = [-freq for freq in task_freq.values()]
        heapq.heapify(heap)

        queue = deque() # monotonic - stores the timestamp of when the
        # task can be added back to the heap

        # global time
        time = 0

        # all tasks must be processed
        while heap or queue:
            time += 1 # increment time

            # check if tasks can be added back to the heap
            if queue and time == queue[0][0]:
                _, freq = queue.popleft()
                heapq.heappush(heap, -freq)

            # heap not empty
            if heap:
                freq = -heapq.heappop(heap)
                freq -= 1

                if freq > 0:
                    queue.append((time + n + 1, freq)) # time + n is
                    # when the task can be re-added to the heap

        return time