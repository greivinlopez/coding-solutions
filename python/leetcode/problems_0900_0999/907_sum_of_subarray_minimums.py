# -----------------------------
# 907. Sum of Subarray Minimums
# -----------------------------

# Problem: https://leetcode.com/problems/sum-of-subarray-minimums
#
# Given an array of integers arr, find the sum of min(b), where b ranges over
# every (contiguous) subarray of arr. Since the answer may be large, return the
# answer modulo 10^9 + 7.
# 
# Example 1:
# 
# Input: arr = [3,1,2,4]
# Output: 17
# 
# Explanation:
# Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4],
# [3,1,2,4].
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
# Sum is 17.
# 
# Example 2:
# 
# Input: arr = [11,81,94,43,3]
# Output: 444
# 
# 
# Constraints:
#         1 <= arr.length <= 3 * 10^4
#         1 <= arr[i] <= 3 * 10^4


# Solution: https://youtu.be/aX1F2-DrBkQ
# Credit: Navdeep Singh founder of NeetCode
def sum_subarray_mins(arr):
    MOD = 10 ** 9 + 7
    res = 0
    arr = [float("-inf")] + arr + [float("-inf")]
    stack = []  # (index, num)
    
    for i, n in enumerate(arr):
        while stack and n < stack[-1][1]:
            j, m = stack.pop()
            left = j - stack[-1][0] if stack else j + 1
            right = i - j
            res = (res + m * left * right) % MOD
        stack.append((i, n))
    
    return res
    # Time: O(n) 
    # Space: O(n)


def main():
    result = sum_subarray_mins(arr = [3,1,2,4])
    print(result) # 17

    result = sum_subarray_mins(arr = [11,81,94,43,3])
    print(result) # 444

if __name__ == "__main__":
    main()
