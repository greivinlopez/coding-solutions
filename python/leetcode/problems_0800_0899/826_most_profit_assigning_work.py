# -------------------------------
# 826. Most Profit Assigning Work
# -------------------------------

# Problem: https://leetcode.com/problems/most-profit-assigning-work
#
# You have n jobs and m workers. You are given three arrays: difficulty, profit,
# and worker where:
#         
#   * difficulty[i] and profit[i] are the difficulty and the profit of the iᵗʰ job, and
#   * worker[j] is the ability of jth worker (i.e., the jth worker can only complete a 
#     job with difficulty at most worker[j]).
# 
# Every worker can be assigned at most one job, but one job can be completed
# multiple times.
#         
#   * For example, if three workers attempt the same job that pays $1, then the total 
#     profit will be $3. If a worker cannot complete any job, their profit is $0.
# 
# Return the maximum profit we can achieve after assigning the workers to the jobs.
# 
# Example 1:
# 
# Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
# Output: 100
# 
# Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get a
# profit of [20,20,30,30] separately.
# 
# Example 2:
# 
# Input: difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]
# Output: 0
# 
# 
# Constraints:
#         n == difficulty.length
#         n == profit.length
#         m == worker.length
#         1 <= n, m <= 10⁴
#         1 <= difficulty[i], profit[i], worker[i] <= 10⁵


# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def max_profit_assignment(difficulty, profit, worker):
    job_profile = [(0, 0)]
    for i in range(len(difficulty)):
        job_profile.append((difficulty[i], profit[i]))
    # Sort by difficulty values in increasing order.

    job_profile.sort()
    for i in range(len(job_profile) - 1):
        job_profile[i + 1] = (
            job_profile[i + 1][0],
            max(job_profile[i][1], job_profile[i + 1][1]),
        )
    net_profit = 0
    for i in range(len(worker)):
        ability = worker[i]

        # Find the job with just smaller or equal difficulty than ability.

        l, r = 0, len(job_profile) - 1
        job_profit = 0
        while l <= r:
            mid = (l + r) // 2
            if job_profile[mid][0] <= ability:
                job_profit = max(job_profit, job_profile[mid][1])
                l = mid + 1
            else:
                r = mid - 1
        # Increment profit of current worker to total profit.

        net_profit += job_profit
    return net_profit
    # Time: O(n * log(n) + m * log(n))
    # Space: (n)
    # n = the number of jobs
    # m = the number of workers


def main():
    result = max_profit_assignment([2,4,6,8,10], [10,20,30,40,50], [4,5,6,7])
    print(result) # 100

    result = max_profit_assignment([85,47,57], [24,66,99], [40,25,25])
    print(result) # 0

if __name__ == "__main__":
    main()
