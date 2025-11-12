# --------------------
# 932. Beautiful Array
# --------------------

# Problem: https://leetcode.com/problems/beautiful-array
#
# An array nums of length n is beautiful if:
#         
#   * nums is a permutation of the integers in the range [1, n].
#   * For every 0 <= i < j < n, there is no index k with i < k < j where 
#     2 * nums[k] == nums[i] + nums[j].
# 
# Given the integer n, return any beautiful array nums of length n. There will be
# at least one valid answer for the given n.
# 
# Example 1:
# 
# Input: n = 4
# Output: [2,1,4,3]
# 
# Example 2:
# 
# Input: n = 5
# Output: [3,1,2,5,4]
# 
# 
# Constraints:
#         1 <= n <= 1000


# Solution: https://algo.monster/liteproblems/932
# Credit: AlgoMonster
def beautiful_array(n):
    # Base case: array of size 1 is always beautiful
    if n == 1:
        return [1]
    
    # Recursively build beautiful array for left half (ceiling division)
    # (n + 1) // 2 handles both odd and even n correctly
    left_half = beautiful_array((n + 1) // 2)
    
    # Recursively build beautiful array for right half (floor division)
    right_half = beautiful_array(n // 2)
    
    # Transform left half elements to odd numbers: 1, 3, 5, 7, ...
    odd_numbers = [x * 2 - 1 for x in left_half]
    
    # Transform right half elements to even numbers: 2, 4, 6, 8, ...
    even_numbers = [x * 2 for x in right_half]
    
    # Combine odd and even parts to form the final beautiful array
    # This works because odd + even can never equal 2 * another_number
    return odd_numbers + even_numbers
    # Time: O(n)
    # Space: O(n)


def main():
    result = beautiful_array(4)
    print(result) # [1, 3, 2, 4]

    result = beautiful_array(5)
    print(result) # [1, 5, 3, 2, 4]

if __name__ == "__main__":
    main()
