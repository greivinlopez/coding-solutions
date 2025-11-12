# -----------------------------------------------------------------------------------
# 1343. Number Of Sub Arrays Of Size K And Average Greater Than Or Equal To Threshold
# -----------------------------------------------------------------------------------

# Problem: https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold
#
# Given an array of integers arr and two integers k and threshold, return the
# number of sub-arrays of size k and average greater than or equal to threshold.
# 
# Example 1:
# 
# Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
# Output: 3
# Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6
# respectively. All other sub-arrays of size 3 have averages less than 4 (the
# threshold).
# 
# Example 2:
# 
# Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
# Output: 6
# Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note
# that averages are not integers.
# 
# Constraints:
#         1 <= arr.length <= 10^5
#         1 <= arr[i] <= 10^4
#         1 <= k <= arr.length
#         0 <= threshold <= 10^4


# Solution: https://youtu.be/D8B4tKxMTnY
# Credit: Navdeep Singh founder of NeetCode
def num_of_subarrays(arr, k, threshold):
    res = 0
    curSum = sum(arr[:k-1])

    for L in range(len(arr) - k + 1):
        curSum += arr[L + k - 1]
        if (curSum / k) >= threshold:
            res += 1
        curSum -= arr[L]
    return res


def main():
    result = num_of_subarrays(arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4)
    print(result) # 3

    result = num_of_subarrays(arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5)
    print(result) # 6

if __name__ == "__main__":
    main()
