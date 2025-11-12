# ----------------
# 818. Race Car 🏎️
# ----------------

# Problem: https://leetcode.com/problems/race-car
#
# Your car starts at position 0 and speed +1 on an infinite number line. Your car
# can go into negative positions. Your car drives automatically according to a
# sequence of instructions 'A' (accelerate) and 'R' (reverse):
# 
#         When you get an instruction 'A', your car does the following:
#   
#                 position += speed
#                 speed *= 2
# 
#         When you get an instruction 'R', your car does the following:
# 
#                 If your speed is positive then speed = -1
#                 otherwise speed = 1
#  
#         Your position stays the same.
# 
# For example, after commands "AAR", your car goes to positions 0 --> 1 --> 3 -->
# 3, and your speed goes to 1 --> 2 --> 4 --> -1.
# 
# Given a target position target, return the length of the shortest sequence of
# instructions to get there.
# 
# Example 1:
# 
# Input: target = 3
# Output: 2
# 
# Explanation:
# The shortest instruction sequence is "AA".
# Your position goes from 0 --> 1 --> 3.
# 
# Example 2:
# 
# Input: target = 6
# Output: 5
# 
# Explanation:
# The shortest instruction sequence is "AAARA".
# Your position goes from 0 --> 1 --> 3 --> 7 --> 7 --> 6.
# 
# 
# Constraints:
#         1 <= target <= 10⁴


# Solution: https://algo.monster/liteproblems/818
# Credit: AlgoMonster
def race_car(target):
    # dp[i] stores the minimum number of instructions to reach position i
    dp = [0] * (target + 1)
    
    # Calculate minimum instructions for each position from 1 to target
    for position in range(1, target + 1):
        # Calculate the number of bits needed to represent the position
        # This represents the minimum accelerations needed if we go straight
        bits_needed = position.bit_length()
        
        # Check if position is exactly reachable by continuous acceleration
        # (i.e., position is of the form 2^k - 1)
        if position == 2**bits_needed - 1:
            # Can reach this position with exactly k accelerations
            dp[position] = bits_needed
            continue
        
        # Case 1: Overshoot the target and then reverse
        # Go to (2^k - 1), then reverse and cover the remaining distance
        overshoot_position = 2**bits_needed - 1
        remaining_distance = overshoot_position - position
        dp[position] = dp[remaining_distance] + bits_needed + 1
        
        # Case 2: Undershoot, reverse, go back some distance, then reverse again
        # Try different amounts of backward movement
        for backward_steps in range(bits_needed - 1):
            # Forward distance: 2^(k-1) - 1 (one bit less than full)
            # Backward distance: 2^j - 1 (where j is backward_steps)
            forward_distance = 2**(bits_needed - 1) - 1
            backward_distance = 2**backward_steps - 1
            net_distance = forward_distance - backward_distance
            
            # Calculate remaining distance to target
            remaining = position - net_distance
            
            # Total instructions: (k-1) forward + 1 reverse + j backward + 1 reverse + remaining
            instructions = (bits_needed - 1) + 1 + backward_steps + 1 + dp[remaining]
            dp[position] = min(dp[position], instructions)
    
    return dp[target]
    # Time: O(n * log(n))
    # Space: O(n)


def main():
    result = race_car(target = 3)
    print(result) # 2

    result = race_car(target = 6)
    print(result) # 5

if __name__ == "__main__":
    main()
