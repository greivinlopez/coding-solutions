# -------------------------------
# 978. Longest Turbulent Subarray
# -------------------------------

# Problem: https://leetcode.com/problems/longest-turbulent-subarray
#
# 
# Given an integer array arr, return the length of a maximum size turbulent
# subarray of arr.
# 
# A subarray is turbulent if the comparison sign flips between each adjacent pair
# of elements in the subarray.
# 
# More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be
# turbulent if and only if:
# 
#         For i <= k < j:
#                 arr[k] > arr[k + 1] when k is odd, and
#                 arr[k] < arr[k + 1] when k is even.
#         Or, for i <= k < j:
#                 arr[k] > arr[k + 1] when k is even, and
#                 arr[k] < arr[k + 1] when k is odd.
# 
# 
# Example 1:
# 
# Input: arr = [9,4,2,10,7,8,8,1,9]
# Output: 5
# Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
# 
# Example 2:
# Input: arr = [4,8,12,16]
# Output: 2
# 
# Example 3:
# Input: arr = [100]
# Output: 1
# 
# 
# Constraints:
# 
#         1 <= arr.length <= 4 * 10^4
#         0 <= arr[i] <= 10^9

# Solution: https://youtu.be/V_iHUhR8Dek
# Credit: Navdeep Singh founder of NeetCode
def max_turbulence_size(arr):
    l, r = 0, 1
    res, prev = 1, ""

    while r < len(arr):
        if arr[r - 1] > arr[r] and prev != ">":
            res = max(res, r - l + 1)
            r += 1
            prev = ">"
        elif arr[r - 1] < arr[r] and prev != "<":
            res = max(res, r - l + 1)
            r += 1
            prev = "<"
        else:
            r = r + 1 if arr[r] == arr[r - 1] else r
            l = r - 1
            prev = ""
    return res


def main():
    result = max_turbulence_size([9,4,2,10,7,8,8,1,9])
    print(result) # 5

    result = max_turbulence_size([4,8,12,16])
    print(result) # 2

    result = max_turbulence_size([100])
    print(result) # 1

if __name__ == "__main__":
    main()
