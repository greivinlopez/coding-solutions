# --------------------------------------------
# 873. Length of Longest Fibonacci Subsequence
# --------------------------------------------

# Problem: https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/
# 
# A sequence x1, x2, ..., xn is Fibonacci-like if:
# 
#   n >= 3
#   xi + xi+1 == xi+2 for all i + 2 <= n
# 
# Given a strictly increasing array arr of positive integers forming a sequence, 
# return the length of the longest Fibonacci-like subsequence of arr. If one 
# does not exist, return 0.
# 
# A subsequence is derived from another sequence arr by deleting any number of 
# elements (including none) from arr, without changing the order of the 
# remaining elements. For example, [3, 5, 8] is a subsequence of 
# [3, 4, 5, 6, 7, 8].
# 
#  
# Example 1:
# 
# Input: arr = [1,2,3,4,5,6,7,8]
# Output: 5
# Explanation: The longest subsequence that is fibonacci-like: [1,2,3,5,8].
# 
# Example 2:
# 
# Input: arr = [1,3,7,11,12,14,18]
# Output: 3
# Explanation: The longest subsequence that is fibonacci-like: 
# [1,11,12], [3,11,14] or [7,11,18].
#  
# 
# Constraints:
# 
#   3 <= arr.length <= 1000
#   1 <= arr[i] < arr[i + 1] <= 10^9


# Solution: https://youtu.be/33kCYPLnvcE
# Credit: Navdeep Singh founder of NeetCode
def len_longest_fib_subseq(arr):
    # Time: o(n^2)
    # Space: o(n^2)
    arr_map = {n:i for i,n in enumerate(arr)}
    res = 0
    dp = [[0]*len(arr) for _ in range(len(arr))]

    for i in reversed(range(len(arr) - 1)):
        for j in reversed(range(i + 1, len(arr))):
            prev, cur = arr[i],arr[j]
            next = prev + cur
            length = 2

            if next in arr_map:
                length = 1 + dp[j][arr_map[next]]
                res = max(res, length)

            dp[i][j] = length
    return res


def main():
    result = len_longest_fib_subseq([1,2,3,4,5,6,7,8])
    print(result) # 5

    result = len_longest_fib_subseq([1,3,7,11,12,14,18])
    print(result) # 3

if __name__ == "__main__":
    main()


