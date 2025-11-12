# -----------------------------------------------------
# 1375. Number of Times Binary String Is Prefix-Aligned
# -----------------------------------------------------

# Problem: https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned
#
# You have a 1-indexed binary string of length n where all the bits are 0
# initially. We will flip all the bits of this binary string (i.e., change them
# from 0 to 1) one by one. You are given a 1-indexed integer array flips where
# flips[i] indicates that the bit at index flips[i] will be flipped in the iᵗʰ
# step.
# 
# A binary string is prefix-aligned if, after the iᵗʰ step, all the bits in the
# inclusive range [1, i] are ones and all the other bits are zeros.
# 
# Return the number of times the binary string is prefix-aligned during the
# flipping process.
# 
# Example 1:
# 
# Input: flips = [3,2,4,1,5]
# Output: 2
# 
# Explanation: The binary string is initially "00000".
# After applying step 1: The string becomes "00100", which is not prefix-aligned.
# After applying step 2: The string becomes "01100", which is not prefix-aligned.
# After applying step 3: The string becomes "01110", which is not prefix-aligned.
# After applying step 4: The string becomes "11110", which is prefix-aligned.
# After applying step 5: The string becomes "11111", which is prefix-aligned.
# We can see that the string was prefix-aligned 2 times, so we return 2.
# 
# Example 2:
# 
# Input: flips = [4,1,2,3]
# Output: 1
# 
# Explanation: The binary string is initially "0000".
# After applying step 1: The string becomes "0001", which is not prefix-aligned.
# After applying step 2: The string becomes "1001", which is not prefix-aligned.
# After applying step 3: The string becomes "1101", which is not prefix-aligned.
# After applying step 4: The string becomes "1111", which is prefix-aligned.
# We can see that the string was prefix-aligned 1 time, so we return 1.
# 
# 
# Constraints:
#         n == flips.length
#         1 <= n <= 5 * 10⁴
#         flips is a permutation of the integers in the range [1, n].


# Solution: https://algo.monster/liteproblems/1375
# Credit: AlgoMonster
def num_times_all_blue(flips):
    # Count of moments when all bulbs from 1 to some position are blue
    count_all_blue_moments = 0
    # Track the maximum bulb position flipped so far
    max_bulb_position = 0
    
    # Iterate through flips with 1-based indexing for step number
    for step_number, bulb_position in enumerate(flips, 1):
        # Update the maximum bulb position seen so far
        max_bulb_position = max(max_bulb_position, bulb_position)
        
        # All bulbs from 1 to step_number are blue if and only if
        # the maximum bulb position equals the current step number
        # (meaning we've flipped exactly bulbs 1 through step_number)
        if max_bulb_position == step_number:
            count_all_blue_moments += 1
    
    return count_all_blue_moments
    # Time: O(n)
    # Space: O(1)


def main():
    result = num_times_all_blue(flips = [3,2,4,1,5])
    print(result) # 2

    result = num_times_all_blue(flips = [4,1,2,3])
    print(result) # 1

if __name__ == "__main__":
    main()
