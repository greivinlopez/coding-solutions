# ----------------------
# 1362. Closest Divisors
# ----------------------

# Problem: https://leetcode.com/problems/closest-divisors
#
# Given an integer num, find the closest two integers in absolute difference whose
# product equals num + 1 or num + 2.
# 
# Return the two integers in any order.
# 
# Example 1:
# 
# Input: num = 8
# Output: [3,3]
# 
# Explanation: For num + 1 = 9, the closest divisors are 3 & 3, for num + 2 = 10,
# the closest divisors are 2 & 5, hence 3 & 3 is chosen.
# 
# Example 2:
# 
# Input: num = 123
# Output: [5,25]
# 
# Example 3:
# 
# Input: num = 999
# Output: [40,25]
# 
# 
# Constraints:
#         1 <= num <= 10^9

from math import sqrt

# Solution: https://algo.monster/liteproblems/1362
# Credit: AlgoMonster
def closest_divisors(num):

    def find_closest_divisor_pair(target):
        # Start from sqrt(target) and iterate downwards
        # The first divisor found will give the minimal difference
        for divisor in range(int(sqrt(target)), 0, -1):
            if target % divisor == 0:
                # Return both divisors as a pair
                return [divisor, target // divisor]
    
    # Find divisor pairs for both num+1 and num+2
    divisors_num_plus_1 = find_closest_divisor_pair(num + 1)
    divisors_num_plus_2 = find_closest_divisor_pair(num + 2)
    
    # Return the pair with smaller absolute difference
    if abs(divisors_num_plus_1[0] - divisors_num_plus_1[1]) < abs(divisors_num_plus_2[0] - divisors_num_plus_2[1]):
        return divisors_num_plus_1
    else:
        return divisors_num_plus_2
    # Time: O(√num)
    # Space: O(1)


def main():
    result = closest_divisors(num = 8)
    print(result) # [3, 3]

    result = closest_divisors(num = 123)
    print(result) # [5, 25]

    result = closest_divisors(num = 999)
    print(result) # [25, 40]

if __name__ == "__main__":
    main()
