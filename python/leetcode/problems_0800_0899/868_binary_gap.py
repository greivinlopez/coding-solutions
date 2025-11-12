# ---------------
# 868. Binary Gap
# ---------------

# Problem: https://leetcode.com/problems/binary-gap
#
# Given a positive integer n, find and return the longest distance between any two
# adjacent 1's in the binary representation of n. If there are no two adjacent
# 1's, return 0.
# 
# Two 1's are adjacent if there are only 0's separating them (possibly no 0's).
# The distance between two 1's is the absolute difference between their bit
# positions. For example, the two 1's in "1001" have a distance of 3.
# 
# Example 1:
# 
# Input: n = 22
# Output: 2
# 
# Explanation: 22 in binary is "10110".
# The first adjacent pair of 1's is "10110" with a distance of 2.
# The second adjacent pair of 1's is "10110" with a distance of 1.
# The answer is the largest of these two distances, which is 2.
# Note that "10110" is not a valid pair since there is a 1 separating the two 1's
# underlined.
# 
# Example 2:
# 
# Input: n = 8
# Output: 0
# 
# Explanation: 8 in binary is "1000".
# There are not any adjacent pairs of 1's in the binary representation of 8, so we
# return 0.
# 
# Example 3:
# 
# Input: n = 5
# Output: 2
# 
# Explanation: 5 in binary is "101".
# 
# 
# Constraints:
#         1 <= n <= 10⁹


# Solution: https://algo.monster/liteproblems/868
# Credit: AlgoMonster
def binary_gap(n):
    # Initialize the maximum distance
    max_distance = 0
    
    # Track the position of the previous 1 bit (initialize to infinity)
    previous_one_position = float('inf')
    
    # Track the current bit position (0-indexed from right)
    current_position = 0
    
    # Process each bit of n from right to left
    while n > 0:
        # Check if the current bit is 1
        if n & 1:
            # Calculate distance from previous 1 and update maximum
            max_distance = max(max_distance, current_position - previous_one_position)
            # Update the position of the most recent 1
            previous_one_position = current_position
        
        # Move to the next bit position
        current_position += 1
        # Right shift n by 1 to process the next bit
        n >>= 1
    
    return max_distance
    # Time: O(log(n))
    # Space: O(1)


def main():
    result = binary_gap(22)
    print(result) # 2

    result = binary_gap(8)
    print(result) # 0

    result = binary_gap(5)
    print(result) # 2

if __name__ == "__main__":
    main()
