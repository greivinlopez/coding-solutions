# -----------------------------------------------------
# 1217. Minimum Cost to Move Chips to The Same Position
# -----------------------------------------------------

# Problem: https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position
#
# We have n chips, where the position of the ith chip is position[i].
# 
# We need to move all the chips to the same position. In one step, we can change
# the position of the ith chip from position[i] to:
# 
#         position[i] + 2 or position[i] - 2 with cost = 0.
#         position[i] + 1 or position[i] - 1 with cost = 1.
# 
# Return the minimum cost needed to move all the chips to the same position.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/08/15/chips_e1.jpg
# 
# Input: position = [1,2,3]
# Output: 1
# Explanation: First step: Move the chip at position 3 to position 1 with cost =
# 0.
# Second step: Move the chip at position 2 to position 1 with cost = 1.
# Total cost is 1.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/08/15/chip_e2.jpg
# 
# Input: position = [2,2,2,3,3]
# Output: 2
# 
# Explanation: We can move the two chips at position  3 to position 2. Each move
# has cost = 1. The total cost = 2.
# 
# Example 3:
# 
# Input: position = [1,1000000000]
# Output: 1
# 
# 
# Constraints:
#         1 <= position.length <= 100
#         1 <= position[i] <= 10⁹


# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def min_cost_to_move_chips(position):
    even_cnt = 0
    odd_cnt = 0
    
    for num in position:
        if num%2 == 0:
            even_cnt += 1
        else:
            odd_cnt += 1
            
    return min(even_cnt, odd_cnt)
    # Time: O(n)
    # Space: O(1)


def main():
    result = min_cost_to_move_chips(position = [1,2,3])
    print(result) # 1

    result = min_cost_to_move_chips(position = [2,2,2,3,3])
    print(result) # 2

    result = min_cost_to_move_chips(position = [1,1000000000])
    print(result) # 1

if __name__ == "__main__":
    main()
