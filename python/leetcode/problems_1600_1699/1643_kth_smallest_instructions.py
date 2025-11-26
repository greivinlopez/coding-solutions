# -------------------------------
# 1643. Kth Smallest Instructions
# -------------------------------

# Problem: https://leetcode.com/problems/kth-smallest-instructions
#
# Bob is standing at cell (0, 0), and he wants to reach destination: (row,
# column). He can only travel right and down. You are going to help Bob by
# providing instructions for him to reach destination.
# 
# The instructions are represented as a string, where each character is either:
#         
#   * 'H', meaning move horizontally (go right), or
#   * 'V', meaning move vertically (go down).
# 
# Multiple instructions will lead Bob to destination. For example, if destination
# is (2, 3), both "HHHVV" and "HVHVH" are valid instructions.
# 
# However, Bob is very picky. Bob has a lucky number k, and he wants the kth
# lexicographically smallest instructions that will lead him to destination. k is
# 1-indexed.
# 
# Given an integer array destination and an integer k, return the kth
# lexicographically smallest instructions that will take Bob to destination.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/10/12/ex1.png
# 
# Input: destination = [2,3], k = 1
# Output: "HHHVV"
# 
# Explanation: All the instructions that reach (2, 3) in lexicographic order are
# as follows:
# ["HHHVV", "HHVHV", "HHVVH", "HVHHV", "HVHVH", "HVVHH", "VHHHV", "VHHVH",
# "VHVHH", "VVHHH"].
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/10/12/ex2.png
# 
# Input: destination = [2,3], k = 2
# Output: "HHVHV"
# 
# Example 3:
# 
# https://assets.leetcode.com/uploads/2020/10/12/ex3.png
# 
# Input: destination = [2,3], k = 3
# Output: "HHVVH"
# 
# 
# Constraints:
#         destination.length == 2
#         1 <= row, column <= 15
#         1 <= k <= nCr(row + column, row), where nCr(a, b) denotes a choose b​​​​​.


# Solution: https://algo.monster/liteproblems/1643
# Credit: AlgoMonster
def kth_smallest_path(destination, k):
    from math import comb

    # Extract vertical and horizontal distances to destination
    vertical_moves, horizontal_moves = destination
    result_path = []
    
    # Build the path character by character
    for _ in range(horizontal_moves + vertical_moves):
        if horizontal_moves == 0:
            # No more horizontal moves left, must go vertical
            result_path.append("V")
        else:
            # Calculate number of paths that start with 'H'
            # This is the number of ways to arrange remaining moves after placing 'H'
            paths_starting_with_h = comb(horizontal_moves + vertical_moves - 1, 
                                        horizontal_moves - 1)
            
            if k > paths_starting_with_h:
                # k-th path starts with 'V' since it's beyond paths starting with 'H'
                result_path.append("V")
                vertical_moves -= 1
                # Adjust k to find position among paths starting with 'V'
                k -= paths_starting_with_h
            else:
                # k-th path starts with 'H'
                result_path.append("H")
                horizontal_moves -= 1
    
    return "".join(result_path)
    # Time: O(n²) 
    # Space: O(n)
    # n = h + v


def main():
    result = kth_smallest_path(destination = [2,3], k = 1)
    print(result) # "HHHVV"

    result = kth_smallest_path(destination = [2,3], k = 2)
    print(result) # "HHVHV"

    result = kth_smallest_path(destination = [2,3], k = 3)
    print(result) # "HHVVH"

if __name__ == "__main__":
    main()
