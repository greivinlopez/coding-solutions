# -------------------------
# 1399. Count Largest Group
# -------------------------

# Problem: https://leetcode.com/problems/count-largest-group
#
# You are given an integer n.
# 
# We need to group the numbers from 1 to n according to the sum of its digits. For
# example, the numbers 14 and 5 belong to the same group, whereas 13 and 3 belong
# to different groups.
# 
# Return the number of groups that have the largest size, i.e. the maximum number
# of elements.
# 
# Example 1:
# 
# Input: n = 13
# Output: 4
# 
# Explanation: There are 9 groups in total, they are grouped according sum of its
# digits of numbers from 1 to 13:
# [1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
# There are 4 groups with largest size.
# 
# Example 2:
# 
# Input: n = 2
# Output: 2
# 
# Explanation: There are 2 groups [1], [2] of size 1.
# 
# 
# Constraints:
#         1 <= n <= 10⁴

from collections import Counter

# Solution: https://algo.monster/liteproblems/1399
# Credit: AlgoMonster
def count_largest_group(n):
    # Dictionary to count frequency of each digit sum
    digit_sum_count = Counter()
    # Track the maximum group size and count of groups with that size
    num_largest_groups = 0
    max_group_size = 0
    
    # Iterate through all numbers from 1 to n
    for number in range(1, n + 1):
        # Calculate sum of digits for current number
        digit_sum = 0
        temp = number
        while temp > 0:
            digit_sum += temp % 10  # Add the last digit
            temp //= 10  # Remove the last digit
        
        # Increment count for this digit sum
        digit_sum_count[digit_sum] += 1
        
        # Update tracking variables
        if digit_sum_count[digit_sum] > max_group_size:
            # Found a new maximum group size
            max_group_size = digit_sum_count[digit_sum]
            num_largest_groups = 1
        elif digit_sum_count[digit_sum] == max_group_size:
            # Found another group with the same maximum size
            num_largest_groups += 1
    
    return num_largest_groups
    # Time: O(n * log n)
    # Space: O(log n)


def main():
    result = count_largest_group(13)
    print(result) # 4

    result = count_largest_group(2)
    print(result) # 2

if __name__ == "__main__":
    main()
