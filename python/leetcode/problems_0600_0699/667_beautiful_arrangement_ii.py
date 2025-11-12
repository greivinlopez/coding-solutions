# -----------------------------
# 667. Beautiful Arrangement II
# -----------------------------

# Problem: https://leetcode.com/problems/beautiful-arrangement-ii
#
# Given two integers n and k, construct a list answer that contains n different
# positive integers ranging from 1 to n and obeys the following requirement:
#         
#   * Suppose this list is answer = [a1, a2, a3, ... , an], then the list 
#     [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k 
#     distinct integers.
# 
# Return the list answer. If there multiple valid answers, return any of them.
# 
# Example 1:
# 
# Input: n = 3, k = 1
# Output: [1,2,3]
# 
# Explanation: The [1,2,3] has three different positive integers ranging from 1 to
# 3, and the [1,1] has exactly 1 distinct integer: 1
# 
# Example 2:
# 
# Input: n = 3, k = 2
# Output: [1,3,2]
# 
# Explanation: The [1,3,2] has three different positive integers ranging from 1 to
# 3, and the [2,1] has exactly 2 distinct integers: 1 and 2.
# 
# 
# Constraints:
#         1 <= k < n <= 10⁴


# Solution: https://algo.monster/liteproblems/667
# Credit: AlgoMonster
def construct_array(n, k):
    left, right = 1, n
    result = []
    
    # First k elements: alternate between left and right boundaries
    # This creates k distinct differences
    for i in range(k):
        if i % 2 == 0:
            # Even index: append from left side
            result.append(left)
            left += 1
        else:
            # Odd index: append from right side
            result.append(right)
            right -= 1
    
    # Remaining elements: append in sequential order
    # The order depends on whether k is even or odd
    for i in range(k, n):
        if k % 2 == 0:
            # If k is even, last element was from right, continue from right
            result.append(right)
            right -= 1
        else:
            # If k is odd, last element was from left, continue from left
            result.append(left)
            left += 1
    
    return result
    # Time: O(n)
    # Space: O(n)


def main():
    result = construct_array(n = 3, k = 1)
    print(result) # [1,2,3]

    result = construct_array(n = 3, k = 2)
    print(result) # [1,3,2]

if __name__ == "__main__":
    main()
