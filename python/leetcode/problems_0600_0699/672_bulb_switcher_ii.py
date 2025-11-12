# ------------------------
# 672. Bulb Switcher II 💡
# ------------------------

# Problem: https://leetcode.com/problems/bulb-switcher-ii
#
# There is a room with n bulbs labeled from 1 to n that all are turned on
# initially, and four buttons on the wall. Each of the four buttons has a
# different functionality where:
# 
#   * Button 1: Flips the status of all the bulbs.
#   * Button 2: Flips the status of all the bulbs with even labels (i.e., 2,
#     4, ...).
#   * Button 3: Flips the status of all the bulbs with odd labels (i.e., 1, 3, ...).
#   * Button 4: Flips the status of all the bulbs with a label j = 3k + 1
#     where k = 0, 1, 2, ... (i.e., 1, 4, 7, 10, ...).
# 
# You must make exactly presses button presses in total. For each press, you may
# pick any of the four buttons to press.
# 
# Given the two integers n and presses, return the number of different possible
# statuses after performing all presses button presses.
# 
# Example 1:
# 
# Input: n = 1, presses = 1
# Output: 2
# 
# Explanation: Status can be:
# - [off] by pressing button 1
# - [on] by pressing button 2
# 
# Example 2:
# 
# Input: n = 2, presses = 1
# Output: 3
# 
# Explanation: Status can be:
# - [off, off] by pressing button 1
# - [on, off] by pressing button 2
# - [off, on] by pressing button 3
# 
# Example 3:
# 
# Input: n = 3, presses = 1
# Output: 4
# 
# Explanation: Status can be:
# - [off, off, off] by pressing button 1
# - [off, on, off] by pressing button 2
# - [on, off, on] by pressing button 3
# - [off, on, on] by pressing button 4
# 
# 
# Constraints:
#         1 <= n <= 1000
#         0 <= presses <= 1000


# Solution: https://algo.monster/liteproblems/672
# Credit: AlgoMonster
def flip_lights(n, presses):
    # Define the four button operations as bit patterns (for up to 6 lights)
    # Each bit represents whether that light gets flipped (1) or not (0)
    button_operations = (
        0b111111,  # Button 1: Flip all lights (lights 1-6)
        0b010101,  # Button 2: Flip even-positioned lights (2, 4, 6)
        0b101010,  # Button 3: Flip odd-positioned lights (1, 3, 5)
        0b100100   # Button 4: Flip lights at positions 3k+1 (1, 4)
    )
    
    # Limit n to 6 since the pattern repeats after 6 lights
    # This optimization works because the button patterns have a cycle of 6
    n = min(n, 6)
    
    # Set to store unique final light states
    unique_states = set()
    
    # Try all possible combinations of button presses (2^4 = 16 combinations)
    for button_combination in range(1 << 4):
        # Count how many buttons are pressed in this combination
        # This will work only on Python 3.10+
        # buttons_pressed = button_combination.bit_count()
        buttons_pressed = bin(button_combination).count('1')
        
        # Check if this combination is valid:
        # 1. We can't press more buttons than allowed
        # 2. The parity must match (pressing a button twice cancels out)
        if buttons_pressed <= presses and buttons_pressed % 2 == presses % 2:
            # Initialize the final state (all lights initially on)
            final_state = 0
            
            # Apply each selected button operation
            for button_index, operation in enumerate(button_operations):
                # Check if this button is pressed in the current combination
                if (button_combination >> button_index) & 1:
                    # XOR applies the flip operation
                    final_state ^= operation
            
            # Mask to keep only the first 6 bits
            final_state &= (1 << 6) - 1
            
            # Shift right to keep only the first n bits
            # This handles cases where n < 6
            final_state >>= (6 - n)
            
            # Add this unique state to our set
            unique_states.add(final_state)
    
    # Return the number of unique states achievable
    return len(unique_states)
    # Time: O(1)
    # Space: O(1)


def main():
    result = flip_lights(n = 1, presses = 1)
    print(result) # 2

    result = flip_lights(n = 2, presses = 1)
    print(result) # 3

    result = flip_lights(n = 3, presses = 1)
    print(result) # 4

if __name__ == "__main__":
    main()
