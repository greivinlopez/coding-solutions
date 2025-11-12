# ------------------------
# 2418. Sort the People 👤
# ------------------------

# Problem: https://leetcode.com/problems/sort-the-people
#
# You are given an array of strings names, and an array heights that consists of
# distinct positive integers. Both arrays are of length n.
# 
# For each index i, names[i] and heights[i] denote the name and height of the ith
# person.
# 
# Return names sorted in descending order by the people's heights.
# 
# Example 1:
# 
# Input: names = ["Mary","John","Emma"], heights = [180,165,170]
# Output: ["Mary","Emma","John"]
# 
# Explanation: Mary is the tallest, followed by Emma and John.
# 
# Example 2:
# 
# Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
# Output: ["Bob","Alice","Bob"]
# 
# Explanation: The first Bob is the tallest, followed by Alice and the second Bob.
# 
# 
# Constraints:
#         n == names.length == heights.length
#         1 <= n <= 10³
#         1 <= names[i].length <= 20
#         1 <= heights[i] <= 10⁵
#         names[i] consists of lower and upper case English letters.
#         All the values of heights are distinct.


# Solution: https://youtu.be/Zv_gXqqslbw
# Credit: Navdeep Singh founder of NeetCode
def sort_people(names, heights):
    height_to_name = {}
    for h, n in zip(heights, names):
        height_to_name[h] = n

    res = []
    for h in reversed(sorted(heights)):
        res.append(height_to_name[h])

    return res
    # Time: O(n * log(n))
    # Space: O(n)


def main():
    result = sort_people(names = ["Mary","John","Emma"], heights = [180,165,170])
    print(result) # ["Mary","Emma","John"]

    result = sort_people(names = ["Alice","Bob","Bob"], heights = [155,185,150])
    print(result) # ["Bob","Alice","Bob"]

if __name__ == "__main__":
    main()
