# 621. Task Scheduler

# Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

# However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

# Return the least number of units of times that the CPU will take to finish all the given tasks.

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]

        heapq.heapify(maxHeap)

        time = 0
        q = deque()

        while q or maxHeap:
            time += 1   
        
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt:
                    q.append([cnt, time + n])

            if q and time == q[0][1]:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time