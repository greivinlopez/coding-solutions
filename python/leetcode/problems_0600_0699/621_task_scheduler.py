# ----------------------
# 621. Task Scheduler 🕗
# ----------------------

# Problem: https://leetcode.com/problems/task-scheduler/
# 
# You are given an array of CPU tasks, each labeled with a letter from A to Z, 
# and a number n. Each CPU interval can be idle or allow the completion of one 
# task. Tasks can be completed in any order, but there's a constraint: there 
# has to be a gap of at least n intervals between two tasks with the same label.
# 
# Return the minimum number of CPU intervals required to complete all tasks.
# 
#  
# Example 1:
# 
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# 
# Output: 8
# 
# Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
# 
# After completing task A, you must wait two intervals before doing A again. 
# The same applies to task B. In the 3rd interval, neither A nor B can be done, 
# so you idle. By the 4th interval, you can do A again as 2 intervals have 
# passed.
# 
# 
# Example 2:
# 
# Input: tasks = ["A","C","A","B","D","B"], n = 1
# 
# Output: 6
# 
# Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
# 
# With a cooling interval of 1, you can repeat a task after just one other task.
# 
# 
# Example 3:
# 
# Input: tasks = ["A","A","A", "B","B","B"], n = 3
# 
# Output: 10
# 
# Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.
# 
# There are only two types of tasks, A and B, which need to be separated by 3 
# intervals. This leads to idling twice between repetitions of these tasks.
# 
#  
# Constraints:
# 
# 	1 <= tasks.length <= 10^4
# 	tasks[i] is an uppercase English letter.
# 	0 <= n <= 100

import heapq
from collections import Counter, deque

# Solution: https://youtu.be/s8p8ukTyA2I
# Credit: Navdeep Singh founder of NeetCode
def least_interval(tasks, n):
    count = Counter(tasks)
    maxHeap = [-cnt for cnt in count.values()]
    heapq.heapify(maxHeap)

    time = 0
    q = deque()  # pairs of [-cnt, idleTime]
    while maxHeap or q:
        time += 1

        if not maxHeap:
            time = q[0][1]
        else:
            cnt = 1 + heapq.heappop(maxHeap)
            if cnt:
                q.append([cnt, time + n])
        if q and q[0][1] == time:
            heapq.heappush(maxHeap, q.popleft()[0])
    return time

# Greedy algorithm
def least_interval_alt(tasks, n):
    counter = Counter(tasks)
    max_count = max(counter.values())
    min_time = (max_count - 1) * (n + 1) + \
                sum(map(lambda count: count == max_count, counter.values()))

    return max(min_time, len(tasks))

def main():
    result = least_interval_alt(tasks = ["A","A","A","B","B","B"], n = 2)
    print(result) # 8

    result = least_interval_alt(tasks = ["A","C","A","B","D","B"], n = 1)
    print(result) # 6

    result = least_interval_alt(tasks = ["A","A","A", "B","B","B"], n = 3)
    print(result) # 10

if __name__ == "__main__":
    main()
