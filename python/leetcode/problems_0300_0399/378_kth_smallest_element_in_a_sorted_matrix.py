# --------------------------------------------
# 378. Kth Smallest Element in a Sorted Matrix
# --------------------------------------------

# Problem: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix
#
# Given an n x n matrix where each of the rows and columns is sorted in ascending
# order, return the kth smallest element in the matrix.
# 
# Note that it is the kth smallest element in the sorted order, not the kᵗʰ
# distinct element.
# 
# You must find a solution with a memory complexity better than O(n²).
# 
# Example 1:
# 
# Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# Output: 13
# 
# Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the
# 8th smallest number is 13
# 
# Example 2:
# 
# Input: matrix = [[-5]], k = 1
# Output: -5
# 
# 
# Constraints:
#         n == matrix.length == matrix[i].length
#         1 <= n <= 300
#         -10⁹ <= matrix[i][j] <= 10⁹
#         All the rows and columns of matrix are guaranteed to be sorted in non-
# decreasing order.
#         1 <= k <= n²
# 
# Follow up:
#         Could you solve the problem with a constant memory (i.e., O(1) memory
# complexity)?
#         Could you solve the problem in O(n) time complexity? The solution may be
# too advanced for an interview but you may find reading this paper fun.

import heapq

# Solution: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/solutions/440927/python-max-heap-beats-88
def kth_smallest(matrix, k):
    if not matrix or not matrix[0]:
        return -1
    heap = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            nextVal = -matrix[row][col]
            if len(heap) < k:
                heapq.heappush(heap, nextVal)
            elif nextVal > heap[0]:
                heapq.heappushpop(heap, nextVal)
    return -heap[0]
    # Time: O(n * m * log(k))
    # Space: O(k)
    # n = number of rows
    # m = number of columns


def main():
    result = kth_smallest(matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8)
    print(result) # 13

    result = kth_smallest(matrix = [[-5]], k = 1)
    print(result) # -5

if __name__ == "__main__":
    main()
