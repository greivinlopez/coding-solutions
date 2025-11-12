# -----------------------
# 575. Distribute Candies
# -----------------------

# Problem: https://leetcode.com/problems/distribute-candies
#
# Alice has n candies, where the iᵗʰ candy is of type candyType[i]. Alice noticed
# that she started to gain weight, so she visited a doctor.
# 
# The doctor advised Alice to only eat n / 2 of the candies she has (n is always
# even). Alice likes her candies very much, and she wants to eat the maximum
# number of different types of candies while still following the doctor's advice.
# 
# Given the integer array candyType of length n, return the maximum number of
# different types of candies she can eat if she only eats n / 2 of them.
# 
# Example 1:
# 
# Input: candyType = [1,1,2,2,3,3]
# Output: 3
# 
# Explanation: Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types,
# she can eat one of each type.
# 
# Example 2:
# 
# Input: candyType = [1,1,2,3]
# Output: 2
# 
# Explanation: Alice can only eat 4 / 2 = 2 candies. Whether she eats types [1,2],
# [1,3], or [2,3], she still can only eat 2 different types.
# 
# Example 3:
# 
# Input: candyType = [6,6,6,6]
# Output: 1
# 
# Explanation: Alice can only eat 4 / 2 = 2 candies. Even though she can eat 2
# candies, she only has 1 type.
# 
# 
# Constraints:
#         n == candyType.length
#         2 <= n <= 10⁴
#         n is even.
#         -10⁵ <= candyType[i] <= 10⁵


# Solution: https://algo.monster/liteproblems/575
# Credit: AlgoMonster
def distribute_candies(candyType):
    # Calculate half the total number of candies (using bit shift for efficiency)
    # This represents the maximum number of candies that can be eaten
    max_candies_allowed = len(candyType) >> 1
    
    # Count the number of unique candy types available
    unique_candy_types = len(set(candyType))
    
    # Return the minimum between:
    # 1. The number of candies we're allowed to eat (n/2)
    # 2. The total number of unique candy types
    # This ensures we don't exceed the eating limit while maximizing variety
    return min(max_candies_allowed, unique_candy_types)


def main():
    result = distribute_candies(candyType = [1,1,2,2,3,3])
    print(result) # 3

    result = distribute_candies(candyType = [1,1,2,3])
    print(result) # 2

    result = distribute_candies(candyType = [6,6,6,6])
    print(result) # 1

if __name__ == "__main__":
    main()
