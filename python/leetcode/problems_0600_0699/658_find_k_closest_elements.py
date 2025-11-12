# ----------------------------
# 658. Find K Closest Elements
# ----------------------------

# Problem: https://leetcode.com/problems/find-k-closest-elements/
# 
# Given a sorted integer array arr, two integers k and x, return the k closest 
# integers to x in the array. The result should also be sorted in ascending 
# order.
# 
# An integer a is closer to x than an integer b if:
# 
# 	|a - x| < |b - x|, or
# 	|a - x| == |b - x| and a < b
# 
# 
# Example 1:
# 
# Input: arr = [1,2,3,4,5], k = 4, x = 3
# 
# Output: [1,2,3,4]
# 
# 
# Example 2:
# 
# Input: arr = [1,1,2,3,4,5], k = 4, x = -1
# 
# Output: [1,1,2,3]
# 
# 
# Constraints:
# 
# 	1 <= k <= arr.length
# 	1 <= arr.length <= 10^4
# 	arr is sorted in ascending order.
# 	-10^4 <= arr[i], x <= 10^4


# Solution: https://youtu.be/o-YDQzHoaKM
# Credit: Navdeep Singh founder of NeetCode
def find_closest_elements(arr, k, x):
    l, r = 0, len(arr) - k

    while l < r:
        m = (l + r) // 2
        if x - arr[m] > arr[m + k] - x:
            l = m + 1
        else:
            r = m
    return arr[l : l + k]
    # Time: O(log(n - k) + k)

# More code but also more intuitive
def find_closest_elements_alt(arr, k, x):
    l, r = 0, len(arr) - 1

    # Find index of x or the closest val to x
    val, idx = arr[0], 0
    while l <= r:
        m = (l + r) // 2
        curDiff, resDiff = abs(arr[m] - x), abs(val - x)
        if curDiff < resDiff or (curDiff == resDiff and arr[m] < val):
            val, idx = arr[m], m

        if arr[m] < x:
            l = m + 1
        elif arr[m] > x:
            r = m - 1
        else:
            break

    l = r = idx
    for i in range(k - 1):
        if l == 0:
            r += 1
        elif r == len(arr) - 1 or x - arr[l - 1] <= arr[r + 1] - x:
            l -= 1
        else:
            r += 1
    return arr[l : r + 1]
    # Time: O(log(n) + k)


def main():
    result = find_closest_elements(arr = [1,2,3,4,5], k = 4, x = 3)
    print(result) # [1,2,3,4]

    result = find_closest_elements(arr = [1,1,2,3,4,5], k = 4, x = -1)
    print(result) # [1,1,2,3]

if __name__ == "__main__":
    main()
