# ---------------------------------
# 1654. Minimum Jumps to Reach Home
# ---------------------------------

# Problem: https://leetcode.com/problems/minimum-jumps-to-reach-home
#
# A certain bug's home is on the x-axis at position x. Help them get there from
# position 0.
# 
# The bug jumps according to the following rules:
# 
#         It can jump exactly a positions forward (to the right).
#         It can jump exactly b positions backward (to the left).
#         It cannot jump backward twice in a row.
#         It cannot jump to any forbidden positions.
# 
# The bug may jump forward beyond its home, but it cannot jump to positions
# numbered with negative integers.
# 
# Given an array of integers forbidden, where forbidden[i] means that the bug
# cannot jump to the position forbidden[i], and integers a, b, and x, return the
# minimum number of jumps needed for the bug to reach its home. If there is no
# possible sequence of jumps that lands the bug on position x, return -1.
# 
# Example 1:
# 
# Input: forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
# Output: 3
# 
# Explanation: 3 jumps forward (0 -> 3 -> 6 -> 9) will get the bug home.
# 
# Example 2:
# 
# Input: forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
# Output: -1
# 
# Example 3:
# 
# Input: forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7
# Output: 2
# 
# Explanation: One jump forward (0 -> 16) then one jump backward (16 -> 7) will
# get the bug home.
# 
# 
# Constraints:
#         1 <= forbidden.length <= 1000
#         1 <= a, b, forbidden[i] <= 2000
#         0 <= x <= 2000
#         All the elements in forbidden are distinct.
#         Position x is not forbidden.

from collections import deque

# Solution: https://algo.monster/liteproblems/1654
# Credit: AlgoMonster
def minimum_jumps(forbidden, a, b, x):
    # Create a set of forbidden positions for O(1) lookup
    forbidden_positions = set(forbidden)
    
    # Initialize BFS queue with starting position (position=0, can_jump_back=1)
    # The second element tracks if we can jump backward (1=yes, 0=no)
    queue = deque([(0, 1)])
    
    # Track visited states as (position, can_jump_back) pairs
    visited = {(0, 1)}
    
    # Track the number of jumps taken
    jumps = 0
    
    # BFS to find minimum jumps to reach target position x
    while queue:
        # Process all positions at current jump level
        level_size = len(queue)
        for _ in range(level_size):
            current_pos, can_jump_back = queue.popleft()
            
            # Check if we've reached the target
            if current_pos == x:
                return jumps
            
            # Generate next possible positions
            next_positions = [(current_pos + a, 1)]  # Forward jump always allowed
            
            # Backward jump only allowed if we didn't just jump backward
            if can_jump_back & 1:  # Equivalent to: if can_jump_back == 1
                next_positions.append((current_pos - b, 0))
            
            # Process each next position
            for next_pos, next_can_jump_back in next_positions:
                # Check boundaries, forbidden positions, and if already visited
                if (0 <= next_pos < 6000 and 
                    next_pos not in forbidden_positions and 
                    (next_pos, next_can_jump_back) not in visited):
                    
                    queue.append((next_pos, next_can_jump_back))
                    visited.add((next_pos, next_can_jump_back))
        
        # Increment jump counter after processing current level
        jumps += 1
    
    # Target position unreachable
    return -1
    # Time: O(m)
    # Space: O(m)
    # m = 6000 the upper bound for positions we need to explore


def main():
    result = minimum_jumps(forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9)
    print(result) # 3

    result = minimum_jumps(forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11)
    print(result) # -1

    result = minimum_jumps(forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7)
    print(result) # 2

if __name__ == "__main__":
    main()
