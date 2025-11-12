# -------------------------------------
# 470. Implement Rand10() Using Rand7()
# -------------------------------------

# Problem: https://leetcode.com/problems/implement-rand10-using-rand7
#
# Given the API rand7() that generates a uniform random integer in the range [1, 7], 
# write a function rand10() that generates a uniform random integer in the
# range [1, 10]. You can only call the API rand7(), and you shouldn't call any
# other API. Please do not use a language's built-in random API.
# 
# Each test case will have one internal argument n, the number of times that your
# implemented function rand10() will be called while testing. Note that this is
# not an argument passed to rand10().
# 
# Example 1:
# 
# Input: n = 1
# Output: [2]
# 
# Example 2:
# 
# Input: n = 2
# Output: [2,8]
# 
# Example 3:
# 
# Input: n = 3
# Output: [3,8,10]
# 
# 
# Constraints:
#         1 <= n <= 10⁵
# 
# 
# Follow up:
#         What is the expected value for the number of calls to rand7() function?
#         Could you minimize the number of calls to rand7()?

# The rand7() API is already defined for you.
import random
def rand7():
    # @return a random integer in the range 1 to 7
    return random.randint(1, 7)

# Solution: https://algo.monster/liteproblems/470
# Credit: AlgoMonster
def rand10():
    while True:
        # Generate row index (0-6) by subtracting 1 from rand7() result
        row = rand7() - 1
        
        # Generate column index (1-7) directly from rand7()
        col = rand7()
        
        # Map to a number in range 1-49 using 7x7 grid
        # row * 7 gives us 0, 7, 14, 21, 28, 35, 42
        # Adding col gives us values from 1 to 49
        combined_value = row * 7 + col
        
        # Only use values 1-40 for uniform distribution
        # Values 41-49 are rejected to ensure equal probability
        if combined_value <= 40:
            # Map 1-40 to 1-10 with equal probability (4 occurrences each)
            # combined_value % 10 gives 0-9, then add 1 to get 1-10
            return combined_value % 10 + 1
    # Time: O(1)
    # Space: O(1)


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
