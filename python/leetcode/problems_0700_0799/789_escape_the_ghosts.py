# ----------------------
# 789. Escape The Ghosts
# ----------------------

# Problem: https://leetcode.com/problems/escape-the-ghosts
#
# You are playing a simplified PAC-MAN game on an infinite 2-D grid. You start at
# the point [0, 0], and you are given a destination point target = [xₜₐᵣ₉ₑₜ,
# yₜₐᵣ₉ₑₜ] that you are trying to get to. There are several ghosts on the map with
# their starting positions given as a 2D array ghosts, where ghosts[i] = [xᵢ, yᵢ]
# represents the starting position of the ith ghost. All inputs are integral
# coordinates.
# 
# Each turn, you and all the ghosts may independently choose to either move 1 unit
# in any of the four cardinal directions: north, east, south, or west, or stay
# still. All actions happen simultaneously.
# 
# You escape if and only if you can reach the target before any ghost reaches you.
# If you reach any square (including the target) at the same time as a ghost, it
# does not count as an escape.
# 
# Return true if it is possible to escape regardless of how the ghosts move,
# otherwise return false.
# 
# Example 1:
# 
# Input: ghosts = [[1,0],[0,3]], target = [0,1]
# Output: true
# 
# Explanation: You can reach the destination (0, 1) after 1 turn, while the ghosts
# located at (1, 0) and (0, 3) cannot catch up with you.
# 
# Example 2:
# 
# Input: ghosts = [[1,0]], target = [2,0]
# Output: false
# 
# Explanation: You need to reach the destination (2, 0), but the ghost at (1, 0)
# lies between you and the destination.
# 
# Example 3:
# 
# Input: ghosts = [[2,0]], target = [1,0]
# Output: false
# 
# Explanation: The ghost can reach the target at the same time as you.
# 
# 
# Constraints:
#         1 <= ghosts.length <= 100
#         ghosts[i].length == 2
#         -10⁴ <= xᵢ, yᵢ <= 10⁴
#         There can be multiple ghosts in the same location.
#         target.length == 2
#         -10⁴ <= xₜₐᵣ₉ₑₜ, yₜₐᵣ₉ₑₜ <= 10⁴


# Solution: https://algo.monster/liteproblems/789
# Credit: AlgoMonster
def escape_ghosts(ghosts, target):
    # Extract target coordinates
    target_x, target_y = target
    
    # Calculate player's Manhattan distance from origin to target
    player_distance = abs(target_x) + abs(target_y)
    
    # Check if all ghosts need more steps to reach target than the player
    # For each ghost, calculate Manhattan distance to target
    for ghost_x, ghost_y in ghosts:
        ghost_distance = abs(target_x - ghost_x) + abs(target_y - ghost_y)
        
        # If any ghost can reach target faster or at same time, player loses
        if ghost_distance <= player_distance:
            return False
    
    # Player can escape if no ghost can intercept
    return True
    # Time: O(n)
    # Space: O(1)


def main():
    result = escape_ghosts(ghosts = [[1,0],[0,3]], target = [0,1])
    print(result) # True

    result = escape_ghosts(ghosts = [[1,0]], target = [2,0])
    print(result) # False

    result = escape_ghosts(ghosts = [[2,0]], target = [1,0])
    print(result) # False

if __name__ == "__main__":
    main()
