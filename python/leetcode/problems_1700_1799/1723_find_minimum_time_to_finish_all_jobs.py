# ---------------------------------------------
# 1723. Find Minimum Time to Finish All Jobs ⏱️
# ---------------------------------------------

# Problem: https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs
#
# You are given an integer array jobs, where jobs[i] is the amount of time it
# takes to complete the iᵗʰ job.
# 
# There are k workers that you can assign jobs to. Each job should be assigned to
# exactly one worker. The working time of a worker is the sum of the time it takes
# to complete all jobs assigned to them. Your goal is to devise an optimal
# assignment such that the maximum working time of any worker is minimized.
# 
# Return the minimum possible maximum working time of any assignment.
# 
# Example 1:
# 
# Input: jobs = [3,2,3], k = 3
# Output: 3
# 
# Explanation: By assigning each person one job, the maximum time is 3.
# 
# Example 2:
# 
# Input: jobs = [1,2,4,7,8], k = 2
# Output: 11
# 
# Explanation: Assign the jobs the following way:
# Worker 1: 1, 2, 8 (working time = 1 + 2 + 8 = 11)
# Worker 2: 4, 7 (working time = 4 + 7 = 11)
# The maximum working time is 11.
# 
# 
# Constraints:
#         1 <= k <= jobs.length <= 12
#         1 <= jobs[i] <= 10⁷


# Solution: https://algo.monster/liteproblems/1723
# Credit: AlgoMonster
def minimum_time_required(jobs, k):
    from math import inf

    def backtrack(job_index):
        nonlocal min_max_time
        
        # Base case: all jobs have been assigned
        if job_index == len(jobs):
            # Update the minimum maximum time if current assignment is better
            min_max_time = min(min_max_time, max(worker_times))
            return
        
        # Try assigning current job to each worker
        for worker_id in range(k):
            # Pruning: skip if this assignment would exceed current best answer
            if worker_times[worker_id] + jobs[job_index] >= min_max_time:
                continue
            
            # Assign job to current worker
            worker_times[worker_id] += jobs[job_index]
            
            # Recursively assign remaining jobs
            backtrack(job_index + 1)
            
            # Backtrack: remove job from current worker
            worker_times[worker_id] -= jobs[job_index]
            
            # Optimization: if worker had no jobs before, no need to try other empty workers
            # (they would produce identical results due to symmetry)
            if worker_times[worker_id] == 0:
                break
    
    # Initialize worker time tracking array
    worker_times = [0] * k
    
    # Sort jobs in descending order for better pruning efficiency
    # (larger jobs assigned first lead to earlier pruning)
    jobs.sort(reverse=True)
    
    # Initialize minimum maximum time to infinity
    min_max_time = inf
    
    # Start backtracking from the first job
    backtrack(0)
    
    return min_max_time
    # Time: O(kⁿ)
    # Space: O(n + k)
    # n = the number of jobs


def main():
    result = minimum_time_required(jobs = [3,2,3], k = 3)
    print(result) # 3

    result = minimum_time_required(jobs = [1,2,4,7,8], k = 2)
    print(result) # 11

if __name__ == "__main__":
    main()
