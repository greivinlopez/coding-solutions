# ---------------------------
# 1395. Count Number of Teams
# ---------------------------

# Problem: https://leetcode.com/problems/count-number-of-teams
#
# There are n soldiers standing in a line. Each soldier is assigned a unique
# rating value.
# 
# You have to form a team of 3 soldiers amongst them under the following rules:
#         
#   * Choose 3 soldiers with index (i, j, k) with rating (rating[i],
#     rating[j], rating[k]).
#   * A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] >
#     rating[j] > rating[k]) where (0 <= i < j < k < n).
# 
# Return the number of teams you can form given the conditions. (soldiers can be
# part of multiple teams).
# 
# Example 1:
# 
# Input: rating = [2,5,3,4,1]
# Output: 3
# 
# Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1),
# (5,3,1).
# 
# Example 2:
# 
# Input: rating = [2,1,3]
# Output: 0
# 
# Explanation: We can't form any team given the conditions.
# 
# Example 3:
# 
# Input: rating = [1,2,3,4]
# Output: 4
# 
# 
# Constraints:
#         n == rating.length
#         3 <= n <= 1000
#         1 <= rating[i] <= 10^5
#         All the integers in rating are unique.


# Solution: https://youtu.be/zONHzIqCr-o
# Credit: Navdeep Singh founder of NeetCode
def num_teams(rating):
    length = len(rating)
    ascend = [[0] * 4 for _ in range(length)]
    descend = [[0] * 4 for _ in range(length)]

    for i in range(length):
        ascend[i][1] = 1
        descend[i][1] = 1

    for count in range(2, 4):
        for i in range(length):
            for j in range(i + 1, length):
                if rating[i] < rating[j]:
                    ascend[i][count] += ascend[j][count - 1]
                if rating[i] > rating[j]:
                    descend[i][count] += descend[j][count - 1]

    res = 0
    for i in range(length):
        res += ascend[i][3] + descend[i][3]

    return res
    # Time: O(n^2)
    # Space: O(n)


def main():
    result = num_teams([2,5,3,4,1])
    print(result) # 3

    result = num_teams([2,1,3])
    print(result) # 0

    result = num_teams([1,2,3,4])
    print(result) # 4

if __name__ == "__main__":
    main()
