# ----------------------------------------------------------
# 1574. Shortest Subarray to be Removed to Make Array Sorted
# ----------------------------------------------------------

# Problem: https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted
#
# Given an integer array arr, remove a subarray (can be empty) from arr such that
# the remaining elements in arr are non-decreasing.
# 
# Return the length of the shortest subarray to remove.
# 
# A subarray is a contiguous subsequence of the array.
# 
# Example 1:
# 
# Input: arr = [1,2,3,10,4,2,3,5]
# Output: 3
# 
# Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The
# remaining elements after that will be [1,2,3,3,5] which are sorted.
# Another correct solution is to remove the subarray [3,10,4].
# 
# Example 2:
# 
# Input: arr = [5,4,3,2,1]
# Output: 4
# 
# Explanation: Since the array is strictly decreasing, we can only keep a single
# element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or
# [4,3,2,1].
# 
# Example 3:
# 
# Input: arr = [1,2,3]
# Output: 0
# 
# Explanation: The array is already non-decreasing. We do not need to remove any
# elements.
# 
# 
# Constraints:
#         1 <= arr.length <= 105
#         0 <= arr[i] <= 109


# Solution: https://youtu.be/eHZLQIH1ruk
# Credit: Navdeep Singh founder of NeetCode
def find_length_of_shortest_subarray(arr):
    n = len(arr)
    r = n - 1
    while r > 0 and arr[r - 1] <= arr[r]:
        r -= 1
    res = r
    l = 0
    while l < r:
        while r < n and arr[l] > arr[r]:
            r += 1
        res = min(res, r - l - 1)
        if arr[l] > arr[l + 1]:
            break
        l += 1
    return res
    # Time: O(n)
    # Space: O(1)


def main():
    result = find_length_of_shortest_subarray(arr = [1,2,3,10,4,2,3,5])
    print(result) # 3

    result = find_length_of_shortest_subarray(arr = [5,4,3,2,1])
    print(result) # 4

    result = find_length_of_shortest_subarray(arr = [1,2,3])
    print(result) # 0

if __name__ == "__main__":
    main()
