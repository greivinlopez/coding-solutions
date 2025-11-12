# -----------------------------------
# 857. Minimum Cost to Hire K Workers
# -----------------------------------

# Problem: https://leetcode.com/problems/minimum-cost-to-hire-k-workers
#
# There are n workers. You are given two integer arrays quality and wage where
# quality[i] is the quality of the ith worker and wage[i] is the minimum wage
# expectation for the ith worker.
# 
# We want to hire exactly k workers to form a paid group. To hire a group of k
# workers, we must pay them according to the following rules:
#         
#   1. Every worker in the paid group must be paid at least their minimum wage
#     expectation.
#   2. In the group, each worker's pay must be directly proportional to their
#      quality. This means if a worker’s quality is double that of another worker in
#      the group, then they must be paid twice as much as the other worker.
# 
# Given the integer k, return the least amount of money needed to form a paid
# group satisfying the above conditions. Answers within 10^-5 of the actual answer
# will be accepted.
# 
# Example 1:
# 
# Input: quality = [10,20,5], wage = [70,50,30], k = 2
# Output: 105.00000
# 
# Explanation: We pay 70 to 0th worker and 35 to 2nd worker.
# 
# Example 2:
# 
# Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3
# Output: 30.66667
# 
# Explanation: We pay 4 to 0th worker, 13.33333 to 2nd and 3rd workers separately.
# 
# 
# Constraints:
#         n == quality.length == wage.length
#         1 <= k <= n <= 10^4
#         1 <= quality[i], wage[i] <= 10^4

import heapq

# Solution: https://youtu.be/f879mUH6vJk
# Credit: Navdeep Singh founder of NeetCode
def min_cost_to_hire_workers(quality, wage, k):
    res = float("inf")
    
    pairs = []
    for i in range(len(quality)):
        pairs.append((wage[i] / quality[i], quality[i]))
    pairs.sort(key=lambda p: p[0])
    
    maxHeap = []  # Qualities
    total_quality = 0
    for rate, q in pairs:
        heapq.heappush(maxHeap, -q)
        total_quality += q
        
        if len(maxHeap) > k:
            total_quality += heapq.heappop(maxHeap)
        
        if len(maxHeap) == k:
            res = min(res, total_quality * rate)
            
    return res
    # Time: O(n * log(n)) 
    # Credit: O(n)


def main():
    result = min_cost_to_hire_workers(quality = [10,20,5], wage = [70,50,30], k = 2)
    print(result) # 105.0

    result = min_cost_to_hire_workers(quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3)
    print(result) # 30.66

if __name__ == "__main__":
    main()
