# -------------------------
# 1534. Count Good Triplets
# -------------------------

# Problem: https://leetcode.com/problems/count-good-triplets
#
# Given an array of integers arr, and three integers a, b and c. You need to find
# the number of good triplets.
# 
# A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:
# 
#         0 <= i < j < k < arr.length
#         |arr[i] - arr[j]| <= a
#         |arr[j] - arr[k]| <= b
#         |arr[i] - arr[k]| <= c
# 
# Where |x| denotes the absolute value of x.
# 
# Return the number of good triplets.
# 
# Example 1:
# 
# Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
# Output: 4
# 
# Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].
# 
# Example 2:
# 
# Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1
# Output: 0
# 
# Explanation: No triplet satisfies all conditions.
# 
# 
# Constraints:
#         3 <= arr.length <= 100
#         0 <= arr[i] <= 1000
#         0 <= a, b, c <= 1000


# Solution: https://youtu.be/yTTtuxccFdU
# Credit: Navdeep Singh founder of NeetCode
def count_good_triplets_alt(arr, a, b, c):
    res = 0
    n = len(arr)

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if (abs(arr[i] - arr[j]) <= a and
                        abs(arr[j] - arr[k]) <= b and
                        abs(arr[i] - arr[k]) <= c):
                    res += 1

    return res

# More efficient solution
def count_good_triplets(arr, a, b, c):
    res = 0
    n = len(arr)
    prefix_cnt = [0] * 1001

    for j in range(n - 1):
        for k in range(j + 1, n):
            if abs(arr[j] - arr[k]) <= b:
                r = min(arr[j] + a, arr[k] + c)
                l = max(arr[j] - a, arr[k] - c)

                l = max(l, 0)
                r = min(r, 1000)

                if l <= r:
                    res += prefix_cnt[r] - (0 if l == 0 else prefix_cnt[l - 1])

        for index in range(arr[j], 1001):
            prefix_cnt[index] += 1

    return res
    # Time: O(n^2 + n * m)

def main():
    result = count_good_triplets(arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3)
    print(result) # 4

    result = count_good_triplets(arr = [1,1,2,2,3], a = 0, b = 0, c = 1)
    print(result) # 0

if __name__ == "__main__":
    main()
