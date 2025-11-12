# ------------------------------------------------
# 1342. Number of Steps to Reduce a Number to Zero
# ------------------------------------------------

# Problem: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero
#
# Given an integer num, return the number of steps to reduce it to zero.
# 
# In one step, if the current number is even, you have to divide it by 2,
# otherwise, you have to subtract 1 from it.
# 
# Example 1:
# 
# Input: num = 14
# Output: 6
# 
# Explanation: 
# Step 1) 14 is even; divide by 2 and obtain 7. 
# Step 2) 7 is odd; subtract 1 and obtain 6.
# Step 3) 6 is even; divide by 2 and obtain 3. 
# Step 4) 3 is odd; subtract 1 and obtain 2. 
# Step 5) 2 is even; divide by 2 and obtain 1. 
# Step 6) 1 is odd; subtract 1 and obtain 0.
# 
# Example 2:
# 
# Input: num = 8
# Output: 4
# 
# Explanation: 
# Step 1) 8 is even; divide by 2 and obtain 4. 
# Step 2) 4 is even; divide by 2 and obtain 2. 
# Step 3) 2 is even; divide by 2 and obtain 1. 
# Step 4) 1 is odd; subtract 1 and obtain 0.
# 
# Example 3:
# 
# Input: num = 123
# Output: 12
# 
# 
# Constraints:
#         0 <= num <= 10⁶


# Solution: https://algo.monster/liteproblems/1342
# Credit: AlgoMonster
def number_of_steps(num):
    step_count = 0
    
    # Continue until the number becomes zero
    while num > 0:
        # Check if the number is odd using bitwise AND
        if num & 1:  # Odd number (last bit is 1)
            num -= 1
        else:  # Even number (last bit is 0)
            num >>= 1  # Right shift by 1 (equivalent to dividing by 2)
        
        # Increment the step counter
        step_count += 1
    
    return step_count
    # Time: O(log n)
    # Space: O(1)


def main():
    result = number_of_steps(num = 14)
    print(result) # 6

    result = number_of_steps(num = 8)
    print(result) # 4

    result = number_of_steps(num = 123)
    print(result) # 12

if __name__ == "__main__":
    main()
