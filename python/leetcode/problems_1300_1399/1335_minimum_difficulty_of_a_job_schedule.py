# ------------------------------------------
# 1335. Minimum Difficulty of a Job Schedule
# ------------------------------------------

# Problem: https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule
#
# You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work
# on the ith job, you have to finish all the jobs j where 0 <= j < i).
# 
# You have to finish at least one task every day. The difficulty of a job schedule
# is the sum of difficulties of each day of the d days. The difficulty of a day is
# the maximum difficulty of a job done on that day.
# 
# You are given an integer array jobDifficulty and an integer d. The difficulty of
# the ith job is jobDifficulty[i].
# 
# Return the minimum difficulty of a job schedule. If you cannot find a schedule
# for the jobs return -1.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/01/16/untitled.png
# 
# Input: jobDifficulty = [6,5,4,3,2,1], d = 2
# Output: 7
# 
# Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
# Second day you can finish the last job, total difficulty = 1.
# The difficulty of the schedule = 6 + 1 = 7
# 
# Example 2:
# 
# Input: jobDifficulty = [9,9,9], d = 4
# Output: -1
# 
# Explanation: If you finish a job per day you will still have a free day. you
# cannot find a schedule for the given jobs.
# 
# Example 3:
# 
# Input: jobDifficulty = [1,1,1], d = 3
# Output: 3
# 
# Explanation: The schedule is one job per day. total difficulty will be 3.
# 
# 
# Constraints:
#         1 <= jobDifficulty.length <= 300
#         0 <= jobDifficulty[i] <= 1000
#         1 <= d <= 10


# Solution: https://youtu.be/DAAULrZFeLI
# Credit: Navdeep Singh founder of NeetCode
def min_difficulty(jobDifficulty, d):
    if len(jobDifficulty) < d:
        return -1
    
    cache = {}
    def dfs(i, d, cur_max):
        if i == len(jobDifficulty):
            return 0 if d == 0 else float("inf")
        if d == 0:
            return float("inf")
        if (i, d, cur_max) in cache:
            return cache[(i, d, cur_max)]
        
        cur_max = max(cur_max, jobDifficulty[i])
        res = min(
            dfs(i + 1, d, cur_max),  # continue day
            cur_max + dfs(i + 1, d - 1, -1)  # end day
        )
        cache[(i, d, cur_max)] = res
        return res
    
    return dfs(0, d, -1)
    # Time: O(n * d * m) where m is the max value in job difficulty
    # Space: O(n * d * m) where m is the max value in job difficulty


def main():
    result = min_difficulty(jobDifficulty = [6,5,4,3,2,1], d = 2)
    print(result) # 7

    result = min_difficulty(jobDifficulty = [9,9,9], d = 4)
    print(result) # -1

    result = min_difficulty(jobDifficulty = [1,1,1], d = 3)
    print(result) # 3

if __name__ == "__main__":
    main()
