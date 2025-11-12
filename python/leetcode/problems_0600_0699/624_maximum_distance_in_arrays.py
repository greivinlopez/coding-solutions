# -------------------------------
# 624. Maximum Distance in Arrays
# -------------------------------

# Problem: https://leetcode.com/problems/maximum-distance-in-arrays
#
# You are given m arrays, where each array is sorted in ascending order.
# 
# You can pick up two integers from two different arrays (each array picks one)
# and calculate the distance. We define the distance between two integers a and b
# to be their absolute difference |a - b|.
# 
# Return the maximum distance.
# 
# Example 1:
# 
# Input: arrays = [[1,2,3],[4,5],[1,2,3]]
# Output: 4
# 
# Explanation: One way to reach the maximum distance 4 is to pick 1 in the first
# or third array and pick 5 in the second array.
# 
# Example 2:
# 
# Input: arrays = [[1],[1]]
# Output: 0
# 
# 
# Constraints:
#         m == arrays.length
#         2 <= m <= 10⁵
#         1 <= arrays[i].length <= 500
#         -10⁴ <= arrays[i][j] <= 10⁴
#         arrays[i] is sorted in ascending order.
#         There will be at most 10⁵ integers in all the arrays.


# Solution: https://youtu.be/J0yYlj_oVTI
# Credit: Navdeep Singh founder of NeetCode
def max_distance(arrays):
    cur_min, cur_max = arrays[0][0], arrays[0][-1]
    res = 0

    for i in range(1, len(arrays)):
        arr = arrays[i]
        res = max(
            res,
            arr[-1] - cur_min,
            cur_max - arr[0]
        )
        cur_min = min(cur_min, arr[0])
        cur_max = max(cur_max, arr[-1])

    return res
    # Time: O(n)
    # Space: O(1)


def main():
    result = max_distance(arrays = [[1,2,3],[4,5],[1,2,3]])
    print(result) # 4

    result = max_distance(arrays = [[1],[1]])
    print(result) # 0

if __name__ == "__main__":
    main()
