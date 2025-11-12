# ------------------------------------------------------------
# 1439. Find the Kth Smallest Sum of a Matrix With Sorted Rows
# ------------------------------------------------------------

# Problem: https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows
#
# You are given an m x n matrix mat that has its rows sorted in non-decreasing
# order and an integer k.
# 
# You are allowed to choose exactly one element from each row to form an array.
# 
# Return the kᵗʰ smallest array sum among all possible arrays.
# 
# Example 1:
# 
# Input: mat = [[1,3,11],[2,4,6]], k = 5
# Output: 7
# 
# Explanation: Choosing one element from each row, the first k smallest sum are:
# [1,2], [1,4], [3,2], [3,4], [1,6]. Where the 5th sum is 7.
# 
# Example 2:
# 
# Input: mat = [[1,3,11],[2,4,6]], k = 9
# Output: 17
# 
# Example 3:
# 
# Input: mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
# Output: 9
# 
# Explanation: Choosing one element from each row, the first k smallest sum are:
# [1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]. Where the 7th sum
# is 9.
# 
# 
# Constraints:
#         m == mat.length
#         n == mat.length[i]
#         1 <= m, n <= 40
#         1 <= mat[i][j] <= 5000
#         1 <= k <= min(200, nᵐ)
#         mat[i] is a non-decreasing array.


# Solution: https://algo.monster/liteproblems/1439
# Credit: AlgoMonster
def kth_smallest(mat, k):
    # Initialize with a single element 0, representing the sum before processing any row
    previous_sums = [0]
    
    # Process each row in the matrix
    for current_row in mat:
        # Generate all possible sums by adding each element from current row
        # to each sum from previous rows
        # Only consider first k elements from current row for optimization
        all_new_sums = []
        for prev_sum in previous_sums:
            for element in current_row[:k]:
                all_new_sums.append(prev_sum + element)
        
        # Sort all new sums and keep only the k smallest ones
        # This ensures we maintain at most k candidates for the final answer
        previous_sums = sorted(all_new_sums)[:k]
    
    # The k-th smallest sum is the last element in our k smallest sums
    return previous_sums[-1]
    # Time: O(n * k² * log(k))
    # Space: O(k²)


def main():
    result = kth_smallest(mat = [[1,3,11],[2,4,6]], k = 5)
    print(result) # 7

    result = kth_smallest(mat = [[1,3,11],[2,4,6]], k = 9)
    print(result) # 17

    result = kth_smallest(mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7)
    print(result) # 9

if __name__ == "__main__":
    main()
