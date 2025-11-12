# -------------------------
# 1494. Parallel Courses II
# -------------------------

# Problem: https://leetcode.com/problems/parallel-courses-ii
#
# You are given an integer n, which indicates that there are n courses labeled
# from 1 to n. You are also given an array relations where relations[i] =
# [prevCourseᵢ, nextCourseᵢ], representing a prerequisite relationship between
# course prevCourseᵢ and course nextCourseᵢ: course prevCourseᵢ has to be taken
# before course nextCourseᵢ. Also, you are given the integer k.
# 
# In one semester, you can take at most k courses as long as you have taken all
# the prerequisites in the previous semesters for the courses you are taking.
# 
# Return the minimum number of semesters needed to take all courses. The testcases
# will be generated such that it is possible to take every course.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/05/22/leetcode_parallel_courses_1.png
# 
# Input: n = 4, relations = [[2,1],[3,1],[1,4]], k = 2
# Output: 3
# 
# Explanation: The figure above represents the given graph.
# In the first semester, you can take courses 2 and 3.
# In the second semester, you can take course 1.
# In the third semester, you can take course 4.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/05/22/leetcode_parallel_courses_2.png
# 
# Input: n = 5, relations = [[2,1],[3,1],[4,1],[1,5]], k = 2
# Output: 4
# 
# Explanation: The figure above represents the given graph.
# In the first semester, you can only take courses 2 and 3 since you cannot take
# more than two per semester.
# In the second semester, you can take course 4.
# In the third semester, you can take course 1.
# In the fourth semester, you can take course 5.
# 
# 
# Constraints:
#         1 <= n <= 15
#         1 <= k <= n
#         0 <= relations.length <= n * (n-1) / 2
#         relations[i].length == 2
#         1 <= prevCourseᵢ, nextCourseᵢ <= n
#         prevCourseᵢ != nextCourseᵢ
#         All the pairs [prevCourseᵢ, nextCourseᵢ] are unique.
#         The given graph is a directed acyclic graph.

from collections import deque

# Solution: https://algo.monster/liteproblems/1494
# Credit: AlgoMonster
def min_number_of_semesters(n, relations, k):
    # Build prerequisite bitmask for each course
    # prerequisites[i] stores a bitmask of all courses that must be taken before course i
    prerequisites = [0] * (n + 1)
    for prereq, course in relations:
        prerequisites[course] |= 1 << prereq
    
    # BFS queue: (completed_courses_bitmask, semester_count)
    queue = deque([(0, 0)])
    visited = {0}
    
    while queue:
        completed_courses, semester_count = queue.popleft()
        
        # Check if all courses are completed (bits 1 to n are set)
        # Target: 111...110 (n ones followed by a zero at bit 0)
        if completed_courses == (1 << (n + 1)) - 2:
            return semester_count
        
        # Find all courses available to take this semester
        # A course is available if all its prerequisites are completed
        available_courses = 0
        for course_id in range(1, n + 1):
            if (completed_courses & prerequisites[course_id]) == prerequisites[course_id]:
                available_courses |= 1 << course_id
        
        # Remove already completed courses from available courses
        available_courses ^= completed_courses
        
        # If we can take all available courses this semester (count <= k)
        # For Python older than 3.10 use: bin(available_courses).count('1')
        if available_courses.bit_count() <= k:
            new_state = available_courses | completed_courses
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, semester_count + 1))
        else:
            # Need to enumerate all possible k-sized subsets of available courses
            subset = available_courses
            while subset:
                # Only consider subsets of exactly k courses
                # For Python older than 3.10 use: bin(subset).count('1')
                if subset.bit_count() == k:
                    new_state = subset | completed_courses
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, semester_count + 1))
                # Generate next subset using bit manipulation trick
                # This iterates through all subsets of available_courses
                subset = (subset - 1) & available_courses
    # Time: O(3ⁿ)
    # Space: O(2ⁿ)


def main():
    result = min_number_of_semesters(n = 4, relations = [[2,1],[3,1],[1,4]], k = 2)
    print(result) # 3

    result = min_number_of_semesters(n = 5, relations = [[2,1],[3,1],[4,1],[1,5]], k = 2)
    print(result) # 4

if __name__ == "__main__":
    main()
