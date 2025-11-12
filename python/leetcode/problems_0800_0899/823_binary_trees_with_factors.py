# ------------------------------
# 823. Binary Trees With Factors
# ------------------------------

# Problem: https://leetcode.com/problems/binary-trees-with-factors
#
# Given an array of unique integers, arr, where each integer arr[i] is strictly
# greater than 1.
# 
# We make a binary tree using these integers, and each number may be used for any
# number of times. Each non-leaf node's value should be equal to the product of
# the values of its children.
# 
# Return the number of binary trees we can make. The answer may be too large so
# return the answer modulo 10⁹ + 7.
# 
# Example 1:
# 
# Input: arr = [2,4]
# Output: 3
# 
# Explanation: We can make these trees: [2], [4], [4, 2, 2]
# 
# Example 2:
# 
# Input: arr = [2,4,5,10]
# Output: 7
# 
# Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2,
# 5], [10, 5, 2].
# 
# 
# Constraints:
#         1 <= arr.length <= 1000
#         2 <= arr[i] <= 10⁹
#         All the values of arr are unique.


# Credit: Jeel Gajera -> https://github.com/JeelGajera
def num_factored_binary_trees(arr):
    arr.sort()
    dp = {x:1 for x in arr}
    for i in arr:
        for j in arr:
            if i == j:
                break
            if i % j == 0 and i // j in dp:
                dp[i] += dp[j] * dp[i // j]
    return sum(dp.values()) % (pow(10,9) + 7)
    # Time: O(n²)
    # Space: O(n)


def main():
    result = num_factored_binary_trees(arr = [2,4])
    print(result) # 3

    result = num_factored_binary_trees(arr = [2,4,5,10])
    print(result) # 7

if __name__ == "__main__":
    main()
