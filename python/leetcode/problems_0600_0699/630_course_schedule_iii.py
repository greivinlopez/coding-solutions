# ------------------------
# 630. Course Schedule III
# ------------------------

# Problem: https://leetcode.com/problems/course-schedule-iii
#
# There are n different online courses numbered from 1 to n. You are given an
# array courses where courses[i] = [durationi, lastDayi] indicate that the ith
# course should be taken continuously for durationi days and must be finished
# before or on lastDayi.
# 
# You will start on the 1st day and you cannot take two or more courses
# simultaneously.
# 
# Return the maximum number of courses that you can take.
# 
# Example 1:
# 
# Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
# Output: 3
# 
# Explanation:
# There are totally 4 courses, but you can take 3 courses at most:
# First, take the 1st course, it costs 100 days so you will finish it on the 100th
# day, and ready to take the next course on the 101st day.
# Second, take the 3rd course, it costs 1000 days so you will finish it on the
# 1100th day, and ready to take the next course on the 1101st day.
# Third, take the 2nd course, it costs 200 days so you will finish it on the
# 1300th day.
# The 4th course cannot be taken now, since you will finish it on the 3300th day,
# which exceeds the closed date.
# 
# Example 2:
# 
# Input: courses = [[1,2]]
# Output: 1
# 
# Example 3:
# 
# Input: courses = [[3,2],[4,3]]
# Output: 0
# 
# 
# Constraints:
#         1 <= courses.length <= 10⁴
#         1 <= durationi, lastDayi <= 10⁴

from heapq import heappush, heappop

# Solution: https://algo.monster/liteproblems/630
# Credit: AlgoMonster
def schedule_course(courses):
    # Sort the courses based on their end day
    courses.sort(key=lambda x: x[1])
    
    # Initialize a max heap to keep track of the longest courses we have taken
    max_heap = []
    
    # This variable will hold the total duration of all courses we have taken so far
    total_duration = 0
    
    # Iterate over each course
    for duration, last_day in courses:
        # Add the current course to the max heap and increment the total duration
        heappush(max_heap, -duration)
        total_duration += duration
        
        # If the total duration exceeds the last day of the current course,
        # remove the longest course from our schedule
        while total_duration > last_day:
            # heappop returns a negative number because we are using max heap,
            # so we add it back to reduce the total duration
            total_duration += heappop(max_heap)
    
    # The number of courses in the max heap is the number of courses we can take
    return len(max_heap)
    # Time: O(n * log(n))
    # Space: O(n)


def main():
    result = schedule_course([[100,200],[200,1300],[1000,1250],[2000,3200]])
    print(result) # 3

    result = schedule_course([[1,2]])
    print(result) # 1

    result = schedule_course([[3,2],[4,3]])
    print(result) # 0

if __name__ == "__main__":
    main()
